#AIM Write a Python program to solve a quadratic equation.

import math
def solve_quadratic(a,b,c):
  discriminant= b**2 - 4*a*c
  if discriminant>0:
    root1=(-b+math.sqrt(discriminant))/(2*a)
    root2=(-b-math.sqrt(discriminant))/(2*a)
    return f"the equation has two real roots:{root1} and {root2}"
  elif discriminant == 0:
    root= -b/(2*a)
    return f"the equation has one real root:{root}"
  else:
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(-discriminant)/(2*a)
    return f"the equation has two complex roots: {real_part}+{imaginary_part}i and {real_part}-{imaginary_part}i"
a=float(input("enter the coefficient a: "))
b=float(input("enter the coefficient b: "))
c=float(input("enter the coefficient c: "))
result= solve_quadratic(a,b,c)
print(result)
