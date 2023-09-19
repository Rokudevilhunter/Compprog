print("The CALC" )

num1 = int(input("What is your first number? "))

math = input("add, subtract, multiply, divide ")

num2 = int(input("What is your second number "))

if math in ["add"] or math in ["Add"]:
    print("Your answer is")
    print(num1 + num2)

if math in ["subtract"] or math in ["Subtract"]:
    print("Your answer is")
    print(num1 - num2)

if math in ["multiply"] or math in ["Multiply"]:
    print("Your answer is")
    print(num1 * num2)

if math in ["divide"] or math in ["Divide"]:
    print("Your answer is")
    print(num1 / num2)


