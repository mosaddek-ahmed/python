n=int(input("Enter the range="))
t=0
for m in range(1,n+1,1):
    c=0
    for i in range(2,m,1):
        if(m%i==0):
            c=c+1
    if(c==0):
        t=t+1

        print(m)
print("total prime number=",t)
