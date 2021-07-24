num1 = input("Enter first number: ")
oper = input("Which Operator do you want to use? ")
num2 = input("Enter second number: ")

if (oper == "+"):
    print("result: ", float(num1) + float(num2))
elif (oper == "-"):
    print("result: ", float(num1) - float(num2))
elif (oper == "*"):
    print("result: ", float(num1) * float(num2))
elif (oper == "/"):
    print("result: ", float(num1) / float(num2))