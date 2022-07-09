names_list = []

with open('.\\Input\\Names\\invited_names.txt', 'r') as letter:
	for name in letter.readlines():
		names_list.append(name.strip('\n'))


with open('.\\Input\\Letters\\starting_letter.txt') as letter:
	let = letter.read()
	for i in range(len(names_list)):
		new_letter = let.replace('[name]', names_list[i])
		with open(f'.\\Output\ReadyToSend\\letter_for_{names_list[i]}.txt', 'w') as file:
			file.write(new_letter)
