#测试twitter_scraper库
from twitter_scraper import get_tweets
for tweet in get_tweets('twitter', pages=1):
    print(tweet['text'])