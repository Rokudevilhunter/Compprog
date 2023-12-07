## import stuff
import random

## Side stuff



## rooms
w1 = ("you are in a room. Right: (wall) Left: (Wall) Front: (A chest) Back: (door) Up: (Light) Down: (A nice red carpet) ")
w2 = ("you are in a room. Right: (another room) Left: (Wall) Front: (painting) Back: (Window) Up: (Light) Down: (dusty stone floor) ")
w3 = ("you are in a room. Right: (another room) Left: (another room) Front: (Door) Back: (Wall) Up: (Light) Down: (dusty stone floor) ")
w4 = ("you are in a room. Right: (wall) Left: (Wall) Front: (A chest) Back: (door) Up: (Light) Down: (A nice red carpet) ")

## game start
print("GET OUT")
print("welcome to GET OUT, this game is about a room that is slowly being slowly filled with fear...")
play = input("would you like to play? y/n    ")

if play == ("y"):
    cr = w3
    print (cr)
    act = input("what do you do?    ")
elif play == ("n"):
    print("ok, then why are you here?")
    
## Movment
if act == ("help"):
    print("(MOVMENT  (Forward = f) (Backward = b) (left = l) (right = r)  )   (Inventory  (look in inventory = inv)  ) (Attack  (Fight = af) (Run away = ar))") 
    

if act == ("f"):
    if cr == w1:
        print("You can't walk into a wall!")


    elif cr == w2:
        print("You can't walk into a wall!")

            
    elif cr == w3:
        if dl == True:
            print("uh oh, the door is locked!")
            
        else:
            cr = w1
            print(cr)


    elif cr == w4: 
        print("You can't walk into a wall!")


if act == ("b"):
    if cr == w1:
        cr = w2
        print(cr)


    elif cr == w2:
        print("oh no, the window is barred!")


    elif cr == w3:
        print("although the painting looks interesting, you still can't walk into walls.....or jump into paintings.")


    elif cr == w4: 
        print("you can't walk into walls")


if act == ("l"):
    if cr == w1:
        print("You can't walk into walls")


    if cr == w2:
        print("you can't walk into walls")


    if cr == w3:
        cr = w2
        print(cr)

        
    if cr == w4: 
        cr = w3
        print(cr)


if act == ("r"):
    if cr == w1:
        print("you can't walk into walls")


    if cr == w2:
        cr = w3
        print(cr)


    if cr == w3:
        cr = w4
        print(cr)


    if cr == w4:
        print("You can't walk into walls") 



## inventory


## random atk
atk = random.randint(1,4)
if atk == 1 and cr == w2:
    print("atk")

## wall check

## chest

