from model import Recommender
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt

recommender = Recommender()
poster = recommender.posters



st.title("Recommender System Dashboard")
selected_userId =  st.number_input('Choose user', min_value=1, max_value=610, value=1, step=1)
preferences = recommender.get_user_preferences(selected_userId)
recommendations = recommender.get_user_recommendations(selected_userId).head(3)

#horizontal bar plot
x=preferences.preference.values
y=preferences.genre.values
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.barh(y, x, color='royalblue',align='center')
st.pyplot(fig)

titles = []
posters = []
plots = []
for movie in recommendations.iterrows():
    posters.append(poster[movie[1].title])
    titles.append(movie[1].title)
    plots.append(recommender.movies_df.iloc[recommender.indices[movie[1].title]].genres)
columns = st.columns(3)
for i in range(0,3):
    columns[i].image(posters[i])
    columns[i].write(titles[i])
    columns[i].write(plots[i])


