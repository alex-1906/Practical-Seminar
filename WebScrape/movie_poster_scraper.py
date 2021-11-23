import requests
import pandas as pd
import csv
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen


def movie_poster_fetcher(imdb_link):
    try:
        source = requests.get(imdb_link)
        source.raise_for_status()

        soup = BeautifulSoup(source.text,'html.parser')

        url = soup.find('meta',property='og:image')['content']
      #  plot = soup.find('meta',property='og:description')['content']
        return url#,plot
    except Exception as e:
        print(e)

#movies_df['poster_url'] = movies_df['url'].apply(movie_poster_fetcher)
#print(movies_df)
'''liste = []
for url in movies_df.url.values:
    liste.append(movie_poster_fetcher(url))
print(liste)
movies_df['posters'] = liste
print(movies_df.iloc[0].posters)'''

#movies_df.to_csv('movie_posters.csv')


row_names = ['title', 'url']
with open('movie_url.csv', 'r', newline='',encoding='utf-8') as in_csv:
    reader = csv.DictReader(in_csv, fieldnames=row_names, delimiter=';')
    for row in reader:
        title = row['title']
        url = row['url']
        try:
            source = requests.get(url)
            source.raise_for_status()

            soup = BeautifulSoup(source.text, 'html.parser')

            poster = soup.find('meta', property='og:image')['content']

            with open('movie_poster.csv', 'a', newline='',encoding='utf-8') as out_csv:
                writer = csv.writer(out_csv, delimiter=';')
                writer.writerow([title, poster])
            # Ignore cases where no poster image is present
        except AttributeError:
            pass