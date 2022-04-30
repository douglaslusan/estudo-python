# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_min = name1.lower()
name2_min = name2.lower()

contador1 = 0
contador2 = 0

contador1 += name1_min.count('t') + name1_min.count('r') + name1_min.count('u') + name1_min.count('e')

contador1 += name2_min.count('t') + name2_min.count('r') + name2_min.count('u') + name2_min.count('e')

contador2 += name1_min.count('l') + name1_min.count('o') + name1_min.count('v') + name1_min.count('e')

contador2 += name2_min.count('l') + name2_min.count('o') + name2_min.count('v') + name2_min.count('e')


pontos = str(contador1) + str(contador2)

pontosint = int(pontos)

if pontosint < 10 or pontosint > 90:
    print(f"Your score is {pontosint}, you go together like coke and mentos.")

elif pontosint > 40 and pontosint < 50:
    print(f"Your score is {pontosint}, you are alright together.")
else:
    print(f"Your score is {pontosint}.")