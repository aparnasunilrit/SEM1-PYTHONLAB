
n=int(input("enter a number of terms: "))
sum=0
num=[]
for i in range(n):
	n1=int(input("enter numbers: "))
	num.append(n1)
print(num)
for i in num:
	sum+=i
print(f"sum of list: {sum}")
