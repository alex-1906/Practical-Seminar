import requests
import pandas as pd
import csv
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
#1145
#7525
movies_df = pd.read_csv('movies.csv')
movies_df = movies_df.loc[9741:]
movies = movies_df.title.values
for movie_title in movies:
    domain = 'http://www.imdb.com'
    search_url = domain + '/find?q=' + urllib.parse.quote_plus(movie_title)
    with urllib.request.urlopen(search_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        # Get url of 1st search result
        try:
            title = soup.find('table', class_='findList').tr.a['href']
            movie_url = domain + title
            with open('movie_url.csv', 'a', newline='',encoding='utf-8') as out_csv:
                writer = csv.writer(out_csv, delimiter=';')
                writer.writerow([movie_title, movie_url])
        # Ignore cases where search returns no results
        except AttributeError:
            pass