from pymongo import MongoClient
import json
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import io

# Twitter podaci
ckey = '6MKsa5bWRW8FLyDs8UCmn8hNX'
consumer_secret = 'uZHxNEfK1cymh6XrmguwNzvjsUzTXT6ZFyMq0RJePeMNZFIPpR'
access_token_key = '2839762967-kGbvANeMdVQWaEljInfck6kHPOoRKqfGsIrVl4J'
access_token_secret = 'eb8TzDXtWfHYKdPh8kHNXseuiIjJjB51bBfLRsD6Kdqnq'


start_time = time.time() #grabs the system time
keyword_list = raw_input("Insert keyword: ")
keyword_list = keyword_list.split()
 
class listener(StreamListener):
 
    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit
 
    def on_data(self, data): 
        while (time.time() - self.time) < self.limit:
            
            try:
                client = MongoClient('localhost', 27017)
                db = client['twitter_db']
                collection = db['twitter_collection']
                tweet = json.loads(data)
                collection.insert(tweet)
                return True
            
            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                pass
            exit()
 
    def on_error(self, status):
        print statuses

auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)

twitterStream = Stream(auth, listener(start_time, time_limit=60)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list)  #call the filter method to run the Stream Object
