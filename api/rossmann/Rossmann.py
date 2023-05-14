import pandas as pd
import numpy as np

import pickle
import inflection
import math
import datetime


class Rossmann(object):
    def __init__(self):
        self.home_path = '/Users/gtvmi/OneDrive/Documentos/Repos/projeto_portifplio_hossmann_bot/'
        self.competition_distance_scaler   = pickle.load(open(self.home_path + 'parameter/competition_distance_scaler.plk', 'rb'))
        self.competition_time_month_scaler = pickle.load(open(self.home_path + 'parameter/competition_time_month_scaler.plk', 'rb'))
        self.promo_time_week_scaler        = pickle.load(open(self.home_path + 'parameter/promo_time_week_scaler.plk', 'rb'))
        self.year_scaler                   = pickle.load(open(self.home_path + 'parameter/year_scaler.plk', 'rb'))
        self.store_type_scaler             = pickle.load(open(self.home_path + 'parameter/store_type_scaler.plk', 'rb'))

    def data_cleaning(self, data):
        ## Rename Columns ##
        
        # Collect the columns name in a list, transfor in lower case and rename columns
        old_columns = list(data.columns)

        snekecase = lambda x: inflection.underscore(x)

        new_columns = list(map(snekecase, old_columns))
        data.columns = new_columns
        
        ## Charge Date Type ##
        data['date'] = pd.to_datetime(data['date'])
        
        ## Fillout NA ##
        
        # Competition Distance
        data['competition_distance'] = data['competition_distance'].apply(lambda x: 0 if math.isnan(x) else x)

        # Competition Open Since Month
        data['competition_open_since_month'] = data.apply(lambda x: x['date'].month if math.isnan(x['competition_open_since_month'])
                                                                                  else x['competition_open_since_month'], axis=1)

        # Competition Open Since Year
        data['competition_open_since_year'] = data.apply(lambda x: x['date'].year if math.isnan(x['competition_open_since_year'])
                                                                                 else x['competition_open_since_year'], axis=1)

        # Promo2 Since Week
        data['promo2_since_week'] = data.apply(lambda x: x['date'].week if math.isnan(x['promo2_since_week'])
                                                                      else x['promo2_since_week'], axis=1)

        # promo2_since_year
        data['promo2_since_year'] = data.apply(lambda x: x['date'].year if math.isnan(x['promo2_since_year'])
                                                                      else x['promo2_since_year'], axis=1)

        # promo_interval
        month_map = {1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 5: 'May', 6 : 'Jun',
                     7 : 'Jul', 8 : 'Aug', 9 : 'Sept', 10 : 'Oct', 11 : 'Nov', 12 : 'Dec'}
        data['promo_interval'] = data['promo_interval'].apply(lambda x: 0 if pd.isna(x) else x)
        data['month_map'] = data['date'].dt.month.map(month_map)
        data['is_promo'] = data[['promo_interval', 'month_map']].apply(lambda x: 0 if x['promo_interval'] == 0 else
                                                                                 1 if x['month_map'] in x['promo_interval'].split(',') else
                                                                                 0, axis=1)
        
        ## Change Types ##

        data['competition_open_since_month'] = data['competition_open_since_month'].astype(np.int64)
        data['competition_open_since_year'] = data['competition_open_since_year'].astype(np.int64)
        data['promo2_since_week'] = data['promo2_since_week'].astype(np.int64)
        data['promo2_since_year'] = data['promo2_since_year'].astype(np.int64)
        
        return data
    
    def feature_engineering(self, data):
        ## Featuring Engineering ##
        
        # year
        data['year'] = data['date'].dt.year

        # month
        data['month'] = data['date'].dt.month

        # day
        data['day'] = data['date'].dt.day

        # week of year
        data['week_of_year'] = data['date'].dt.isocalendar().week

        # year week
        data['year_week'] = data['date'].dt.strftime('%W-%Y')

        # competition since
        data['competition_since'] = data.apply(lambda x: datetime.datetime(year  = x['competition_open_since_year'],
                                                                           month = x['competition_open_since_month'],
                                                                           day=1), axis=1)

        # competition_time_month
        data['competition_time_month'] = ( ( data['date'] - data['competition_since'] ) /30 ).apply(lambda x: x.days).astype( int )
        data['competition_time_month'] = data['competition_time_month'].apply(lambda x: 0 if x < 0 else x)

        # promo since
        data['promo_since'] = data['promo2_since_year'].astype(str) + "-" + data['promo2_since_week'].astype(str)
        data['promo_since'] = data['promo_since'].apply(lambda x: datetime.datetime.strptime(x + '-1', "%Y-%W-%w") - datetime.timedelta(days=7))

        # promo_time_week
        data['promo_time_week'] = ((data['date'] - data['promo_since'])/7).apply(lambda x: x.days).astype(int)

        # assortment
        # Assortment - describes an assortment level: a = basic, b = extra, c = extended
        data['assortment'] = data['assortment'].apply(lambda x: 'basic' if x == 'a' else
                                                                'extra' if x =='b' else
                                                                'extended')

        # state holiday
        # StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, 
        # are closed on state holidays. Note that all schools are closed on public holidays and 
        # weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
        data['state_holiday'] = data['state_holiday'].apply(lambda x: 'public_holiday' if x == 'a' else
                                                                      'easter_holiday' if x == 'b' else
                                                                      'christmas' if x == 'c' else 'regular_day')
        
        ## Charge Types ##
        
        data['week_of_year'] = data['week_of_year'].astype(np.int64)
        data['competition_time_month'] = data['competition_time_month'].astype(np.int64)
        data['promo_since'] = data['promo_since'].astype(np.int64)
        data['promo_time_week'] = data['promo_time_week'].astype(np.int64)
        
        ## Columns Selection ##
        
        # Rows select

        data = data[data['open'] != 0]

        # Columns Drop

        data.columns

        columns_drop = ['open', 'promo_interval', 'month_map']
        data.drop(columns_drop, axis=1)
        
        return data
    
    def data_preparation(self, data):
        ## Data Preparation ##
        
        # Rescaling ##
        
        # Competition_Distance
        data['competition_distance'] = self.competition_distance_scaler.fit_transform( data[['competition_distance']].values )

        # Competition_time_month
        data['competition_time_month'] = self.competition_time_month_scaler.fit_transform( data[['competition_time_month']].values )
        
        # Promo_time_week
        data['promo_time_week'] = self.promo_time_week_scaler.fit_transform(data[['promo_time_week']].values)
        
        # year
        data['year'] = self.year_scaler.fit_transform(data[['year']].values)
        
        ## Transformation ##
        
        # Encoding

        # State Holiday - One hot Encoding
        data = pd.get_dummies(data, prefix=['state_holiday'], columns=['state_holiday'])

        # Store Type - Label Encoding
        data['store_type'] = self.store_type_scaler.fit_transform(data['store_type'])

        # Assortment - Ordinal Encoding
        assortment_dict = {'basic':1, 'extra':2, 'extended':3}
        data['assortment'] = data['assortment'].map(assortment_dict)

        ## Nature Transformation ##

        # Day of Week
        data['day_of_week_sin'] = data['day_of_week'].apply(lambda x: np.sin( x * ( 2. * np.pi/7 ) ) )
        data['day_of_week_cos'] = data['day_of_week'].apply(lambda x: np.cos( x * ( 2. * np.pi/7 ) ) )

        # month - Transformação Ciclica
        data['month_sin'] = data['month'].apply( lambda x: np.sin ( x * ( 2.*np.pi/12 ) ) )
        data['month_cos'] = data['month'].apply( lambda x: np.cos ( x * ( 2.*np.pi/12 ) ) )

        # day

        data['day_sin'] = data['day'].apply( lambda x: np.sin ( x * ( 2.*np.pi/30 ) ) )
        data['day_cos'] = data['day'].apply( lambda x: np.cos ( x * ( 2.*np.pi/30 ) ) )

        # week of year
        data['week_of_year_sin'] = data['week_of_year'].apply(lambda x: np.sin( x * ( 2. * np.pi/52 ) ) )
        data['week_of_year_cos'] = data['week_of_year'].apply(lambda x: np.cos( x * ( 2. * np.pi/52 ) ) )
        
        cols_selected = ['store',
                         'promo',
                         'store_type',
                         'assortment',
                         'competition_distance',
                         'competition_open_since_month',
                         'competition_open_since_year',
                         'promo2',
                         'promo2_since_week',
                         'promo2_since_year',
                         'competition_time_month',
                         'promo_time_week',
                         'month_sin',
                         'month_cos',
                         'day_of_week_sin',
                         'day_of_week_cos',
                         'day_sin',
                         'day_cos',
                         'week_of_year_sin',
                         'week_of_year_cos']
        return data[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        # prediction
        pred = model.predict( test_data )
        
        # join pred into the original data
        original_data['prediction'] = np.expm1(pred)
        
        return original_data.to_json(orient='records', date_format='iso')
        