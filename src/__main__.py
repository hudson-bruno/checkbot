import asyncio

import discord
from discord.ext import commands

import config
from check.cog import CheckCog


async def main():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=config.BOT_PREFIX, intents=intents)

    @bot.listen("on_ready")
    async def on_ready():
        try:
            await bot.tree.sync()
        except Exception as e:
            print(f"Failed to sync commands: {e}")

        print(f"Logged in as {bot.user}")

    await bot.add_cog(CheckCog(bot))
    await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
