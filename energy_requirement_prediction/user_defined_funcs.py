import pandas as pd

def load_data():
    raw_df = pd.read_csv('power_data.csv')
    raw_df = raw_df.drop('Unnamed: 0', axis=1)

    return raw_df

def set_index(df):
    df1 = df.set_index('Datetime')
    df1.index = pd.to_datetime(df1.index)

    return df1

def create_features(df):
    df = df.copy()
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.day_of_week
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.day_of_year

    return df

def train_test_split(df):
    train = df.loc[df.index < '01-01-2017']
    test = df.loc[df.index >= '01-01-2017']

    return train, test
