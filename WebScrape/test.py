import streamlit as st
import pandas as pd

url1 = 'https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_FMjpg_UX1000_.jpg'
url2 = 'https://m.media-amazon.com/images/M/MV5BMWM5ZDcxMTYtNTEyNS00MDRkLWI3YTItNThmMGExMWY4NDIwXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_FMjpg_UX1000_.jpg'
url3 = 'https://m.media-amazon.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_FMjpg_UX1000_.jpg'
images = [url1,url2,url3]

'''col1,col2,col3 = st.columns(3)
col1.header('Toy Story')
col1.image(url1,use_column_width=True)

col2.header('Toy Story 2')
col2.image(url2,use_column_width=True)

col3.header('Toy Story 3')
col3.image(url3,use_column_width=True)

c = st.container()

col1.markdown(":star: :star: :star: :star: :star:")
col2.markdown(":star: :star: :star: :star: :star:")'''

size = 3
columns = st.columns(size)
for i in range(0,size):
    columns[i].header(i)
    columns[i].image(images[i],use_column_width=True)
    columns[i].markdown(":star: :star: :star: :star: :star:")


