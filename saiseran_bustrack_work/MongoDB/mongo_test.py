from mongo_conn import *
from file_parser_mongo import *

c = mongo_db()
datab=db
collection=collection
u = c.mongo_connect(datab,collection)
print(u)