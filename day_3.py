#Day_3 
num = []

count = 1


while count <=5:
	
	user_numb = input(f'Enter a number for ({count}/5) times(or "done" to finish): ')
	
	if user_numb.lower() == 'done':
		break
	
	try:
		n = int(user_numb)
	except ValueError:
		print("Invalid input. Please enter a valid number.")
		continue

	num.append(n)
	print(f"You entered: {n}. It is ", end="")
	
	if n % 2 == 0:
			print("even.")
	else:
			print(" odd.")

	if n > 0:
			print("positive.")	
	elif n < 0:
			print("negative.")
	else:
			print("zero.")	
	
	if n % 3 == 0:
			print("divisible by 3.")
	
	if n % 5 == 0:
			print("divisible by 5.")
	
	count += 1

#largest number
largest_numb = num[0]
try:
	for n in num:
		if n  > largest_numb:
			largest_numb = n
except IndexError:
	print("No numbers were entered.")

if num:
	print("The largest number is:", largest_numb)
	even_numb_count = sum(1 for n in num if n % 2 == 0)
	odd_numb_count = sum(1 for n in num if n % 2 != 0)
	print("You entered the following numbers:", num)
	print("Count of even numbers:", even_numb_count)
	print("Count of odd numbers:", odd_numb_count)
else:
	print("No numbers were entered.")	
