# import smtplib
#
# # gmail = smtp.gmail.com
# # hotmail = smtp.live.com
# # yahoo = smtp.mail.yahoo.com
#
# my_email = 'muramassa@hotmail.com'
# password = ''
#
# with smtplib.SMTP('smtp.live.com') as connection:
# 	connection.starttls() #conexao segura
# 	connection.login(user=my_email, password=password)
# 	connection.sendmail(from_addr=my_email, to_addrs='douglas.lusan@gmail.com', msg='Subject:assunto\n\ncorpo da mensagem')

import datetime as dt
from random import choice

# frases = []
# with open('quotes.txt', 'r') as data:
# 	for frase in data.readlines():
# 		frases.append(frase.strip('\n'))

with open('quotes.txt', 'r') as data:
	frases = data.readlines()
	frase = choice(frases)

print(frase)


# week = dt.datetime.now().weekday()
#
# print(week)
# if week == 5:
# 	print(choice(frases))
