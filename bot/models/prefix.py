from os import remove
from mongoengine import Document, DecimalField, StringField
from mongoengine.errors import NotUniqueError


class PrefixServer(Document):
    id_guild = DecimalField(min_value=1, unique=True, Required=True)
    prefix = StringField(max_length=5)


def addPrefix(g: int, pre: str):
    try:
        newPre = PrefixServer(id_guild=g, prefix=pre)
        newPre.save()
    except NotUniqueError as e:
        print("Le serveur a déjâ un prefix ")


def getPrefix(g: int):
    for serveur in PrefixServer.objects(id_guild=g):
        return serveur.prefix

def updatePrefix(g: int, pre: str):
    updatePre = PrefixServer.objects(id_guild=g)
    updatePre.update(prefix= pre)

def removePrefix(g:int):
    removePre = PrefixServer.objects(id_guild=g)
    removePre.remove()