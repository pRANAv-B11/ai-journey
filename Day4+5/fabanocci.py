fab_num = [0, 1]
'''while True:
	user_num = input("Enter the number of Faboanacci number you want to generate (or enter 'quit to exit): ")

	if user_num.lower() == 'quit':
		break

	try:
		n = int(user_num)
	except ValueError:
		print("Enter a valid number")
		continue

	count = 0

	while count < (n-2):
		
		if user_num.lower() == 'quit':
			break
		fab_num.append(fab_num[-1] + fab_num[-2])

		count += 1

	for num in fab_num:
		print(num, end = ' ')'''

#function to generate fabonacci numbers
def fab_limit(x):
	count = 0
	while count < (x-2):
		fab_num.append(fab_num[-1] +fab_num[-2])
		count += 1
	return fab_num

while True:
	user_num = input("Enter the limit of fabannoci terms required (or enter 'quit' to exit): ")
	if user_num.lower() == 'quit':
		break
	
	try:
		n =int(user_num)
		fab_limit(n)
		for num in fab_num:
			print(num, end = ' ')
	except ValueError:	
		print("Enter a valid number")
		
