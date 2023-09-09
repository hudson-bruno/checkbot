from datetime import datetime
from typing import Callable, Optional

from discord.ext import commands
from discord.ext.commands.context import Context

from check.repositories.in_memory_check_repository import InMemoryCheckRepository
from check.use_cases.check import CheckUseCase, CheckUseCaseDTO


class DateConverter:
    def __init__(self, *, default: Callable) -> None:
        self.default = default

    async def convert(self, argument: Optional[str]):
        if argument is None:
            if callable(self.default):
                return self.default()
            raise Exception("argument used as optional when default is None")

        return datetime.strptime(argument, "%d/%m/%y %H:%M")


class CheckCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.repository = InMemoryCheckRepository()

    @commands.command()
    async def check(self, ctx: Context, *, arg: Optional[str]):
        try:
            converter = DateConverter(default=datetime.utcnow)
            date = await converter.convert(arg)
        except Exception as e:
            return await ctx.send(str(e))

        use_case = CheckUseCase(self.repository)

        check = await use_case.execute(CheckUseCaseDTO(ctx.author, date))

        await ctx.send(
            f"{check.user.mention} checked at {check.date.strftime('%d/%m/%y %H:%M')}!"
        )
