from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

website = response.text

soup = BeautifulSoup(website, 'html.parser')

articles = soup.findAll(name='a', class_='titlelink')

article_texts = []
article_links = []

for article_tag in articles:
	text = article_tag.getText()
	article_texts.append(text)
	link = article_tag.get('href')
	article_links.append(link)

article_upvotes = []
for score in soup.findAll(name='span', class_='score'):
	if score is None:
		continue
	else:
		article_upvotes.append(int(score.getText().split()[0]))

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])
print('index', largest_index )
print()


# with open("website.html", encoding="utf8") as file:
# 	content = file.read()

# soup = BeautifulSoup(content, 'lxml')

# print(soup.title.string)

# print(soup.prettify())

# print(soup.li)

# anchors = soup.find_all(name='a')

# for anchor in anchors:
# 	print(anchor.getText())
# 	print(anchor.get('href')) #pegar os links

# head = soup.find_all(name='h1', id='name')
#
# print(head)
#
# section_head = soup.find_all(name='h3', class_='heading')
#
# print(section_head)

# name = soup.select_one('#name')
#
# print(name)
#
# heading = soup.select('.heading')
#
# print(heading)
