# Importing the module
from twython import Twython

#Setting these as variables will make them easier for future edits
app_key = "xxxxxxx"# your app key
app_secret = "xxxxxxx "#your app secret key
oauth_token = "xxxxxxxxx"#your Oauth token
oauth_token_secret = "xxxxxxxxx"#your oauth token secret key

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break

#The obligatory first status update to test
twitter.update_status(status="I did it now I can play with my bot.")
