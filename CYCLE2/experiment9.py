#AIM :Write a program to prompt the user for a list of integers. For all values greater than 100,store ‘over’ instead.

n=int(input("enter number of integers to input : "))
list1=[]
for i in range(n):
  num=int(input("enter integers : "))
  if num>100:
    num="over"
  list1.append(num)
print(list1)
