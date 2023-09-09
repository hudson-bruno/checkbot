from typing import Optional

from discord import Interaction, app_commands
from discord.ext import commands

from check.repositories.in_memory_check_repository import InMemoryCheckRepository
from check.use_cases.check import CheckUseCase, CheckUseCaseDTO
from check.validators.check_validator import CheckParametersValidator


class CheckCog(commands.Cog):
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
        dto_params = CheckParametersValidator(user=ctx.user, date=date).model_dump()
        dto = CheckUseCaseDTO(**dto_params)
        use_case = CheckUseCase(self.repository)

        check = await use_case.execute(dto)

        await ctx.response.send_message(
            f"{check.user.mention} checked at {check.date.strftime('%d/%m/%y %H:%M')}!"
        )
