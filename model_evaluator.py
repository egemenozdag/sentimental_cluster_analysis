from sklearn.metrics import classification_report

class ModelEvaluator:
    @staticmethod
    def evaluate_model(y_true, y_pred):
        """Modelin performansını değerlendirir."""
        print(classification_report(y_true, y_pred))
