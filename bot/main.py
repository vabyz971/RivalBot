import os
import settings

from utils import get_prefix
from discord.ext import commands


client = commands.Bot(command_prefix=get_prefix)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(settings.DISCORD_BOT_TOKEN)
