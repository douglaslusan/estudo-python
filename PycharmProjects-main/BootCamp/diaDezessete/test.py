class User:
	def __init__(self, user_id, username):
		self.id = user_id
		self.username = username
		self.followers = 0
		self.following = 0

	def follow(self, user):
		self.followers += 1
		self.following += 1

	def assassin(self):
		self.username = '?'

user_1 = User('001', 'douglas')
user_2 = User('002', 'raziel')

user_1.assassin()

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


print(f'ID: {user_1.id}\nNome: {user_1.username}')
