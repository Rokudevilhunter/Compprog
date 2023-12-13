## import stuff
import random
import time
import inflect
## Side stuff
roomNum = 2
p = inflect.engine()
health = 10
mobHealth = 1
mobName = ''


def playerDeath():
    print('You DIED! what a RaNdoM way to die!\nBetter luck next time rando!\nYou made to the', (p.ordinal(roomNum)),'room')
    
    exit()

def mobRun():
    global roomNum
    global health
    playerHealth = health
    runChance = random.randint(1,2)
    
    if runChance == 1:
        global runDamage
        runDamage = random.randint(1,3)
        playerHealth -= runDamage
        if playerHealth <= 0:
            playerDeath()
        else:
            print('you took', runDamage, 'damage while trying to escape past the', mobName,'.\n')
            time.sleep(.5)
            health = playerHealth
            roomNum += 1
            newRoom()
    else:
        print('You find an opportune moment to slip past the', mobName + ', barely making it to the next room without a scratch!\n')
        time.sleep(.5)
        roomNum += 1
        newRoom()

def mobAtk():
    while True:
        global roomNum
        global mobDamage
        global mobHealth
        global mobName
        global health
        playerHealth = health
        print('The',mobName,'has',mobHealth,'health.\n')
        time.sleep(.5)
        mobDamage = random.randint(1,3)
        playerHealth -= mobDamage
        playerDamage = random.randint(1,5)
        mobHealth -= playerDamage
        print('The',mobName,'hit you for',mobDamage,'damage.\nYou now have',playerHealth,'health\n')       
        print('You swing and deal',playerDamage,'damage.\n The',mobName + ' now has',mobHealth,'health.\n')
        time.sleep(.5)
        if playerHealth <= 0:
            playerDeath()             
        elif mobHealth <= 0:
            playerHealth += 1
            print('You have killed the',mobName + ', and in doing so gained 1 health.\n')
            health = playerHealth
            roomNum += 1
            newRoom()
            break
        else:
            health = playerHealth
            mobAction()
            break
    

def mobAction():
    while True:
        atkAct = input("\nDo you want to (a)ttack or (r)un?\n")
        if atkAct == ("run") or atkAct.lower() == ("r"):
            mobRun()
            break
        elif atkAct == ("attack") or atkAct.lower() == ("a"):
            time.sleep(.5)
            mobAtk()
            break
        else:
            print("\nPlease enter a valid response")
            continue

    
def randMob():
    global mobHealth
    global mobName
    mob = random.randint(1,3)
    if mob == 1:
        print("\nOh No! a snake is slithering your way\n")
        mobHealth = 5
        mobName = ("Snake")
    elif mob == 2:
        print("\nOh No! a large spider dropped from the ceiling\n")
        mobHealth = 3
        mobName = ("Spider")

    elif mob == 3:
        print("\nOh a hissing black cat lurks in the shadows!\n")
        mobHealth = 10
        mobName = ("Black Feline")
    
def newRoom():
    
    while True:
        global roomNum
        print('You have entered the', (p.ordinal(roomNum)), 'room\n')
        print('You have',health ,'health.')
        time.sleep(.5)
        ifMob = random.randint(1,4)
        if ifMob == (1):
            randMob()
            mobAction()
            break
        else:
            while True:
                action = input('\nPress "w" to walk to the next room.\n')
                if action.lower() == ("w"):
                    roomNum += 1
                    break
                else:
                    print("\nPlease enter a valid response")
                    continue
                

def game():
    while True: 
        print ("welcome to RandomPlayerGame (RPG), where you, a random person, randomly move through a maze and randomly encounter magical beasts!\n")
        time.sleep(.5)
        gameStart = input("Would you like to play? y/n\n")
        time.sleep(.5)
        if gameStart.lower() == ("y"):
            ##inv = []
            ##health = 10
            name = input("\n\nWhat shall I call you, random player?\n")
            print('\n\nok', name +',')
            while True:
                action = input('\nWelcome to the first room, which is surprisingly empty. Shall we (w)alk into the next room?\n')
                if action == ("walk") or action.lower() == ("w"):
                    newRoom()
                else:
                    print("\nPlease enter a valid response")
                    continue
        elif gameStart.lower() == ('n'):
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
        else:
            print("Please enter a valid response")
            continue


game()
