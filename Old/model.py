import pandas as pd
import numpy as np


ratings_df = pd.read_csv('../ratings.csv')
movies_df = pd.read_csv('../movies.csv')
movies_df['genres'] = movies_df.genres.str.split('|')
movies_with_genres = movies_df.copy(deep=True)
name = 'test'

# Let's iterate through movies_df, then append the movie genres as columns of 1s or 0s.
# 1 if that column contains movies in the genre at the present index and 0 if not.

x = []
for index, row in movies_df.iterrows():
    x.append(index)
    for genre in row['genres']:
        movies_with_genres.at[index, genre] = 1

# Confirm that every row has been iterated and acted upon
print(len(x) == len(movies_df))
movies_with_genres = movies_with_genres.fillna(0)


#movies_with_genres.drop(columns=['movieId','title','genres'],axis=1,inplace=True)

#Let's look at the ratings dataframe
ratings_df.drop('timestamp',axis=1,inplace=True)
movie_ratings = pd.merge(ratings_df,movies_df,on='movieId')
movie_ratings_user = movie_ratings.pivot_table(index='userId',columns='title',values='rating')

indices = pd.Series(movies_df.index,index=movies_df['title'])


def create_user_profile(userId):
    user_profile = movie_ratings_user.iloc[userId]
    user_profile.dropna(inplace = True)
    user_ratings = user_profile
    liste = []
    for i in user_profile.index:
        liste.append(movies_with_genres.iloc[indices[i]])
    user_profile_df = pd.concat(liste,axis=1).T
    user_profile_df = user_profile_df.reset_index()
    user_profile_df.drop(columns=['movieId','genres','index'],inplace=True)
    return user_ratings,user_profile_df

def create_user_preferences(userId):
    ratings, profile = create_user_profile(userId)
    ratings_df = pd.DataFrame(list(zip(ratings.index, ratings.values)), columns=['title', 'rating'])
    user_preferences = profile.T.dot(ratings_df.rating)
    return user_preferences

def get_user_recommendations(userId):
    user_preferences = create_user_preferences(userId)
    recommendations_table = movies_with_genres.dot(user_preferences.score.to_numpy()) / (user_preferences.score.sum())


print(create_user_preferences(19))
#movies_with_genres.drop(columns=['movieId','title','genres'],inplace=True)
#print(get_user_recommendations(19))
