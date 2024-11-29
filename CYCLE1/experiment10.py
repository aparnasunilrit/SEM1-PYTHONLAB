#AIM  Write a Python program to determine the rate of entry-ticket in a trade fair based on age as follows:
#Age Rate
#<10 7
#>=10 and <60 10
#>= 60 5

age=int(input("enter your age:"))
if age<10:
  print("your ticket rate for trade fair is:7")
elif 10<= age <60:
  print("your ticket rate for trade fair is:10")
elif age>=60:
  print("your ticket rate for trade fair is :5")
else:
  print("enter the proper age")
