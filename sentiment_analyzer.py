from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.model = pipeline('sentiment-analysis')

    def analyze_sentiments(self, df):
        df['sentiment'] = df['clean_text'].apply(lambda x: self.model(x)[0]['label'])
        return df
