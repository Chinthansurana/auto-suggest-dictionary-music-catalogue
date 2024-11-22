import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class CollaborativeFilteringModel:
    def __init__(self, user_data):
        self.user_data = user_data
        self.user_similarity = None

    def train(self):
        self.user_similarity = cosine_similarity(self.user_data)

    def predict(self, user_id, prefix, song_catalog):
        similar_users = self.user_similarity[user_id]
        suggestions = []
        for other_user_id in np.argsort(similar_users)[::-1]:
            if self.user_data[other_user_id, prefix] > 0:
                suggestions.append(song_catalog[other_user_id])
        return suggestions
