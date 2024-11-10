from data_collector import DataCollector
from data_preprocessor import DataPreprocessor
from sentiment_analyzer import SentimentAnalyzer
from feature_extractor import FeatureExtractor
from clusterer import Clusterer
from sentiment_cluster_tester import SentimentClusterTester


if __name__ == "__main__":
    # Veri toplama
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMeGwwEAAAAAU%2Blw5qWkEw0vy%2BAS7%2BDwvRITtn0%3DYELXSi9Sd0g98FmUpxguHuv3FeTfkS1jV1mQQBkjmCEgFsOQzt'
    collector = DataCollector(bearer_token=bearer_token)
    raw_data = collector.fetch_tweets("AI", max_tweets=200)

    # Veri temizleme
    preprocessor = DataPreprocessor()
    clean_data = preprocessor.preprocess(raw_data)

    # Duygu analizi
    analyzer = SentimentAnalyzer()
    sentiment_data = analyzer.analyze_sentiments(clean_data)

    # Özellik çıkarımı ve kümeleme
    extractor = FeatureExtractor()
    features = extractor.extract_features(sentiment_data)

    clusterer = Clusterer()
    sentiment_data['cluster'] = clusterer.cluster_data(features)

    # Sonuçları görüntüle
    print(sentiment_data[['clean_text', 'sentiment', 'cluster']].head())
