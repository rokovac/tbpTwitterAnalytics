from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from bson.son import SON
from bson.code import Code

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'twitter_db'
mongo = PyMongo(app, config_prefix='MONGO')

mapping = Code("""function() {
                emit(this.lang, 1)
                }""")

reducing = Code("""function(key, values) {
                return Array.sum(values); }""")

@app.route('/')
def home_page():
    collection_number = mongo.db.twitter_collection.count()
    languages = mongo.db.twitter_collection.map_reduce(mapping, reducing, "twitter")
    languages = svi_jezici.find()
    return render_template('index.html',
        collection_number = collection_number, languages = languages)