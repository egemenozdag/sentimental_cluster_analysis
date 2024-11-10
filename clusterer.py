from sklearn.cluster import KMeans

class Clusterer:
    def __init__(self, n_clusters=3):
        self.model = KMeans(n_clusters=n_clusters)

    def cluster_data(self, features):
        return self.model.fit_predict(features)
