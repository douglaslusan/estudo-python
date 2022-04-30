# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_age = int(age)
left_year = 90 - new_age
left_days = left_year * 365
left_weeks = left_year * 52
left_months = left_year * 12

print(f'you have {left_days} days, {left_weeks} weeks and {left_months} months left')
