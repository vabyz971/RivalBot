from discord.ext import commands
from models.prefix import getPrefix


async def notify_user(member, message):
    """ envoie un msg en mp """
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)


def mods_or_owner():
    """ Vérification du role de l'utilisateur """
    def predicate(ctx):
        return commands.check_any(
            commands.is_owner(),
            commands.has_role("Moderateur")
        )
    return commands.check(predicate)


def get_prefix(client, message):
    return getPrefix(message.guild.id)
