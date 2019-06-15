import pandas as pd
from interval import Interval

a = [[0,8],[9,26],[27,80],[81,150],[151,8350]]  # >90, >50, >20, >10, others
a = [[6, 13], [14, 22], [23, 39], [40, 88], [89, 13278]]

def locate(x, a):
    intervals = [Interval(min, max, closed=True) for min, max in a]
    #print(intervals)
    for i, interval in enumerate(intervals):
        if x in interval:
            return i
    return -1

pkl_file = 'dataset/final users.pickle'
data = pd.read_pickle(pkl_file)

for i in range(10):
    x = data.iloc[i,:]['review']
    print(x,end = " * ")
    print(locate(x,a))
