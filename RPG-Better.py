import random
import time

def Rstart():
    print(name)
    for i in cr:
        time.sleep(1)
        print(cr)
    global act
    act = input("What do you do?    ")
def move():
    if act == ("f"):
        if cr == r1:
            print("You can't go through walls")
            Rstart()
        if cr == r2:
            print("You can't go through walls")
            Rstart()
        if cr == r3:
            if dl == True:
                print("Oh no, the door is locked")
                Rstart()
            else:
                cr == r1
                Rstart()
        if cr == r4:
            print("You can't go through walls")
            Rstart()
    if act == ("b"):
        if cr == r1
        if cr == r2
        if cr == r3
        if cr == r4
    if act == ("l"):
        if cr == r1
        if cr == r2
        if cr == r3
        if cr == r4
    if act == ("r"):
        if cr == r1
        if cr == r2
        if cr == r3
        if cr == r4

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
        global dl
        dl = False
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

r1 = ["Up","   A dim light",
      "Down","   An old carpet",
      "Front","   A wall",
      "Back","   A door",
      "left","   A door",
      "Right","   A door",]

r2 = ["Up","   A Light",
      "Down","   ",
      "Front","   ",
      "Back","   ",
      "left","   ",
      "Right","   ",]

r3 = ["Up","   ",
      "Down","   ",
      "Front","   ",
      "Back","   ",
      "left","   ",
      "Right","   ",]

r4 = ["Up","   ",
      "Down","   ",
      "Front","   ",
      "Back","   ",
      "left","   ",
      "Right","   ",]

game()

if start == True:
    cr = r1
    print(".")
    time.sleep(1)
    name = input("What shall thy name be for thyself...eww i don't want to say that ever again   ")
    time.sleep(1)
    

    