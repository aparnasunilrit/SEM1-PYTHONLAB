

N = int(input("Enter the value of N: "))
primes = []
for num in range(2, N + 1):
	is_prime = True
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			is_prime = False
			break
	if is_prime:
		primes.append(num)
print("Alternate prime numbers up to", N, "are:")
for i in range(0,len(primes),2):
	print(primes[i], end=" ")
	print()
