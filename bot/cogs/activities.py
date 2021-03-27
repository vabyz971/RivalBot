import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(activities(bot))


class activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Activity(name="!help",type = discord.ActivityType.playing)
        await self.bot.change_presence(activity=activity)

