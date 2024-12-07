

def fibanocci(a,b,num):
        if num<=0:
                return
        print(a,end=" ")
        c=a+b
        a=b
        b=c
        fibanocci(a,b,num-1)
num=int(input("Enter the number of terms:"))
if num<=0:
        print("Please enter positive number")
else:
        print("Fibanocci series:")
        fibanocci(0,1,num)



