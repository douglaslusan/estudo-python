import datetime as dt
import pandas as pd
from random import randint
import smtplib

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

TODAY = (today_month, today_day)
data = pd.read_csv('birthdays.csv')

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if (today_month, today_day) in birthdays_dict:
	birthdays_person = birthdays_dict[TODAY]
	file_path = f'letter_templates/letter_{randint(1,3)}.txt'
	with open(file_path) as letter:
		letter_aniver = letter.read()
		letter_name = letter_aniver.replace('[NAME]', birthdays_person['name'])

	with smtplib.SMTP('smtp.live.com') as connect:
		connect.starttls()
		connect.login(user='muramassa@hotmail.com', password='myamoto')
		email = connect.sendmail(
			from_addr='muramassa@hotmail.com',
			to_addrs=birthdays_person['email'],
			msg=f'Subject:Happy Birthday\n\n{letter_name}')
