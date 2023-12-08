import random
import time
def aor():
    print("Its attacking you!")
    akorrn = input("do you run, or do you fight back")

def atk():
    attack = random.randint(1,4)
    if attack == 1:

        if cr == r2:
            ent = ("Window!")

        if cr == r4:
            ent = ("Vent!")
        mon = random.randint(1,3)


        if mon == 1:
            print("Oh No! a snake came through the",ent)
        if mon == 2:
            print("Oh No! a large spider came through the",ent)
        if mon == 3:
            print("Oh a cute cat came through the",ent,"this cat reminds me of the painting!")

def Rstart():
    print(name)
    global cr
    for i in cr:
        time.sleep(1)
        print(i)
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
                cr = r1
                Rstart()
        if cr == r4:
            print("You can't go through walls")
            Rstart()

    if act == ("b"):
        if cr == r1:
            cr = r3
            Rstart() 
        if cr == r2:
            print("You can't go through walls!")
            Rstart()
        if cr == r3:
            print("You can't go through walls!")
            Rstart()
        if cr == r4:
            print("You can't go through walls!")
            Rstart()

    if act == ("l"):
        if cr == r1:
            print("You can't go through walls!")
            Rstart()
        if cr == r2:
            print("You can't go through walls!")
            Rstart()
        if cr == r3:
            cr = r2
            Rstart()
        if cr == r4:
            cr = r3
            Rstart()

    if act == ("r"):
        if cr == r1:
            print("You can't go through walls!")
            Rstart()
        if cr == r2:
            cr = r3
            Rstart()
        if cr == r3:
            cr == r2
            Rstart()
        if cr == r4:
            print("You can't go through walls!")
            Rstart()

    if act == ("hp"):
        print(heath)

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
        health = 10
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
      "Down","   Hard stone floor",
      "Front","   A wall",
      "Back","   A window",
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
    cr = r3
    print(".")
    time.sleep(1)
    name = input("What will your name be?   ")
    time.sleep(1)
    Rstart()
    move()
    

    