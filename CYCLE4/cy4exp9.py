
def add(*args):
	return sum(args)
user_input=input("enter numbers seperated by commas")
numbers=list(map(int,user_input.split()))
print("sum of integers:",add(*numbers))
