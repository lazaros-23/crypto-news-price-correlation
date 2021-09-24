# DOCUMENTATION: https://developer.twitter.com/en/docs/twitter-api/premium/search-api/overview

# 1. Full-archive search
# 2. result_type=popular

import requests
import json

# endpoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json"
endpoint = "https://api.twitter.com/1.1/search/tweets.json"

headers = {"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAALBZTwEAAAAAA%2BevMtTXt57NGHbye95AtJIpcBc%3DwLlZVxOt1ZWgFYUEdCrkiJmwjHG3gw70Macn1HHUxqs61nfrTs", "Content-Type": "application/json"}  

# data = '{"query":"(ethereum OR ether OR eth) lang:en", "fromDate": "201802020000", "toDate": "201802240000", "maxResults":"10"}'
data = '{"query":"(ethereum OR ether OR eth) -is:retweet -is:reply result_type:popular lang:en", "fromDate": "201802020000", "toDate": "201802240000", "maxResults":"10"}'

response = requests.post(endpoint,data=data,headers=headers).json()

print(json.dumps(response, indent = 2))


collected_tweets = response["results"]

for tweet in collected_tweets:
    # Extract relevant files from API response
    id = tweet["id"]
    text = tweet["text"]
    # full_text = tweet["retweeted_status"]["extended_tweet"]["full_text"]
    created_at = tweet["created_at"]
    reply_count = tweet["reply_count"]
    retweet_count = tweet["retweet_count"]
    favorite_count = tweet["favorite_count"]
    user_id = tweet["user"]["id"]
    user_name = tweet["user"]["name"]
    user_screen_name = tweet["user"]["screen_name"]
    user_location = tweet["user"]["location"]
    user_verified = tweet["user"]["verified"]
    user_followers_count = tweet["user"]["followers_count"]

    # Store to csv file
    with open("tweets.csv", "a") as f:
        f.write(str(id) + "," + str(text) + "," + str(created_at) +\
                 "," + str(reply_count) + "," + str(retweet_count) + "," + str(favorite_count)+\
                 "," + str(user_id) + "," + str(user_name) + "," + str(user_screen_name) +\
                 "," + str(user_location) + "," + str(user_verified) + "," + str(user_followers_count) + "\n")

        # +"," + str(full_text) 





#################### DEV ########################
 
# - Get a response from the API
# - Clean up the response
# - Save data to a file

type(response)
len(response)
response.keys()

collected_tweets = response["results"]
response["next"]
response["requestParameters"]

type(collected_tweets)
len(collected_tweets)

tweet = collected_tweets[0]
type(tweet)
len(tweet)
tweet.keys()

for tweet in collected_tweets:
    print(tweet["id"])
    print(tweet["text"])
    print(tweet["retweeted_status"]["extended_tweet"]["full_text"])
    print(tweet["created_at"])
    print(tweet["reply_count"])
    print(tweet["retweet_count"])
    print(tweet["favorite_count"])
    print(tweet["user"]["id"])
    print(tweet["user"]["name"])
    print(tweet["user"]["screen_name"])
    print(tweet["user"]["location"])
    print(tweet["user"]["verified"])
    print(tweet["user"]["followers_count"])
    
    print("\n")
    break