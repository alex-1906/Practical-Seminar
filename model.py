import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import process
import itertools


movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
ratings.drop(columns='timestamp',inplace=True)
movie_ratings = pd.merge(ratings,movies,on='movieId')
movie_ratings_user = movie_ratings.pivot_table(index='userId',columns='title',values='rating')


#load datasets and transform it into sparse matrix
movies_ = 'movies.csv'
ratings_ = 'ratings.csv'

df_movies =pd.read_csv(movies_, usecols =['movieId','title'],dtype={'movieId':'int32','title':'str'})
df_ratings =pd.read_csv(ratings_, usecols =['userId','movieId','rating'],dtype={'userId':'int32','movieId':'int32','rating':'float32'})

movies_users = df_ratings.pivot(index='movieId',columns='userId',values='rating').fillna(0)
matrix_movies_users = csr_matrix(movies_users)

#instantiate model
knn = NearestNeighbors(metric='cosine',algorithm='brute')

#method for recommendations
def recommender(movie,data,model,n_recommendations):
    model.fit(data)
    idx = process.extractOne(movie,df_movies['title'])
    print('Movie selected: ',idx[0],',','Index: ',idx[2])
    distances,indices = model.kneighbors(data[idx[2]],n_neighbors=n_recommendations)
    indices = np.delete(indices,0)
    related_movies = []
    for i in indices:
        related_movies.append(df_movies['title'][i])
    return related_movies


def get_recommendations(userId,best_movies):


    recommendations = []
    for i in best_movies:
        print(recommender(i, matrix_movies_users, knn, 4))
        print()
        recommendations.append(recommender(i, matrix_movies_users, knn, 4))

    recommendations = list(itertools.chain(*recommendations))

    return recommendations
def get_best_movies(userId):
    userProfile = movie_ratings_user.loc[userId]
    userProfile.dropna(inplace=True)
    userProfile = userProfile.sort_values(ascending=False)
    best_movies = userProfile[:10]
    best_movies = best_movies.to_frame().index.values.tolist()
    return best_movies







