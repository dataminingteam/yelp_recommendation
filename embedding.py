from gensim.models import word2vec
import logging
import nltk
from nltk import word_tokenize

import pandas as pd
from interval import Interval

vector_dim = 100
pkl_file = 'dataset/final business.pickle'
nltk.download('punkt')


def locate(x, a):
    intervals = [Interval(min, max, upper_closed=False) for min, max in a]
    for i, interval in enumerate(intervals):
        if x in interval:
            return i
    return -1


def generate_word(data):
    string = str(data['business_id'])
    string += data['cuisine']
    string += str(int(data['stars']))
    string += 'os' + str(0 if data['OutdoorSeating'] == 'FALSE' else 1)
    string += 'bacc' + str(0 if data['BusinessAcceptsCreditCards'] ==
                           'FALSE' else 1)
    string += 'rd' + str(0 if data['RestaurantsDelivery'] == 'FALSE' else 1)
    string += 'rr' + str(0 if data['RestaurantsReservations'] ==
                         'FALSE' else 1)
    string += 'wifi' + str(0 if data['WiFi'] == 'No' else
                           (1 if data['WiFi'] == 'Yes' else 2))
    string += 'alcohol' + str(0 if data['Alcohol'] == 'Full_Bar' else
                              (1 if data['Alcohol'] == 'Beer&Wine' else
                               (2 if data['Alcohol'] == 'No' else 3)))
    return string


class mySentences(object):
    def __init__(self, pkl_file):
        self.dataframe = pd.read_pickle(pkl_file)
        print(self.dataframe.head())

    def __iter__(self):
        for index, line in self.dataframe.iterrows():
            string = generate_word(line)
            if index < 5:
                print(string)
                print(word_tokenize(string))
            yield word_tokenize(string)


sentences = mySentences(pkl_file)
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = word2vec.Word2Vec(
    sentences=sentences,
    sg=1,
    iter=10,
    min_count=0,
    size=vector_dim,
    workers=4)

# print([model.wv.index2word[i] for i in range(50)])
