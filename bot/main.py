import os
from mongoengine import connect
from discord.ext import commands
from settings import *

bot = commands.Bot(command_prefix=BOT_PREFIX)

connect(MONGODB_DATABASE, 
        host=MONGODB_HOST, 
        username=MONGODB_USER, 
        password=MONGODB_PASSWORD,
        authentication_source="admin")




for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(DISCORD_BOT_TOKEN)