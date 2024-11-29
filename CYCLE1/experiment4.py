//aim Write a program to calculate the salary of an employee given his basic pay (to be entered by the user) . HRA = 10 percent of the basic pay, TA = 5 percent of the basic pay.

basic_pay=float(input("enter the basic pay:"))
hra=0.10*basic_pay
ta=0.05*basic_pay
total=hra+ta+basic_pay
print(f"basic pay: {basic_pay}\n hra: {hra}\n ta: {ta}\n total salary: {total}")
