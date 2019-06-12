import pandas as pd 

users = pd.read_pickle("./dataset/final_users.pickle")
print(users.header)