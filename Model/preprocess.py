import numpy as np
import pandas as pd

import datetime


from sklearn.preprocessing import OneHotEncoder,  FunctionTransformer, OrdinalEncoder

#scaler
from sklearn.preprocessing import StandardScaler

#imputer
from sklearn.impute import SimpleImputer

#column transformer  and pipeline
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline

from sklearn.externals import joblib

features = ['Store', 'DayOfWeek', 'Open', 'Promo', 'StateHoliday_a','StateHoliday_b','StateHoliday_c',
'CompetitionDistance','CompetitionOpenSinceMonth','CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
           'Promo2SinceYear','Year','Month','Day','Assortment_b','Assortment_c','StoreType_b','StoreType_c',
            'StoreType_d','PromoInterval_Jan,Apr,Jul,Oct','PromoInterval_Mar,Jun,Sept,Dec']

class data_preprocessed():
    def __init__(self, path_test): # = './data/test.csv'
        #_ = pd.read_csv(path_test)
        #_ = _[_['Store'] == 1]
        #self.test = pd.read_csv(path_test)
        self.test = pd.read_csv(path_test)
        self.dates = pd.read_csv(path_test)['Date']
        self.store_data = pd.read_csv('./data/store.csv')
        return None

    def processing(self):
        ord_enc = joblib.load('./Model/encoder.pkl')
        test = self.test
        test['Date'] = pd.to_datetime(test['Date'])
        test = pd.merge(test, self.store_data, on = 'Store')
        test['Year'] = test.Date.dt.year
        test['Month'] = test.Date.dt.month
        test['Day'] = test.Date.dt.day

        imputer_competition_year = SimpleImputer(strategy = 'constant', fill_value = 1900)
        imputer_competition_month = SimpleImputer(strategy = 'constant', fill_value = 1)
        test['CompetitionOpenSinceYear'] = imputer_competition_year.fit_transform(np.array(test['CompetitionOpenSinceYear']).reshape(-1,1))
        test['CompetitionOpenSinceMonth'] = imputer_competition_year.fit_transform(np.array(test['CompetitionOpenSinceMonth']).reshape(-1,1))


        today = pd.to_datetime(datetime.date.today())
        imputer_promo_year = SimpleImputer(strategy = 'constant', fill_value = today.year)
        imputer_promo_week = SimpleImputer(strategy = 'constant', fill_value = today.week)

        test['Promo2SinceYear'] = imputer_promo_year.fit_transform(np.array(test['Promo2SinceYear']).reshape(-1,1))
        test['Promo2SinceWeek'] = imputer_promo_week.fit_transform(np.array(test['Promo2SinceWeek']).reshape(-1,1))

        distance_max = 151720
        imputer_competition_distance = SimpleImputer(strategy = 'constant', fill_value = distance_max)
        test['CompetitionDistance'] = imputer_competition_distance.fit_transform(np.array(test['CompetitionDistance']).reshape(-1,1))

        test.Store = ord_enc.transform(np.array(test.Store).reshape(-1, 1))

        test.StateHoliday.replace(0, '0', inplace=True)

        categorical_features = ['Assortment', 'StoreType', 'PromoInterval', 'StateHoliday']
        test = pd.get_dummies(test, columns = categorical_features, drop_first=True)

        test['StateHoliday_b'] = np.zeros(len(test))
        test['StateHoliday_c'] = np.zeros(len(test))

        test.Open.fillna(1, inplace=True)
        X_test = test[features]

        self.data = X_test

        return self.data
