print("The CALC" )

num1 = int(input("What is your first number? "))

math = input("add, subtract, multiply, divide ")

num2 = int(input("What is your second number "))

if math in ["add"] or math in ["Add"] or math in ["+"]:
    print("Your answer is")
    print(num1 + num2)

if math in ["subtract"] or math in ["Subtract"] or math in ["-"]:
    print("Your answer is")
    print(num1 - num2)

if math in ["multiply"] or math in ["Multiply"] or math in ["*"]:
    print("Your answer is")
    print(num1 * num2)

if math in ["divide"] or math in ["Divide"] or math in ["/"]:
    print("Your answer is")
    print(num1 / num2)
else: print("Sorry, I didn't understand")
