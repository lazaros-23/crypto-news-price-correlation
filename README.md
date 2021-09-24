# Crypto News-Price correlation

Proof of Concept Project for the Crypto News-Price correlation.

**Project Management Document:** <https://docs.google.com/document/d/19MJ_T_3Y7oA5kcOyW95NghsbLv40C-d5ZKfetxn8OtY/edit#>

## Project timeline

1. 6/9/2021 - Initial commit
2. 19/9/2021 - Added correlation plot
3. 28/9/2021 - Final commit

## Bitcoin
Official website: https://bitcoin.org/el/

<img src="https://github.com/lazaros-23/crypto-news-price-correlation/blob/main/assets/btc_logo.png" width="200" height="200" />

## Ethereum

Official website: <https://ethereum.org/en/>
<img src="https://github.com/lazaros-23/crypto-news-price-correlation/blob/main/assets/ethereum_logo.png" width="200" height="100" />

## Python libraries

* [numpy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [matplotlib](https://matplotlib.org/)
* [seaborn](https://seaborn.pydata.org/)
* [pytest](https://docs.pytest.org/)
* [tweepy](https://docs.tweepy.org/en/latest/index.html)
* [vaderSentiment](https://pypi.org/project/vaderSentiment/)

## Requirements

1. Get price feed for Crypto Avalanche AVAX
<https://docs.chain.link/docs/historical-price-data/?_ga=2.56010543.584813608.1630464090-795458070.1630464090>

2. Twitter Account:
<https://twitter.com/avalancheavax?s=11>

3. Web scrapping - News site
<https://cryptopanic.com/news/avalanche-2/>

## About Avalance

`Avalance` (AVAX) coin: <https://coinmarketcap.com/el/currencies/avalanche/>

Avalanche Foundation Announces $180M DeFi Incentive Program
<https://medium.com/avalancheavax/avalanche-foundation-announces-180m-defi-incentive-program-d320fdfafff7>

**Data sources:**

1. Crypto prices (Binance API)
2. Crpyto News (Twitter API)

## Resources

1. https://lunarcrush.com/
2. https://santiment.net/
3. https://bitinfocharts.com/comparison/tweets-eth.html#3y

## Tweets (Twitter API)

Twitter Dev: https://github.com/twitterdev
Documentation: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
Postman: https://documenter.getpostman.com/view/9956214/T1LMiT5U

* Sentiment analysis of collected tweets
* Tweet Volume
* Google trends

Query

* Tweet has the words or hastags: ethereum, ether, eth
* Tweet language english
* more than faves:100 (I can't search based on number of favorites in Twitter API v2)
* limit:10-500 (Pagination needed)

author_id, created_at, text, public_metrics (like_count, quote_count, reply_count, retweet_count), has_link, has_media, hyperlink

**Problem**
Twitter API v2 can't search based on number of favorites, retweets.

TODO
 
* Total tweets per hour.

Tweet query

1. Get twitter API data
2. Sentiment Analysis
