import discord
from discord import channel
from discord import message
from discord.ext import commands
from discord.ext.commands.core import command
from utils import notify_user


def setup(bot):
    bot.add_cog(Basic(bot))


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send(f'Utiliser la command !help, ou contacter un administrateur.')


    @commands.command()
    @commands.guild_only()
    async def invitation(self, ctx):
        """ command creation d'une invitation durée 1j """

        link = await ctx.channel.create_invite(max_ags=1)
        await ctx.send(link)

    @commands.command()
    async def alert(self,ctx, member: discord.Member = None):
        """ alert un user en message priver """
        if member is not None:
            message = "** %s ta alerté** je c'est pas pourquoi " % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Utilise @user pour l'alerté")