



n=int(input("Enter  number of integers to input:"))
list1=[]
for i in range(n):
	num=int(input("Enter integers:"))
	list1.append(num)
n=int(input("Enter  number of integers to input:"))
list2=[]
for i in range(n):
	num=int(input("Enter integers:"))
	list2.append(num)

if len(list1)==len(list2):
	print("lists are of the same length")
else:
	print("The lists are of different lengths.")

if sum(list1) == sum(list2):
	print("The lists sum to the same value.")
else:
	print("The lists do not sum to the same value.")

common_value = set(list1).intersection(list2)
if common_value:
	print(f"Common values in both lists: {common_value}")
else:
	print("There are no common values in both lists.")
