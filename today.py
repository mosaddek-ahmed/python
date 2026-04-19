operator = input("enter the operator(+,-,*,/): ")
num1 = float(input("enter the first number: "))
num2 =float(input("enter the second number: "))

#print("type of num1",type(num1))
#print("type of num2",type(num2))

if operator == "+":
     print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
     print(num1 * num2)

elif operator == "/":
    if num2==0.0:
        print("division by zero not allow")
    else:
        print(num1 / num2)

else:
    print("operator is not a correct operator")   