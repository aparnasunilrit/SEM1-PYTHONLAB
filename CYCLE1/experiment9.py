//AIM Program to determine whether a year is a leap year or not

year=int(input("enter a year:"))
if year%4!=0:
  print(year,"not a leap year")
elif year%100!=0:
  print(year,"is a leap year")
elif year%400==0:
  print(year,"is a leap year")
else:
  print(year,"is not a leap year")
