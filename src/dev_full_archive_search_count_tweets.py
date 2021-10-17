import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

## // Count tweets //

# Optional params: start_time, end_time, since_id, until_id, next_token, granularity

search_url = "https://api.twitter.com/2/tweets/counts/all"

# Query:
# - ethereum OR ether OR eth 
query_params = {'query': '(audiusproject OR audius OR $audio OR audiocoin) lang:en -is:retweet -is:reply',
                'granularity': 'day', 
                'start_time': '2020-01-01T00:00:00Z', 'end_time': '2021-08-31T00:00:00Z'}


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
    print(json.dumps(json_response, indent=4, sort_keys=False))

    ## Write the json_response to a csv file
    meta = json_response["meta"]
    data = json_response["data"]

    import pandas as pd
    from pandas import json_normalize 

    df = json_normalize(json_response, 'data')
    print(df)
    df.to_csv('data/total_tweets_ethereum_ether_eth.csv', index=False)
    # df.to_pickle('data/tweets.pkl')
    # df = pd.read_pickle('data/tweets.pkl')
    


if __name__ == "__main__":
    main()