

n=int(input("Enter number of terms:"))
list1=[]
for i in range(n):
        term=int(input(f"Enter  term{i+1}:"))
        list1.append(term)
func=filter(lambda x:x%3==0,list1)
print("Multiples of 3 are:")
multiple=list(func)
print(multiple)
