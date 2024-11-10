import re

class DataPreprocessor:
    @staticmethod
    def clean_text(text):
        text = re.sub(r'http\S+', '', text)  # URL'leri kaldır
        text = re.sub(r'@\w+', '', text)     # Kullanıcı adlarını kaldır
        text = re.sub(r'#', '', text)        # Hashtag sembolünü kaldır
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Özel karakterleri kaldır
        text = text.lower().strip()  # Küçük harfe çevir ve baştaki/sondaki boşlukları kaldır
        return text

    def preprocess(self, df):
        df['clean_text'] = df['text'].apply(self.clean_text)
        return df
