
import tweepy
import sys
import pymongo



consumer_key=#CONSUMER KEY
consumer_secret=#CONSUMER SECRET

access_token=#ACCESS TOKEN
access_token_secret=#ACCESS TOKEN SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.db = pymongo.MongoClient().#DB


    def on_status(self, status):
        print status.text , "\n"

        data ={}
        data['text'] = status.text
        data['created_at'] = status.created_at
        data['source'] = status.source
        if location == type(dict):
            longitude = location['coordinates'][0]
            latitude = location['coordinates'][1]
            data['longitude'] = longitude
            data['latitude'] = latitude


       
        print (status.text) 
        print "\n"
      
        self.db.#COLLECTION.insert(data)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=['#SEARCH TERM'])