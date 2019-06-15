import pandas as pd

dataframe = pd.read_pickle('dataset/users_have_tips.pickle')
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

