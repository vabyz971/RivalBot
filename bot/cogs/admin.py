from discord.ext import commands
from models.prefix import Prefix

import discord
import datetime


def setup(bot):
    bot.add_cog(Admin(bot))


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="[ADMIN] Charger une command(cogs.command)")
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        """ Charger une commande """
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Impossible de charger la commande")
            return
        await ctx.send("Commande charger")

    @commands.command(brief="[ADMIN] Recharger un command(cogs.command)")
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        """ Reharger une commande """
        try:
            self.bot.unload_extension(cog)
            self.bot.reload_extension(cog)
        except Exception as e:
            await ctx.send("Impossible de recharger la commande")
            return
        await ctx.send("Commande recharger")

    @commands.command(brief="[ADMIN] décharge un command(cogs.command)")
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        """ Décharger une commande """
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Impossible de décharger la commande")
            return
        await ctx.send("Commande décharger")

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx):
        """ [ADMIN] Information sur le serveur """

        guild = ctx.guild

        nb_voice_channels = len(guild.voice_channels)
        nb_text_channels = len(guild.text_channels)

        embed = discord.Embed(
            description="Information du serveur", colour=discord.Colour.dark_red())
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="# Channel vocal", value=nb_voice_channels)
        embed.add_field(name="# Channel textuel", value=nb_text_channels)
        embed.set_author(name=self.bot.user.name)
        embed.set_footer(text=datetime.datetime.now())

        await ctx.send(embed=embed)

    @commands.command(brief="[ADMIN] Changer le prefix du bot")
    @commands.is_owner()
    async def prefix(self, ctx, prefix):
        Prefix.update_prefix(ctx.guild.id, prefix)
        await ctx.send("Prefix ajouter")