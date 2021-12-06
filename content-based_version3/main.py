from model import Recommender
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

recommender = Recommender()
posters = recommender.posters
#Methods for button controlling
def counter_reset():
    st.session_state.count = 0
if 'count' not in st.session_state:
	st.session_state.count = 0
def increment_counter():
	st.session_state.count += 1

st.title("Recommender System Dashboard")
selected_userId =  st.number_input('Choose user', min_value=1, max_value=610, value=1, step=1,on_change=counter_reset)
recommendations = recommender.get_scaled_scores(selected_userId).head()

st.write('Recommendations for user: ',selected_userId)


if(st.button('Get next recommendation',on_click=increment_counter)):
    st.write(st.session_state.count)
    st.write('Here is your ',st.session_state.count,'th recommendation: ', recommendations.index[st.session_state.count-1])
    try:
        st.image(posters[recommendations.index[st.session_state.count-1]],width=400)
    except Exception:
        st.image("https://i.ibb.co/TqJsxKM/IMG-20190204-WA0001.jpg",width=400)
    st.write('Because you liked the following movies: ')
    images = []
    titles = []
    stars = []
    scores = recommendations.iloc[st.session_state.count-1].root_scores
    for title in recommendations.iloc[st.session_state.count-1].roots:
        try:
            images.append(posters[title])
        except Exception:
            images.append("https://i.ibb.co/TqJsxKM/IMG-20190204-WA0001.jpg")
        titles.append(title)

        #get star ratings
        ratings = recommender.get_user_ratings(selected_userId)
        n = int(ratings[title])
        star = ''
        for i in range(0,n):
            star += ' :star: '
        stars.append(star)
    columns = st.columns(len(titles))
    for i in range(0,len(titles)):
        columns[i].caption(titles[i])
        columns[i].image(images[i],use_column_width=True)
        columns[i].markdown(stars[i])
    #plot the bar chart
    scores = np.array(scores, dtype='float32')
    fig = plt.figure(figsize=(18, 5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(titles, scores, color='royalblue')

    st.pyplot(fig)
