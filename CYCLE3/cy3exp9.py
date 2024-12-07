

number = input("Enter a number: ")

if number == number[::-1]:
	print(f"{number} is a palindromic number.")
else:
	print(f"{number} is not a palindromic number.")
