# try:
# 	file = open('text.txt')
# 	dictionary = {'key':'valor'}
# 	print(dictionary['asdfa'])
# except FileNotFoundError:
# 	file = open('text.txt', 'w')
# 	file.write('something')
# except KeyError as message:
# 	print(f'the key {message} does not exist')
# else:
# 	content = file.read()
# 	print(content)
# finally:
# 	raise TypeError('this is an error that I made up')
#
# height = float(input('height: '))
# weight = int(input('weight: '))
#
# if height > 3:
# 	raise ValueError('a altura nao pode ultrapassar 3 metros')
# bmi = weight / (height ** 2)
#
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
# 	try:
# 		fruit = fruits[index]
# 	except IndexError:
# 		print('Fruit pie')
# 	else:
# 		print(fruit + " pie")
#
#
# make_pie(4)
#
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
# 	try:
# 		total_likes = total_likes + post['Likes']
# 	except KeyError:
# 		pass
#
#
# print(total_likes)
