## import stuff
import random
import time

## Side stuff
def playerHealth():
    print()
def mobHealth():
    print()
def mobRun():
    print()

def mobAtk():
    print("")
def mobAction():
    print("do you want to Attack or Run")
    
def randMob():
    mob = random.randint(1,3)
    if mob == 1:
        print("Oh No! a snake is slithering your way\n")
    elif mob == 2:
        print("Oh No! a large spider dropped from the ceiling\n")

    elif mob == 3:
        print("Oh a hissing black cat lurks in the shadows!\n")
    
def newRoom():
    
    while True:
        print("room desc\n")
        ifmob = random.randint(1,4)
        if ifmob == (1):
            randMob()
            mobAction()
            break
        else:
            action = input('Press "w" to walk to the next room.\n')
            if action.lower() == ("w"):
                continue
                

def game():
    while True: 
        print ("welcome to RandomPlayerGame (RPG), where you, a random person, randomly move through a maze and randomly encounter magical beasts!\n")
        time.sleep(1)
        gameStart = input("Would you like to play?\n")
        time.sleep(1)
        if gameStart.lower() == ("y"):
            ##inv = []
            ##health = 10
            name = input("what shall I call you, random player?\n")
            print('ok', name)
            action = input('Welcome to the first room, press "w" to walk to the next room.\n')
            if action.lower() == ("w"):
                newRoom()
            else:
                break
            break
        else:
            nr = random.randint(1,5)
            if nr == 1:
                print("Ha, I knew you were a wimp!\n")
                break
            if nr == 2:
                print("Scram! You are wasting my time!\n")
                break
            if nr == 3:

                print("  >:(  \n")
                break
            if nr == 4:

                print("You have Really Poor Gamesmanship (RPG). ;)\n")
                break
            if nr == 5:

                print("Thank goodness, I'm glad you're not staying!\n")
                break

game()