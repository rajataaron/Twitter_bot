from twython import Twython, TwythonError
# Need to import csv now too!
import csv
import datetime
import time

app_key = "xxxxxxxx"#Your App Key
app_secret = "xxxxxxxxxx"#Your App secret Key
oauth_token = "xxxxxxxx"# Your Oauth Token
oauth_token_secret = "xxxxxxxx"#Your Oauth Token secret key

twitter = Twython(app_key,app_secret,oauth_token,oauth_token_secret)

# This time we want to make several lists!
names = []
usernames = []
ids = []
locations = []
follower_count = []

datestamp = datetime.datetime.now().strftime("%Y-%m-%d")

username = raw_input("Retrieve Follower list of: ")

next_cursor = -1

while(next_cursor):
    get_followers = twitter.get_followers_list(screen_name=username,count=200,cursor=next_cursor)
    for follower in get_followers["users"]:
# And add some more user details to its corresponding list
        names.append(follower["name"].encode("utf-8"))
        usernames.append(follower["screen_name"].encode("utf-8"))
        ids.append(follower["id"])
        locations.append(follower["location"].encode("utf-8"))
        follower_count.append(follower["followers_count"])
        next_cursor = get_followers["next_cursor"]
# Instead of creating a .txt we want to create a .csv!
open_csv = open(username+"-"+datestamp+".csv","wb")
# And write to it...
followers_csv = csv.writer(open_csv)

# Creating our top "title" row
names.insert(0,"@%s has %s followers (%s)" % (str(username),str(len(follower)),str(datestamp)))
usernames.insert(0,"")
ids.insert(0,"")
locations.insert(0,"")
follower_count.insert(0,"")

# Give each column its own title
names.insert(1,"\nDisplay Name\n")
usernames.insert(1,"\nUsername (@)\n")
ids.insert(1,"\nUser ID\n")
locations.insert(1,"\nLocation\n")
follower_count.insert(1,"\n# of their Followers\n")

# Merge all our lists together so that they line up
rows = zip(names,usernames,ids,locations,follower_count)

# Write each row one-by-one to our spreadsheet
for row in rows:
    followers_csv.writerow(row)

#The obligatory first status update to test
for i in names[2:]:
    print i
    twitter.update_status(status=i)
    time.sleep(60)
# Save and close our csv spreadsheet
open_csv.close()
