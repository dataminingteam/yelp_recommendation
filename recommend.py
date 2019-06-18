from gensim.models import word2vec
import pandas as pd
import word_generate

business_file = 'dataset/final business.pickle'
user_file = 'dataset/users_have_tips.pickle'
#user_file = 'dataset/final users.pickle'

dataframe = pd.read_pickle(user_file)
#print(dataframe.shape[0])
model = word2vec.Word2Vec.load('embedding_616.model')

business_df = pd.read_pickle(business_file)

for i in range(20):
    #print(dataframe[dataframe['user_id'] == 'HbyHhB6WOSQjU-JYwED9Ww'].index.tolist())
    business_word = word_generate.generate_business_word(business_df.iloc[i])
    #print(business_word)
    user_type = word_generate.generate_user_word(dataframe.iloc[i])
    print(user_type[:20])
    user_type = model.wv[user_type]
    result = pd.DataFrame(model.most_similar(positive=[user_type], topn=10))
    print(result)

