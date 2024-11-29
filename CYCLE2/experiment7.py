#AIM :Write a python program to read two lists color-list1 and color-list2. Print out all colors from color-list1 not contained in color-list2.

list1_element=input("enter the colorlist1 elements ")
colorlist1=list1_element.split(",")
list2_element=input("enter the colorlist2 elements ")
colorlist2=list2_element.split(",")
uniquelist=[]
for color in colorlist1:
  if color not in colorlist2:
    uniquelist.append(color)
print(uniquelist)
