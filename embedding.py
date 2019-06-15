from gensim.models import word2vec
import logging
import nltk
from nltk import word_tokenize

import pandas as pd

import word_generate

vector_dim = 100
business_file = 'dataset/final business.pickle'
user_file = 'dataset/users_have_tips.pickle'
nltk.download('punkt')


class mySentences(object):
    def __init__(self, business_file, user_file):
        self.dataframe = []
        self.dataframe.append(pd.read_pickle(business_file))
        self.dataframe.append(pd.read_pickle(user_file))
        self.dataframe[1] = self.dataframe[1][self.dataframe[1]['review'] > 8]
        self.sentences = []
        self.user_embedding = []
        self.business_embedding = []
        # 生成business的字符串
        str1 = []
        for index, line in self.dataframe[0].iterrows():
            str1.append(word_generate.generate_business_word(line))
            self.business_embedding.append(word_generate.generate_business_word(line))
        print(len(str1))
        # print(str1[0])

        # 生成user的字符串
        str2 = []
        for index, line in self.dataframe[1].iterrows():
            self.user_embedding.append(word_generate.generate_user_word(line))
            str2.append(word_generate.generate_user_word(line))
        print(len(str2))
        # print(str2[0])
        # 交叉合并两个字符串数组，保证embedding在一个向量空间
        for i in range(max(len(str1), len(str2))):
            if str1:
                self.sentences.append(str1.pop())
            if str2:
                self.sentences.append(str2.pop())
        print(len(self.sentences))

        # print(self.sentences[0], self.sentences[1], self.sentences[2], self.sentences[3])

    def __iter__(self):
        for string in self.sentences:
            yield word_tokenize(string)


sentences = mySentences(business_file, user_file)
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = word2vec.Word2Vec(
    sentences=sentences,
    sg=1,
    iter=10,
    min_count=0,
    size=vector_dim,
    workers=4)

#model.save('embedding_final.model')

'''只针对用户特征进行embedding，获得特征矩阵'''
# user_embedding = sentences.user_embedding
# print(user_embedding[:5])