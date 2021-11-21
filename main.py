import pandas as pd
import numpy as np
import streamlit as st

ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

#Preprocessing
movies_df['genres'] = movies_df.genres.str.split('|')
movies_with_genres = movies_df.copy(deep=True)
movies_df.drop_duplicates(subset='title',inplace=True,ignore_index=True)
    #One-hot encoding the categories
for index, row in movies_df.iterrows():
    for genre in row['genres']:
        movies_with_genres.at[index, genre] = 1

movies_with_genres = movies_with_genres.fillna(0)

#Let's look at the ratings dataframe
ratings_df.drop('timestamp',axis=1,inplace=True)
movie_ratings = pd.merge(ratings_df,movies_df,on='movieId')
movie_ratings_user = movie_ratings.pivot_table(index='userId',columns='title',values='rating')

indices = pd.Series(movies_df.index,index=movies_df['title'])
print(len(indices))

def create_user_profile(userId):
    user_ratings = movie_ratings_user.iloc[userId]
    user_ratings.dropna(inplace = True)
    liste = []
    for i in user_ratings.index:
        liste.append(i)
    user_profile_df = movies_with_genres.iloc[liste]
    user_profile_df.drop(columns=['movieId','genres','index'],inplace=True)
    return user_ratings,user_profile_df

def create_user_preferences(userId):
    ratings, profile = create_user_profile(userId)
    ratings_df = pd.DataFrame(list(zip(ratings.index, ratings.values)), columns=['title', 'rating'])
    user_preferences = profile.T.dot(ratings_df.rating)
    return user_preferences

def get_user_recommendations(userId):
    user_preferences = create_user_preferences(userId)
    user_preferences = pd.DataFrame(list(zip(user_preferences.index, user_preferences.values)), columns=['title', 'score'])
    user_preferences.drop(axis='index', index=0, inplace=True)
    movies_with_genres_ = movies_with_genres.copy(deep=True)
    movies_with_genres_.drop(columns=['movieId','title','genres'],inplace=True)
    recommendations_table = movies_with_genres_.dot(user_preferences.score.to_numpy()) / (user_preferences.score.sum())
    return recommendations_table

def get_top_movies(userId):
    recommendations_table = get_user_recommendations(userId)
    recommendations_table.sort_values(ascending=False, inplace=True)
    top_10_index = recommendations_table.index[:10].tolist()
    top_10_movies = movies_df.iloc[top_10_index]
    return top_10_movies

def get_user_recommendations_1(user_preferences):
    user_preferences = pd.DataFrame(list(zip(user_preferences.index, user_preferences.values)), columns=['title', 'score'])
    user_preferences.drop(axis='index', index=0, inplace=True)
    movies_with_genres_ = movies_with_genres.copy(deep=True)
    movies_with_genres_.drop(columns=['movieId','title','genres'],inplace=True)
    recommendations_table = movies_with_genres_.dot(user_preferences.score.to_numpy()) / (user_preferences.score.sum())
    return recommendations_table

def get_influences(userId):
    ratings, profile = create_user_profile(userId)
    ratings_df = pd.DataFrame(list(zip(ratings.index, ratings.values)), columns=['title', 'rating'])
    recommendations = get_user_recommendations(userId)
    liste = []
    for i in ratings_df.index:
        r_df = ratings_df.drop(index=i, axis=1)
        p_df = profile.drop(index=i, axis=1)
        user_preferences = p_df.T.dot(r_df.rating)
        rec = get_user_recommendations_1(user_preferences)
        #Todo!!!
        score = abs((recommendations - rec).sum())
        liste.append(score)
    ratings_df['influence'] = liste
    ratings_df['influence'] = ratings_df['influence'] / (ratings_df['influence'].max())
    return ratings_df

user_ratings,user_profile = create_user_profile(20)
print(user_ratings)
print(user_profile)

'''influences = get_influences(19)
influences.sort_values(by=['influence'],inplace=True,ascending=False)
print(influences)'''

'''st.title("Recommender System Dashboard")
selected_userId =  st.number_input('Choose user', min_value=1, max_value=610, value=1, step=1)
st.write('User profile of user: ',selected_userId)
user_pref = create_user_preferences(selected_userId)
#user_recommmendations = get_user_recommendations(selected_userId)
#st.write(user_recommmendations)
user_influences = get_influences(selected_userId)
user_influences.sort_values(by=['influence'],inplace=True,ascending=False)
user_profile = create_user_preferences(selected_userId)
user_recommendations = get_top_movies(selected_userId)
#st.write('Here is your profile')
#st.write(user_profile)
st.write('Based on that we recommend you the following movies')
st.write(user_recommendations)
st.write('Your ratings on movies had the following influence')
st.write(user_influences)'''






