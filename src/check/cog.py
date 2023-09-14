import logging
from typing import Optional

from discord import Interaction, app_commands
from discord.ext import commands

from check.repositories.in_memory_check_repository import InMemoryCheckRepository
from check.use_cases.check import CheckUseCase
from check.validators.jsonschema.jsonschema_check_validator import (
    JsonSchemaCheckValidator,
)
from core.exceptions import AppValidationError


class CheckCog(commands.Cog):
    logger = logging.getLogger("CheckCog")

    def __init__(self, bot):
        self.bot = bot
        self.repository = InMemoryCheckRepository()

    @app_commands.command()
    @app_commands.describe(date="custom date, ex: 1/1/23 13:59")
    async def check(
        self,
        ctx: Interaction,
        date: Optional[str],
    ):
        dto = JsonSchemaCheckValidator.convertToDto(user=ctx.user, date=date)
        use_case = CheckUseCase(self.repository)
        check = await use_case.execute(dto)

        await ctx.response.send_message(
            f"{check.user.mention} checked at {check.date.strftime('%d/%m/%y %H:%M')}!",
            ephemeral=True,
        )

    async def cog_app_command_error(self, interaction, error):
        if isinstance(error, app_commands.CommandInvokeError):
            if isinstance(error.original, AppValidationError):
                return await interaction.response.send_message(
                    error.original, ephemeral=True
                )

        self.logger.error(error)
