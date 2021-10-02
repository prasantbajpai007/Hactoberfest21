def newtonmeth(n):
    a=n
    for i in range(n):
        n=0.5*(n+a/n)
    return n

n=int(input("enter the first  number"))
m=int(input("enter the second number"))
print(newtonmeth(n))
print(newtonmeth(m))
a=4//2
print(a)
