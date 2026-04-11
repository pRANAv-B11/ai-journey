
'''num = []


while True:
	user_num = input("Enter a number to check if it is a prime nuser_numumber or not (or enter 'quit' to exit the window.): ")
	if user_num.lower() == 'quit':
		break
	try:
		n = int(user_num)
		if n > 1:
			for i in range(2, int (n**0.5) +1):
				if n % i == 0:
					print(f"{n} is not a prime number. ")
					break
			else:
				print(f"{n} is a prime number.")
				num.append(n)
		else:
			print(f"{n} is not a prime number.")	
	except ValueError:
		print("Enter a valid number")

print(f"The prime numbers entered till now: {num}")'''

#function to check if a number is prime or not
def is_prime(x):
	if x > 1:
		for i in range(2, int(x**0.5) + 1):
			if x % 2 == 0:
				return False
		else:
			return True
	else:
		return False
	
while True:
	user_num = input("Enter a number to check if it is a prime nuser_numumber or not (or enter 'quit' to exit the window.): ")
	if user_num.lower() == 'quit':
		break
	try:
		n = int(user_num)
		if is_prime(n):
			print(f"{n} is a prime number.")
		else:
			print(f"{n} is not a prime number.")
	except ValueError:
		print("Enter a valid number")


	

