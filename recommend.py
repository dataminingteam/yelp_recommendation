from gensim.models import word2vec
import pandas as pd
import word_generate

business_file = 'dataset/final business.pickle'
user_file = 'dataset/final users.pickle'

dataframe = pd.read_pickle(user_file)
model = word2vec.Word2Vec.load('embedding.model')
#print(dataframe[dataframe['user_id'] == '8k3aO-mPeyhbR5HUucA5aA'])
user_type = word_generate.generate_user_word(dataframe.iloc[10000])
print(user_type)
user_type = model.wv[user_type]
print(model.most_similar(positive=[user_type], topn=10))
