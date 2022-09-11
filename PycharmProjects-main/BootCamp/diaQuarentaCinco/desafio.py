import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url)

website = response.text

soup = BeautifulSoup(website, 'html.parser')

texts = soup.findAll(name='h3', class_='title')

for text in texts:
	print(text.get_text())
