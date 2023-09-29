on = input("what is your salary? ")
tw = input("how many years have you been working? ")

lil = int(on) / 20 + int(on)
lol = (f"your now making ${lil}")

if tw != "1":
    if tw != "2":
        if tw != "3":
            if tw != "4":
                if tw != "5":
                    print(lol)

ne = input("what is the length of your rectangle? ")
mab = input("what is the width of your rectangle? ")

lel = "this is a rectangle"
lal = "this is a square"

if ne != mab:
    print(lel)
if ne == mab:
    print(lal)

ol = input("what is your first number? ")
lo = input("what is your second number? ")

if ol < lo:
    print(f"your biggest number is {lo} ") 
if lo < ol:
    print(f"you biggest number is {ol}" )

first = input("how old is the first person? ")
second = input("how old is your second person? ")
third = input("how old is your third person? ")

one = (f"the oldest person is {first}")
two = (f"the oldest person is {second}.")
three = (f"the oldest person is {third}.")

if first > second:
    if first > third:
        print(one)
if second > first:
    if second > third:
        print(two)
if third > first:
    if third > second:
        print(three)

classes_held = input("how many classes have been held? ")
classes_attended = input("how many classes have you attended? ")

to = int(classes_attended) / int(classes_held) * 100

if to > 75:
    print(f"your passing with {to}%.")
if to < 75:
    print(f"you are failing with {to}%.")