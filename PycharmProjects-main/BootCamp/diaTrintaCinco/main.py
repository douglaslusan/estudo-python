import requests as re
import pandas

api_key = '3fc347a8d1fe4b784d3d1f9d1fbc8623'

parameters = {
	'q':'Santos,BR',
	'appid': api_key,
	'units':'metric',
}

response = re.get(
	'https://api.openweathermap.org/data/2.5/weather',
	params=parameters
)
response.raise_for_status()
data = response.json()
print(data)

for k, v in data.items():
	print(f'{k} {v}')
