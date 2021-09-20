import requests
import os
import json
import csv

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

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


## // Collect tweets from the search endpoint //

# How to build a query:
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
# https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule

# Tip: use the "advanced search" to build your query on Twitter website and then apply it here
#      and vice-versa.

# - Core operators: Available when using any Project.
# - Advanced operators: Available when using an Academic Research Project 

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
#                  expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

# Example query:
# '(from:cz_binance)'
# '(from:ethereum -is:retweet -is:reply -is:quote -is:nullcast) OR #ethereum'
# '(ethereum OR ether OR eth) min_faves:1000'
# '(Ethereum OR ether OR eth) (from:aantonop) min_faves:1000 min_replies:10 min_retweets:10 lang:en'
# 'ethereum is:verified -is:retweet lang:en'

search_url = "https://api.twitter.com/2/tweets/search/all"

query_params = {'query': '(ethereum OR ether OR eth) -is:retweet lang:en',
                'tweet.fields': 'author_id,created_at,text,public_metrics',
                'max_results': 10,
                'start_time': '2020-01-01T00:00:00Z', 'end_time': '2021-08-31T00:00:00Z',
                # 'expansions': 'author_id,geo.place_id',    
                # 'user.fields': 'id,name,username,verified',
                # 'place.fields': 'country',
                }


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    meta = json_response["meta"]
    data = json_response["data"]
    
    ## // Store collected tweets in a pickle file //
    import pandas as pd
    
    # pd.DataFrame(json_response['data'])

    from pandas import json_normalize 
    df = json_normalize(json_response, 'data')
    print(df)
    print(df.columns)
    df.to_pickle('data/collected_tweets.pkl')
    df = pd.read_pickle('data/collected_tweets.pkl')

    ## // Store the data in Human readable format (collected_tweets.txt) // 
    # but also store the data in a pickle dataframe ready to be processed using pandas.
    keys = json_response["data"][0].keys()
    print(keys)

    with open('data/collected_tweets.txt', 'a') as outfile:
        for i in range(len(json_response["data"])):
            json.dump(json_response["data"][i], outfile)
            outfile.write('\n')


if __name__ == "__main__":
    main()


##  Pagination

# To get the next page, take the next_token value directly from the response (7140w) and set it as the pagination_token for the next request call.
