'''numb = input("Enter a number: ")
try:
	n = int(numb)
	reverse_num = 0

	while n > 0:
		reverse_num = (n % 10 + reverse_num )*10
		n = n // 10
	print(f"The reverse of the number is: {reverse_num // 10}")
except ValueError:
	print("Enter a valid number")'''

def user_input():
	try:
		n = input("Enter the number to be reversed: ")
		n = int(n)
		return n
	except ValueError:
		print("Inavalid input.")
		return None
	
def num_reverse():
	n = user_input()
	if n is not None:
		reverse_num = 0
		while n > 0:
			reverse_num = (reverse_num + n % 10) * 10
			n = n // 10
		print(f"The reverse of the number is: {reverse_num//10}")

while True:
	num_reverse()
	cont = input("Do you want to reverse another number? (yes/no): ")
	if cont.lower() != 'yes':
		break

