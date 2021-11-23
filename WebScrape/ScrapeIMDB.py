import requests
from bs4 import BeautifulSoup

try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')

    movies = soup.find('tbody',class_='lister-list').find_all('tr')

    titles = []
    poster_urls = []
    for movie in movies:
        title = movie.find('td',class_='titleColumn').a.text



        titles.append(title)
    print(titles)
except Exception as e:
    print(e)

