import tweepy
import pandas as pd
import time

class DataCollector:
    def __init__(self, bearer_token):
        self.client = tweepy.Client(bearer_token=bearer_token)

    def fetch_tweets(self, query, max_tweets=100, wait_time=15):
        tweets = []
        try:
            for tweet in tweepy.Paginator(self.client.search_recent_tweets, query=query, max_results=100).flatten(limit=max_tweets):
                tweets.append(tweet.text)
                if len(tweets) % 100 == 0:  # API'nin sınırlarına yaklaşırken kısa bir bekleme süresi ekle
                    print(f"Fetched {len(tweets)} tweets, sleeping for {wait_time} seconds...")
                    time.sleep(wait_time)  # Bekleme süresi ekleniyor
            return pd.DataFrame(tweets, columns=['text'])
        except tweepy.errors.TooManyRequests:
            print("API request limit reached. Retrying in 15 minutes...")
            time.sleep(15 * 60)  # 15 dakika bekleyip tekrar deneyin
            return self.fetch_tweets(query, max_tweets, wait_time)
