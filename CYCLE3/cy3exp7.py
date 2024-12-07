


upper_limit = int(input("Enter the upper limit: "))

total_sum = 0
for num in range(1, upper_limit):
	if num % 6 == 0 and num % 4 != 0:
		total_sum += num

print(f"The sum of all integers divisible by 6 but not by 4 below {upper_limit} is: {total_sum}")


