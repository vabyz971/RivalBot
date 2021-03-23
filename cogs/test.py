from discord.ext import commands


def setup(bot):
    bot.add_cog(Test(bot))


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *args):
        await ctx.send(", ".join(args))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")
