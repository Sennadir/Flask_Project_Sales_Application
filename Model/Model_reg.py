import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.base import BaseEstimator
from sklearn.externals import joblib

import warnings
warnings.filterwarnings("ignore")

class Regressor(BaseEstimator):
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators= 5)
        return None

    def fit(self, X, y):
        self.model.fit(X, y)
        return None

    def save(self):
        joblib.dump(self.model, "./Model/model_rf.pkl", 0)
        return None

    def predict(self, X):
        predictions = self.model.predict(X)
        return predictions
