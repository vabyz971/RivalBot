from ._global import *
from mongoengine import connect

print("===== DEBUG MODE ======")

connect(MONGODB_DATABASE, 
        host=MONGODB_HOST, 
        username=MONGODB_USER, 
        password=MONGODB_PASSWORD,
        authentication_source="admin")


if connect is not None:
    print("connexion a MongoDB reussie")
else:
    print("connexion a MongoDB perdue")

