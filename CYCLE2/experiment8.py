#AIM :Create a list of colors from comma-separated color names entered by the user. Display first and last colors.

colors=input("enter the colorlist elements: ")
colorlist=colors.split(",")
print(f"first color:{colorlist[0]},last color: {colorlist[-1]}")
