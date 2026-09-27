a=int(input("enter the num do you want: "))
i=1
totalPrice = 0
while(i<=a):
    brand=input("Enter the phone brand: ")
    model=input("Enter the phone model: ")
    price=int(input("Enter the phone price: "))

    totalPrice = totalPrice + price 
    print("my phone is: " ,brand,model,price)
    i=i+1
print(totalPrice)
    