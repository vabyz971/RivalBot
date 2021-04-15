import discord
from discord.ext import commands
from models.prefix import addPrefix, removePrefix


def setup(bot):
    bot.add_cog(activities(bot))


class activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # Activity Bot
        activity = discord.Activity()
        activity.type = discord.ActivityType.watching
        activity.name = "les actualités"
        await self.bot.change_presence(activity=activity)

        for guild in self.bot.guilds:
            print(guild.name, ":Nombre User:", guild.member_count)

    @commands.Cog.listener()
    async def on_guild_join(self, ctx):
        addPrefix(ctx.guild.id, "!")
        print("Préfix ! crée pour le serveur:", ctx.guild.name)

    @commands.Cog.listener()
    async def on_guild_remove(self, ctx):
        removePrefix(ctx.guild.id)
        print("Supprétion des donnée lier au serveur")
