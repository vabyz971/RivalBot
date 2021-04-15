from ._global import *
from mongoengine import connect

print("===== PRODUCTION MODE ======")

connect(MONGODB_DATABASE, 
        host=MONGODB_HOST, 
        username=MONGODB_USER, 
        password=MONGODB_PASSWORD,
        authentication_source="admin")
