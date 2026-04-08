# Day 2: Loops & conditionals

# Filter "hot days" (Data preprocessing simulation)
temperature = [33.0, 32.9, 36.0, 28.9, 31.0, 31.6, 32.5] # emperature in degree Celsius
hot_days = []

for temp in temperature:
	if temp > 30:
		hot_days.append(temp)
print(f"Temperatures above 30 degrees: {hot_days}")

# Binary classification simulation
scores = [0.2, 0.8, 0.6, 0.3, 0.9]
predictions = []

for s in scores:
	if s >= 0.5:
		predictions.append("Healthy")
	else:
		predictions.append("Unhealthy")
print(f'predictions: {predictions}')

# Loop through text:
Fruits =['Apple', "Mango", "Guava", 'Jackfruit']

for Fruit in Fruits:
	 if 'a' in Fruit:
		 print(f'{Fruit} contains the letter "a".')

#mini challenge: user input
user_input = input('enter your name: ')
if user_input.lower() == 'pranav':
	print('Welcome back, Pranav!')
else:
	print(f'Who are you?')

# Mini challenge: filter values from a list

numbers = [1, 2, 3, 5, 8, 9, 11, 17, 20, 21]
prime_numbers =[]

for number in numbers:
	if number < 2:  # prime number starts from 2, so less than 2 is not a prime number 
		print(f'{number} is not a prime number')
	else: 
		for i in range(2, int(number**0.5) +1):	#checks if the number is divisible by NUMBER in the range of 2 to sqrt(number)
			if number % i == 0:
				print(number, 'is not a prime number.') #if number is divisible by any i, print statement and break
				break
		else:
				prime_numbers.append(number)	# for  number which is not divisible by i, it is added to prime_number list
			
print(prime_numbers)	

