#0 1 1 2 3 5 8 13
n=int(input("enter total number:"))
a=0
b=1
while(n>0):
    print(a)
    a,b=b,a+b
    n=n-1
    