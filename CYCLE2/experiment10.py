#AIM : From a list of integers, create a list after removing even numbers.

n=int(input("enter total numbers: "))
listed=[]
for i in range(n):
  num=int(input("enter integers: "))
  if num%2!=0:
    listed.append(num)
print(f"new list: {listed}")
