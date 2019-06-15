"""
process tip data 
find more information
"""
import json
import pandas as pd

frames_tip = []
for chunk in pd.read_json(open("dataset/tip.json", "r", encoding="utf-8"),lines=True, chunksize=10000):
    frames_tip.append(chunk)

tip = pd.concat(frames_tip)
 
user_list = []
nearest_history_list = []
for name, group in tip.groupby(tip['user_id']):
    if len(group) > 10:   # choose user who have more than 10 tips
        user_list.append(name)  ## user name
        '''extract user tip history'''
        group = group.sort_values(by="date" , ascending=False).reset_index(drop=True)
        group = group.drop_duplicates(subset=['business_id'],keep='first',inplace=False)
        # extract the top 20 records
        if group.shape[0] <= 10:
            nearest_history = group.iloc[:group.shape[0],:]
        else:
            nearest_history = group.iloc[:20,:]

        nearest_history_list.append(''.join(list(nearest_history['business_id'])))
print(len(user_list))
users_have_tips = pd.DataFrame({'user_id':user_list, 'history':nearest_history_list})

user_file = 'dataset/final users.pickle'
users_df = pd.read_pickle(user_file)
print(users_df.shape[0])

processed_users_df = pd.merge(users_df, users_have_tips, how = 'inner') #users_df[users_df.user_id.isin(user_list)]
print(processed_users_df.shape[0])
processed_users_df.to_pickle("dataset/users_have_tips.pickle")