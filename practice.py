print("WELCOME!!!")
Num1 = float(input("Please enter first number:"))
Num2 = float(input("Please enter second number:"))
operation = input("Please enter operation:")
if operation == "add":
    Sum = Num1 + Num2
    print("The answer is:" + str(Sum))
elif operation == "subtract":
    diff = Num1-Num2
    print("The answer is:" + str(diff))
elif operation == "multiply":
    prod = Num1*Num2
    print("The answer is:" + str(prod))
elif operation == "divide":
    div = Num1/Num2
    print("The answer is:" + str(div))
else: print("INVALID OPERATION!!!")
