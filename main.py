
from tweepy import OAuthHandler, Stream
from src.twitter_reply_function import *
from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"),os.getenv("TWITTER_API_SECRET") )
auth.set_access_token( os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))


l = StdOutListener()
stream = Stream(auth, l)
stream.filter(track = ["@whatsup_buddy"])