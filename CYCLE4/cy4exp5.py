
n=int(input("Enter number of terms:"))
list1=[]
for i in range(n):
        term=int(input(f"Enter term{i+1}:"))
        list1.append(term)
func=map(lambda x:2**x,list1)
print("Powers of 2 are:")
power=list(func)
print(power)
