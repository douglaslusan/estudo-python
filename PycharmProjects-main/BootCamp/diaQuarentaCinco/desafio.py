import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url)

website = response.text

soup = BeautifulSoup(website, 'html.parser')

texts = soup.findAll(name='h3', class_='title')

movie_titles = [text.get_text() for text in texts]

movies = movie_titles[::-1]

with open('filmes.txt', 'w') as file:
	for movie in movies:
		file.write(f'{movie.encode("utf8")}\n')
