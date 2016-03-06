#Importing time and random now!
from twython import Twython, TwythonError
import time
import random

app_key = "xxxxxxxxx"#enter your app key
app_secret = "xxxxxxxx"#your app secret
oauth_token = "xxxxxxx"#your oauth token
oauth_token_secret = "xxxxxxxxx"#your oauth token secret key

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#Small list of Tweets to Tweet Below is the example you can as many you want
list = [
    "I think I got u!",
    "Enjoy! every moment with your friends. Because this is a precious moment.",
    "Now I will understand you my friend twitter and rasp!!!"
    ]

#This is called a while loop.
while True:
    try:
        if len(list) > 0:
            toTweet = list[random.randint(0,len(list))-1]
            twitter.update_status(status=toTweet)
            list.remove(toTweet)
            time.sleep(60)
        else:
#Oops! Our twitter.update_status should all be on one line!
            twitter.update_status(status="Oh dear... I'm afraid I'm rather empty =(")
            break
    except TwythonError as e:
        print e
