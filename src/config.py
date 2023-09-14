import logging
import os

from dotenv import load_dotenv

load_dotenv(override=True)
logging.basicConfig(level="INFO")

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
BOT_PREFIX = os.getenv("BOT_PREFIX", "$")
