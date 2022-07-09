# list_data = []
# with open('weather_data.csv') as file:
# 	for date in file.readlines():
# 		new_data = date.strip()
# 		list_data.append(new_data)
#
# print(list_data)

# import csv
#
# with open('weather_data.csv') as data_file:
# 	data = csv.reader(data_file)
#
# 	temperatures = []
# 	for row in data:
# 		if row[1] != 'temp':
# 			temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas as pd

# data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# print(data_dict)
# print(data['temp'].to_list())

# print(sum(data['temp'])/len(data['temp'])) #media

# print(data['temp'].mean()) #media

# print(data['temp'].max()) #valor mais alto

# print(data['condition']) #operacoes iguais
# print(data.condition)

# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()])
	#linha   coluna        condicao

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp * 9 / 5 + 32 #atribuindo a temperatura de monday e convertendo em farenheit
#
# print(monday_temp)

# data_dict = {
# 	'students': ['amy', 'james', 'angela'],
# 	'scores': [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
#
# data.to_csv('new_data.csv')

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

squirrel_gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
squirrel_black_count = len(data[data['Primary Fur Color'] == 'Black'])
squirrel_cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])


data_dict = {
	'Fur Color': ['gray', 'black', 'cinnamon'],
	'count': [squirrel_gray_count, squirrel_black_count, squirrel_cinnamon_count]
}


new_data = pd.DataFrame(data_dict)
new_data.to_csv('fur_colors_squirrel')

print(new_data)
