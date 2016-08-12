import pymongo
from pymongo import MongoClient
from operator import itemgetter

client = MongoClient()
db = client.twitter_db

lista = []

filtriranaLista = []

collection = db['twitter2']
for collection in collection.find():
    lista.append(collection)

newlist = sorted(lista, key=itemgetter('value'), reverse=True)

for a in newlist:
    key = []
    value = []
    key.append(str(a['_id']))
    value.append(int(a['value']))
    key.extend(value)
    filtriranaLista.append(key)
    print key
