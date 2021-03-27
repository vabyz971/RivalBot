from discord.ext import commands

import discord

from utils import mods_or_owner, notify_user

def setup(bot):
    bot.add_cog(Moderator(bot))


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="[MODO] Virée quelqu'un")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @mods_or_owner()
    async def kick(self, ctx, member:discord.Member = None, reaseon: str ="Because"):
        """ Commande Kick """

        if member is not None:
            await ctx.guild.kick(member, reaseon=reaseon)
            await notify_user(member, reaseon)
        else:
            await ctx.send("Mentioner l'utilisateur a kick")


    @commands.command(brief="[MODO] Bannir quelqu'un ")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @mods_or_owner()
    async def ban(self, ctx, member:discord.Member = None, reaseon: str ="Ben tu a fait chier quelqu'un qui a fait chier un des modérateurs Mec"):
        """ Commande ban """

        if member is not None:
            await ctx.guild.ban(member, reaseon=reaseon)
            await notify_user(member, reaseon)
        else:
            await ctx.send("Mentioner l'utilisateur a kick")


    @commands.command(brief="[MODO] déban quelqu'un ")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @mods_or_owner()
    async def unban(self, ctx, member:str = "", reaseon: str ="Because"):
        """ Commande unban """

        if member == "":
            await ctx.send("Écrie le pseudo a déban ")
            return
        
        bans = await ctx.guild.bans()
        for b in bans:
            if b.user.name == member:
                await ctx.guild.unban(b.user, reaseon=reaseon)
                await ctx.send(f"{member.user.name} a été déban")
                await notify_user(b.user, reaseon)
                return
        await ctx.send("Le gars est pas dans la list des banni.")