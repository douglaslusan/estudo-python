import requests as re
from twilio.rest import Client



stock_parameters = {
	'function': 'TIME_SERIES_DAILY',
	'symbol': STOCK_NAME,
	'apikey': ALPHA_API_KEY,
}

response = re.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

print(yesterday_closing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
	up_down = "🔼"
else:
	up_down = "🔽"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

news_parameters = {
	"apiKey": news_api_key,
	"q": COMPANY_NAME,
}

if abs(diff_percent) > 4:
	news_response = re.get(NEWS_ENDPOINT, params=news_parameters)
	articles = news_response.json()["articles"]
	three_articles = articles[:3]

	formatted_article = [f'{STOCK_NAME}: {up_down}{diff_percent}%\nHeadlines: {article["title"]}.' 
							f'\nBrief: {article["description"]}' for article in three_articles]

	client = Client(TWILIO_SID, TOKEN)

	for article in formatted_article:
		message = client.messages.create(
		body= article,
		from_= MY_PHONE_NUMBER,
		to= '+5513997581602'
	)
