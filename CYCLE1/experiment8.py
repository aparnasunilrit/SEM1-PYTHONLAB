//aim Find biggest of 3 numbers entered.

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if num1>num2:
  if num1>num3:
    print(f"{num1} is greater")
elif num2>num3:
  print(f"{num2} is greater")
else:
  print(f"{num3} is greater")
