import asyncio
import logging

import discord
from discord.ext import commands

import config
from check.cog import CheckCog


async def main():
    logger = logging.getLogger("checkbot")

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=config.BOT_PREFIX, intents=intents)

    @bot.listen("on_ready")
    async def on_ready():
        logger.info(f"Logged in as {bot.user}")

        try:
            await bot.tree.sync()
        except Exception as e:
            logger.warning(f"Failed to sync commands: {e}")

    await bot.add_cog(CheckCog(bot))
    await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
