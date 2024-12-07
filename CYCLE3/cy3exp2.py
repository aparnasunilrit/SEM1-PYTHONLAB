num=int(input("enter a number of terms: "))
a,b=0,1
if(num<=0):
	print("enter a positive number :")
else:
	print("fobonacci series: ")
	for i in range(1,num+1):
		print(a,end=",")
		c=a+b
		a,b=b,c
	print()
