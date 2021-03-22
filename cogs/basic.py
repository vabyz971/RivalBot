from  discord.ext import commands


def setup(bot):
    bot.add_cog(Basic(bot))


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong")
