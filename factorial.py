def factorial(m):
    if m==0:
        return 1
    else:
        return m*factorial(m-1)
m=int(input("Enter a number: "))
print("The value is: ",factorial(m))