#AIM :Get a string from an input string where all occurrences of the first character are replaced with ‘$’, except the first character. [eg: onion -> oni$n]

str=input("enter a string which has reoccurence of first character: ")
firstchar=str[0]
newstr=firstchar+str[1:].replace(firstchar,'$')
print(f"newstring is: {newstr}")
