import streamlit as st
import pandas as pd
import numpy as np

movies = pd.read_csv('../movies.csv')
ratings = pd.read_csv('ratings.csv')
ratings.drop(columns='timestamp',inplace=True)
movie_ratings = pd.merge(ratings,movies,on='movieId')
movie_ratings_user = movie_ratings.pivot_table(index='userId',columns='title',values='rating')


#st.write(movie_ratings_user.head(100))
#st.write(movie_ratings_user.loc[1])
st.title('Recommender Systems Dashboard')

user_count = movie_ratings['userId'].values

st.sidebar.header('Input')
selected_userId = st.sidebar.selectbox('Choose User Profile',list([1,2,3]))
st.sidebar.selectbox('Choose Algorithm',list(['content-based','collaborative-filtering','others']))

def load_userId(userId):
    userProfile = movie_ratings_user.loc[userId]
    userProfile.dropna(inplace=True)
    st.write(userProfile)
st.write('Profile of user: ',selected_userId)
load_userId(selected_userId)