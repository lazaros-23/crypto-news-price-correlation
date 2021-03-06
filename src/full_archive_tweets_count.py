import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/counts/all"

# Optional params: start_time, end_time, since_id, until_id, next_token, granularity
# Vizag gas leak -is:retweet
query_params = {'query': 'Vizag gas leak -is:retweet',
                'granularity': 'day', 
                'start_time': '2020-05-07T00:00:00.000Z', 'end_time': '2020-05-12T00:00:00.000Z'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveTweetCountsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    res = json.dumps(json_response, indent=4, sort_keys=True)
    print(res)
    return res


if __name__ == "__main__":
    res = main()