import random
import time

def game():
    global start
    print ("welcome to GET OUT, this game is about a room that is slowly being slowly filled with fear...")
    print(".")
    time.sleep(1)
    gm = input("Would you like to play?  ")
    time.sleep(1)
    if gm.lower() == ("y"):
        start = True
        inv = []
    else:
        nr = random.randint(1,5)
        if nr == 1:
            time.sleep(1)
            print("ha, I knew you were a wimp!")
        if nr == 2:
            time.sleep(1)
            print("Are you here just to waste my time?")
        if nr == 3:
            time.sleep(1)
            print("  >:(  ")
        if nr == 4:
            time.sleep(1)
            print("Get out... no puns intended")
        if nr == 5:
            time.sleep(1)
            print("Thank goodness, I'm so glad your not staying")

r3 = ("you're in a room, ")

game()

if start == True:
    cr = r1
    print(".")
    time.sleep(1)
    name = input("What shall thy name be for thyself...eww i don't want to say that ever again   ")
    time.sleep(1)
    print(name, r3)

    