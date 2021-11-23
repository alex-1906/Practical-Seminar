import pandas as pd
import csv
import requests
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup


'''movie_title = 'Andrew Dice Clay: Dice Rules (1991)'
movie_title = 'Bungo Stray Dogs: Dead Apple (2018)'
domain = 'http://www.imdb.com'
search_url = domain + '/find?q=' + urllib.parse.quote_plus(movie_title)
with urllib.request.urlopen(search_url) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    # Get url of 1st search result
    try:
        title = soup.find('table', class_='findList').tr.a['href']
        movie_url = domain + title
        print(movie_url)
        with open('movie_url.csv', 'a', newline='',encoding='utf-8') as out_csv:
            writer = csv.writer(out_csv, delimiter=';')
            writer.writerow([movie_title, movie_url])
        # Ignore cases where search returns no results
    except AttributeError as ae:
        print(ae)
        pass'''

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
print(movie_poster_fetcher('https://www.imdb.com/name/nm0001048/'))