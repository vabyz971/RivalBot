import random

from discord.ext import commands


def setup(bot):
    bot.add_cog(Gamble(bot))


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Donne un nombre entre 1 et 100")
    async def roll(self,ctx):
        n= random.randrange(1,101)
        await ctx.send(n)
