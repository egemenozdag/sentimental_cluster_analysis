from preprocessing import clean_data
def test_clean_data():
    raw_data = ["This is a good comment! :) ", "Bad comment!!!"]
    cleaned = clean_data(raw_data)
    assert cleaned == ["this is a good comment", "bad comment"]

from model import train_model
def test_train_model():
    mock_data = [[1, 2], [2, 3], [3, 4]]
    model = train_model(mock_data, n_clusters=3)
    assert model.n_clusters == 3

from pipeline import full_pipeline
def test_full_pipeline():
    raw_data = ["I love this product!", "This is terrible."]
    results = full_pipeline(raw_data)
    assert len(results) == 2
    assert "sentiment" in results[0]

test_clean_data()
test_train_model()
test_full_pipeline()
