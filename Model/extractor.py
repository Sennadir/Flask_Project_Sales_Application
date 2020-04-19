import os
import pandas as pd
import numpy as np
import datetime
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder

import warnings
warnings.filterwarnings("ignore")

features = ['Store', 'DayOfWeek', 'Open', 'Promo', 'StateHoliday_a','StateHoliday_b','StateHoliday_c',
'CompetitionDistance','CompetitionOpenSinceMonth','CompetitionOpenSinceYear','Promo2','Promo2SinceWeek',
           'Promo2SinceYear','Year','Month','Day','Assortment_b','Assortment_c','StoreType_b','StoreType_c',
            'StoreType_d','PromoInterval_Jan,Apr,Jul,Oct','PromoInterval_Mar,Jun,Sept,Dec']

def get_date_promo2(i, store_df):
    '''
    A partir de la variable Promo2SinceWeek et Promo2SinceYear, crée une vraie date
    i : index
    store_df : données par store
    '''
    try: #fonctionne si le magasin participe à Promo2
        year = str(int(store_df.loc[i, 'Promo2SinceYear']))
        week = str(int(store_df.loc[i, 'Promo2SinceWeek']))
        d = year+'-W'+week
    except:
        return np.nan
    return datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")


class FeatureExtractor(object):
    def __init__(self, path_train = './data/train.csv', path_store = './data/store.csv'):
        self.path_train = path_train
        self.path_store = path_store
        return None


    def fit(self):
        self.store_data = pd.read_csv(self.path_store)
        self.train_data = pd.read_csv(self.path_train,  parse_dates=['Date'])
        return None

    def transform(self):
        data = self.train_data
        store_data = self.store_data

        # Merge Train with Store Data
        data.StateHoliday.replace(0,'0', inplace=True)
        data = pd.merge(data, store_data, on="Store")

        data['Average_Sales_by_customer'] = data['Sales']/data['Customers']
        store_data['date_debut_promo2'] = store_data.index.map(lambda x: get_date_promo2(x, store_data))
        data = pd.merge(data, store_data[['Store','date_debut_promo2']], on='Store')

        # Extract Temporal Values
        data['Year'] = data.Date.dt.year
        data['Month'] = data.Date.dt.month
        data['Day'] = data.Date.dt.day

        # Imput the Missing Values
        imputer_competition_year = SimpleImputer(strategy = 'constant', fill_value = 1900)
        imputer_competition_month = SimpleImputer(strategy = 'constant', fill_value = 1)
        data['CompetitionOpenSinceYear'] = imputer_competition_year.fit_transform(np.array(data['CompetitionOpenSinceYear']).reshape(-1,1))
        data['CompetitionOpenSinceMonth'] = imputer_competition_year.fit_transform(np.array(data['CompetitionOpenSinceMonth']).reshape(-1,1))


        # Extract Promo Features
        today = pd.to_datetime(datetime.date.today())
        imputer_promo_year = SimpleImputer(strategy = 'constant', fill_value = today.year)
        imputer_promo_week = SimpleImputer(strategy = 'constant', fill_value = today.week)

        data['Promo2SinceYear'] = imputer_promo_year.fit_transform(np.array(data['Promo2SinceYear']).reshape(-1,1))
        data['Promo2SinceWeek'] = imputer_promo_week.fit_transform(np.array(data['Promo2SinceWeek']).reshape(-1,1))

        distance_max = 2*data['CompetitionDistance'].max()
        imputer_competition_distance = SimpleImputer(strategy = 'constant', fill_value = distance_max)
        data['CompetitionDistance'] = imputer_competition_distance.fit_transform(np.array(data['CompetitionDistance']).reshape(-1,1))

        # Ordinal Encoder for the Store ID
        ord_enc = OrdinalEncoder()
        data.Store = ord_enc.fit_transform(np.array(data.Store).reshape(-1, 1))

        data.StateHoliday.replace(0, '0', inplace=True)

        # Transform Categorical Features
        categorical_features = ['Assortment', 'StoreType', 'PromoInterval', 'StateHoliday']
        data = pd.get_dummies(data, columns = categorical_features, drop_first=True) # drop first to avoid colinearity

        return data[features], data['Sales']
