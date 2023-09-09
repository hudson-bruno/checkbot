import os

from dotenv import load_dotenv

load_dotenv(override=True)

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
BOT_PREFIX = os.getenv("BOT_PREFIX", "$")
