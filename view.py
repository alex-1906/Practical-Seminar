import pandas as pd
import numpy as np
import streamlit as st
import model

st.title("Recommender System Dashboard")
selected_userId =  st.number_input('Choose user', min_value=1, max_value=610, value=1, step=1)
st.write('User profile of user: ',selected_userId)

#st.write(model.create_user_preferences(selected_userId))
user_preferences = model.create_user_preferences(selected_userId)
user_recommendations = model.get_user_recommendations(selected_userId)
st.write(user_preferences.dropna())
st.write(user_recommendations.dropna())
