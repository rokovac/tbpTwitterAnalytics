import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.twitter_db

lista = []

collection = db['twitter2']
for collection in collection.find():
    lista.append(collection)
