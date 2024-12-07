

number = int(input("Enter a number to find its factors: "))
i = 1
factors = []
while i <= number:
	if number % i == 0:
		factors.append(i)
	i += 1
print(f"The factors of {number} are: {factors}")
