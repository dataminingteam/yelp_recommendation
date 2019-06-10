import pandas as pd
from interval import Interval

a = [[0,8],[9,26],[27,80],[81,150],[151,8350]]  # >90, >50, >20, >10, others

def locate(x, a):
    intervals = [Interval(min, max, closed=True) for min, max in a]
    #print(intervals)
    for i, interval in enumerate(intervals):
        if x in interval:
            return i
    return -1

pkl_file = 'dataset/final business.pickle'
data = pd.read_pickle(pkl_file)

for i in range(10):
    x = data.iloc[i,:]['review_count']
    print(x,end = " * ")
    print(locate(x,a))