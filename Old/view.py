import streamlit as st
import model

st.title("Recommender System Dashboard")

st.sidebar.header('Input')
selected_userId =  st.number_input('Choose user', min_value=1, max_value=610, value=1, step=1)
st.sidebar.selectbox('Choose Algorithm',list(['content-based','collaborative-filtering','others']))

def load_userId(userId):
    userProfile = model.movie_ratings_user.loc[userId]
    userProfile.dropna(inplace=True)
    st.write(userProfile)



st.write('Profile of user: ',selected_userId)
load_userId(selected_userId)

clicked_best_movies = st.button('Get favourite movies')
clicked_rec = st.button('Click for recommendations')
best_movies = []
if(clicked_best_movies):
    best_movies = model.get_best_movies(selected_userId)
    st.write('Here are your favourite 10 movies', best_movies)

if(clicked_rec):
    recommendations = model.get_recommendations(selected_userId, best_movies)
    st.write('Based on them we suggest you: ', recommendations)