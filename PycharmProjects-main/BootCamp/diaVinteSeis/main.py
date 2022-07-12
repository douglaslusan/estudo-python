# list_1 = [1,2,3,4,5]
# list_2 = [n * 2 for n in list_1]
#
# print(f'list 2{list_2}')
#
# lista3 = ['douglas', 'aline', 'raziel', 'airam']
# new_nomes = [item.upper() for item in lista3 if len(item) > 5]
#
# print(new_nomes)
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
#
# squared_numbers = [n ** 2 for n in numbers]
#
# #Write your code 👆 above:
#
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
# result = [n for n in numbers if n % 2 == 0]
#
# #Write your code 👆 above:
#
# print(result)

# with open('file1.txt') as file1:
# 	file1_data = file1.readlines()
# with open('file2.txt') as file2:
# 	file2_data = file2.readlines()
#
# result = [int(n) for n in file1_data if n in file2_data]
#
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# result = {word:len(word) for word in sentence.split()}
#
# print(result)


# import random
#
# names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
#
# scores = {student:random.randint(10,100) for student in names}
#
# print(scores)
# #
# # passed_students = {new_key:new_value for (key, value) in dictionary.items()}
# passed_students = {name:score for (name, score) in scores.items() if score >= 60}
#
# print(passed_students)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {week:(temp * 9 / 5) + 32 for (week, temp) in weather_c.items()}
#
# print(weather_f)

student_dict = {
    'students' : ['raziel', 'douglas', 'aline'],
    'scores' : [50, 80, 30]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas as pd

student_DF = pd.DataFrame(student_dict)

for(index, row) in student_DF.iterrows():
    # print(index)
    # print(row)
    # print(row.students)
    # print(row.scores)
    if row.students == 'douglas':
        print(row.scores)
