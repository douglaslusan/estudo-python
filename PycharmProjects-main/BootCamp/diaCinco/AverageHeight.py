# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

soma = 0
media = 0
div = 1

for student in student_heights:
	soma += student
	media = soma / div
	div += 1

print(round(media))
