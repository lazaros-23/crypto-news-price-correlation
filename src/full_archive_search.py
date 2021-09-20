import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/all"

# How to build a query:
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
# - Core operators: Available when using any Project.
# - Advanced operators: Available when using an Academic Research Project 

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
#                  expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

query_params = {'query': '(from:ethereum -is:retweet) OR #ethereum',
                'tweet.fields': 'author_id,created_at,text',
                'max_results':100,
                'start_time': '2020-01-01T00:00:00Z', 'start_time': '2020-12-31T00:00:00Z'}


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
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()