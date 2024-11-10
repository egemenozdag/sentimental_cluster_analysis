import torch
from transformers import BertForSequenceClassification, BertTokenizer

class ModelTrainer:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
        self.model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        outputs = self.model(**inputs)
        return torch.argmax(outputs.logits, dim=1).item()
