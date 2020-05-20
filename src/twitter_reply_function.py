import tweepy
import os
import wget
import json
import pandas as pd
from tensorflow.keras.models import load_model
from dotenv import load_dotenv
from tweepy import OAuthHandler, Stream, StreamListener, TweepError
from time import sleep
from random import choice
from src.reply_sentences import *
from src.face_detection import *
from src.dictionarys import emotion_numbers
load_dotenv()


#handling access to twitter
auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"),os.getenv("TWITTER_API_SECRET") )
auth.set_access_token( os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)


sentiment_analysis=load_model(filepath="models/model_complex_with_data_augmentation_rotatation_25degrees.h5",compile=True)    
df_songs=pd.read_csv("output/spotify_songs.csv")


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This class handles all the different responses to a tweet
    """
    def on_data(self, data):
        tweet=json.loads(data)
        tweetid=tweet['id']
        user=tweet["user"]["screen_name"]
        try:
            url=tweet["entities"]["media"][0]["media_url"]
            image=wget.download(url)
            face=face_detection(image)
            if face is not False:
                sentiment=sentiment_analysis.predict_classes(face)[0]
                url_song=choice(df_songs[df_songs.sentiment_code==sentiment]["URL"].values)
                status=choice(status_emotions[sentiment]).format(user=user, url=url_song)
            else:
                status=choice(status_no_face_detected).format(user=user)
            os.remove(image)
        except:
            status =choice(status_no_photo).format(user=user)
            print("This tweet has no picture attached")
        try:
             api.update_status(status=status, in_reply_to_status_id=tweetid)
        except TweepError as error:
            if error.api_code == 187:
                print('duplicate message')
                sleep(10)
            else:
                print(error)
        
        return True

    def on_error(self, status):
        print(status)
        pass