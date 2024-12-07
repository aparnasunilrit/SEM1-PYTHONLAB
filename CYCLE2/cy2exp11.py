


str=input("enter the list of words seperated by space : ")
words=str.split()
length=0
for i in words:
	if len(i)>length:
		longestword=i
		length=len(i)
print(f"the longest word is {longestword} and its length is {length}")
