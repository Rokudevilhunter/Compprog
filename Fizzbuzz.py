u = input("pick a number between 1-12 ")
w = input("numbers that are divisible by my number, should be replaced with ____ ")

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
   