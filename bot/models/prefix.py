from mongoengine import DynamicDocument, DecimalField, StringField


class PrefixConfigServer(DynamicDocument):
    id_guild = DecimalField()
    prefix = StringField()


class Prefix():

    def __init__(self):
        self.prefix = PrefixConfigServer

    def add_prefix(self, g: int, pre: str):
        print("Add Prefix serveur:", g)
        obj = self.prefix.objects(id_guild=g, prefix=pre)
        obj.save()

    def update_prefix(self, g: int, pre: str):
        print("Update serveur:", g, "Prefix", pre)
        self.prefix.update(id_guild=g, prefix=pre)

    def get_prefix(self, g):
        if self.prefix.object(id_guild=g):
            return self.prefix.id_guild
