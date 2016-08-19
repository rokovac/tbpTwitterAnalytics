from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from bson.son import SON
from bson.code import Code
from operator import itemgetter

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'twitter_db'
mongo = PyMongo(app, config_prefix='MONGO')

def funkcija():
    lista = []
    filtriranaLista = []
    header_strings = ['Jezik', 'Broj pojavljivanja']

    mapping = Code("""function() {
                emit(this.lang, 1)
                }""")

    reducing = Code("""function(key, values) {
                return Array.sum(values); }""")
    
    collection_number = mongo.db.twitter_collection.count()
    languages = mongo.db.twitter_collection.map_reduce(mapping, reducing, "twitter2")
    
    languages_popis = mongo.db.twitter2
    for collection in languages_popis.find():
        lista.append(collection)
        
    newlist = sorted(lista, key=itemgetter('value'), reverse=True)
    for a in newlist:
        key = []
        value = []   
        key.append(str(a['_id']))
        value.append(int(a['value']))
        key.extend(value)
        filtriranaLista.append(key)
    filtriranaLista = [header_strings] + filtriranaLista

    return filtriranaLista


@app.route('/')
def home_page():
    collection_number = mongo.db.twitter_collection.count()
    languages = funkcija()
    return render_template('index.html',
                           collection_number = collection_number,
                           languages = languages)

@app.route('/geo')
def geo():
    filtriranaLista2 = funkcija()
    return render_template('geo.html', geo = filtriranaLista2)

