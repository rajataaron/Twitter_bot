import sys
import time
from datetime import datetime
from twython import Twython

class bot:
    def __init__(self, c_key, c_secret, a_token, a_token_secret):
        self.api = Twython(c_key, c_secret, a_token, a_token_secret)
        
        try:
            self.api.verify_credentials()
        except:
            sys.exit("Authentication Failed")
        self.last_ran = datetime.now()

    @staticmethod
    def timestr_to_datetime(timestr):
        timestr = "{0} {0}".format(timestr[:19], datetime.now().year)

        return datetime.strptime(timestr, '%a %b %d %H:%M: %S %Y')

    def retweet_tast(self, screen_name):
        print "Checking for new tweets from @{0}".format(screen_name)
        timeline = self.api.get_user_timeline (screen_name = screen_name)
        for t in timeline:
            tweet_time = bot.timestr_to_datetime(t['created_at'])
            if tweet_time > self.last_run:
                print "Retweeting {0}".format(t['id'])
                self.api.retweet(id = t['id'])

if __name__ == "__main__":
    c_key = "xxxxxxxxxxx"#your C_KEY
    c_secret = "xxxxxxxxxxx"#Your Secret Key
    
    a_token = "xxxxxxxx"#Your Token Authentication
    a_token_secret = "xxxxxxxx"#Your Secret Token
    
    twitter = Twython(c_key, c_secret, a_token, a_token_secret)

    while True:
        print "hey"
        twitter.retweet(id="xxxxxxx")#Twitter id of a person you want to retweet its in the URL
        print "done"
        twitter.last_ran = datetime.now()
        time.sleep(5 )
