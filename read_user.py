import pandas as pd
from datetime import date


dataframe = pd.read_pickle('dataset/users_have_tips.pickle')
today = date(2019,6,16)

## add years
dataframe['years'] =  (today - dataframe['yelping_since']).apply(lambda x:round(x.days/365))

pd.set_option('display.max_columns', None)
'''print(dataframe.head())

print(dataframe.min(),dataframe.max())
print(dataframe.quantile(0.2), dataframe.quantile(0.4), dataframe.quantile(0.6), dataframe.quantile(0.8))

dataframe = pd.read_pickle('dataset/final business.pickle')
print(dataframe.min(),dataframe.max())
print(dataframe.quantile(0.2), dataframe.quantile(0.4), dataframe.quantile(0.6), dataframe.quantile(0.8))
'''
dataframe = dataframe[dataframe['review'] > 8]
print(len(dataframe))
print(dataframe.min(),dataframe.max())
print(dataframe.quantile(0.2), dataframe.quantile(0.4), dataframe.quantile(0.6), dataframe.quantile(0.8))

