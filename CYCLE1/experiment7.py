//aim Program to accept an integer n and compute n+nn+nnn. [Hint : n = 5, then compute 5 + 55 + 555]

n=int(input("enter the number:"))
result=n+(n*10+n)+(n*100+n*10+n)
print(f"{n}+{n}{n}+{n}{n}{n}={result}")
