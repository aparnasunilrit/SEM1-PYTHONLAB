import math
start=int(input("enter the starting range"))
end=int(input("enter the ending range"))
for num in range(start,end+1):
        temp=num
        all_even=True
        while temp>0:
                digit=temp%10
                if digit%2!=0:
                        all_even=False
                        break
                temp//=10
        if all_even and math.isqrt(num)**2==num:
                print(num)
