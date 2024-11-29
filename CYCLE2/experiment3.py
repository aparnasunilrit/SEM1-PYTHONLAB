#AIM :Create a single string separated with space from two strings by swapping the character at position 1.
#Eg : str1 = “Hello” str2 =”World” , then create a string str3 = “Hollo Werld” [Hint: use slicing and concatenation ]
str1=input("enter the first string: ")
str2=input("enter the second string: ")
str3=str1[0]+str2[1]+str1[2:]+" "+str2[0]+str1[1]+str2[2:]
