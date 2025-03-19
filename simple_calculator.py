num1= eval(input("Enter a first number:"))
num2= eval(input("Enter a second number"))

print("+,-,/,*")
operation = input("Enter a number")

if operation == "+":
    print("result:")
    print(num1+num2)
elif operation == "-":
    print("result:")
    print(num1-num2)
elif operation == "/":
    print("Result:")
    print(num1/num2)
elif operation == "*":
    print("Result:")
    print(num1*num2)
    
else:
    print("unvalid Operation")
    print("result:")