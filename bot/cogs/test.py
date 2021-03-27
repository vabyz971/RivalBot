from discord.ext import commands


def setup(bot):
    bot.add_cog(Test(bot))


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="")
    async def ping(self, ctx):
        await ctx.send("Pong")
