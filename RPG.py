## import stuff
import random
import time
## Side stuff
global health
health = 10 - mobDamage - runDamage
def mobHealth():
    global mobH 
    mobH = int(5 - mobDamage)
    print()
def mobRun():
    runChance = random.randint(1,2)
    if runChance == 1:
        global runDamage
        runDamage = random.randint(1,3)
        print("you took dmg")
        time.sleep(1)
        newRoom()
    else:
        print("you made it out\n")
        time.sleep(1)
        newRoom()

def mobAtk():
    while True:
        print("you swing")
        global mobDamage
        mobDamage = random.randint(1,5)
        playerDamage = random.randint(1,5)
        print('you have dealt',playerDamage,'Damage\n')
        time.sleep(1)
        print('you have taken',mobDamage,'Damage\n')
        time.sleep(.5)
        if mobH <= 0:
            print("You have killed the Creature")
            newRoom()
            break
        else:
            mobAction()
            break
    

def mobAction():
    atkAct = input("do you want to Attack or Run\n")
    if atkAct == ("run"):
        mobRun()
    elif atkAct == ("attack"):
        print("You attack")
        time.sleep(1)
        mobAtk()
        

    
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
        time.sleep(1)
        playerHealth()
        ifMob = random.randint(1,4)
        if ifMob == (1):
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
        gameStart = input("Would you like to play? y/n\n")
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