from sklearn.feature_extraction.text import TfidfVectorizer

class FeatureExtractor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000)

    def extract_features(self, df):
        return self.vectorizer.fit_transform(df['clean_text']).toarray()
