import requests
import os
import json
import csv

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


## // Collect tweets from the search endpoint //

# How to build a query:
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query

# Tip: use the "advanced search" to build your query on Twitter website and then apply it here
#      and vice-versa.

# - Core operators: Available when using any Project.
# - Advanced operators: Available when using an Academic Research Project 

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
#                  expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

# Example query:
# '(from:ethereum -is:retweet) OR #ethereum'
# '(ethereum OR ether OR eth) min_faves:1000'
# (Ethereum OR ether OR eth) (from:aantonop) min_faves:1000 min_replies:10 min_retweets:10 lang:en
search_url = "https://api.twitter.com/2/tweets/search/all"

query_params = {'query': 'from:cz_binance',
                'tweet.fields': 'author_id,created_at,text',
                'max_results':10,
                'start_time': '2020-01-01T00:00:00Z', 'end_time': '2020-12-31T00:00:00Z'
                }


## // Count tweets //

# Optional params: start_time, end_time, since_id, until_id, next_token, granularity

search_url = "https://api.twitter.com/2/tweets/counts/all"

query_params = {'query': 'from:cz_binance',
                'granularity': 'day', 
                'start_time': '2020-01-01T00:00:00Z', 'start_time': '2020-01-10T00:00:00Z'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))

    ## Write the json_response to a csv file

    # json_response["meta"]
    # json_response["data"]
    
    # Store the data in Human readable format (tweets.txt)
    # but also store the data in a pickle dataframe ready to be processed using pandas.
    keys = json_response["data"][0].keys()

    with open('data/tweets.txt', 'a') as outfile:
        for i in range(len(json_response["data"])):
            json.dump(json_response["data"][i], outfile)
            outfile.write('\n')

    f = open("data/tweets.txt", "r")
    print(f.readlines())

    from pandas import json_normalize 

    df = json_normalize(json_response, 'data')
    print(df)
    df.to_pickle('data/tweets.pkl')
    df = pd.read_pickle('data/tweets.pkl')

    
    

    import pandas as pd
    dataframe = pd.read_csv('data/tweets.csv')
    dataframe

    list_of_dictionaries = dataframe.to_dict('records')
    dataframe.to_csv('data/tweets.csv', index=False)


if __name__ == "__main__":
    main()