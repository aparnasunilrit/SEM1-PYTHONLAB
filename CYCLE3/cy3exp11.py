


num = int(input("Enter a number: "))
original_num = num
sum_of_powers = 0
num_digits = 0
temp = num
while temp > 0:
	temp //= 10
	num_digits += 1
temp = num
while temp > 0:
	digit = temp % 10
	sum_of_powers += digit ** num_digits
	temp //= 10
if sum_of_powers == original_num:
	print(f"{original_num} is an Armstrong number.")
else:
	print(f"{original_num} is not an Armstrong number.")
