class SentimentClusterTester:
    def __init__(self, sentiment_analyzer, clusterer):
        self.sentiment_analyzer = sentiment_analyzer
        self.clusterer = clusterer

    def test(self, text):
        sentiment = self.sentiment_analyzer.model(text)[0]['label']
        print(f"Sentiment: {sentiment}")
        # Kümeleme için dummy özellikler kullanabiliriz.
        return sentiment
