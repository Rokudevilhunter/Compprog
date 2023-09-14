print("The CALC" )

num1 = int(input("What is your first number? "))

math = input("add, subtract, multiply, divide ")

num2 = int(input("What is your second number "))

if math in ["add"]:
    print("Your answer is")
    print(num1 + num2)

if math in ["subtract"]:
    print("Your answer is")
    print(num1 - num2)

if math in ["multiply"]:
    print("Your answer is")
    print(num1 * num2)

if math in ["divide"]:
    print("Your answer is")
    print(num1 / num2)


