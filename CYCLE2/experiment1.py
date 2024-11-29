#AIM :Create a string from the given string where the first and last character are exchanged. Eg: Python ⇒ nythoP

str=input("enter a string:")
newstring=str[-1]+str[1:-1]+str[0]
print(f"new string:{newstring}")
