import random

def match(comp,you):
    if comp==you:
        return None

    elif comp == "r":
        if you == "s":
            return False
        elif you=="p":
            return True

    elif comp == "p":
        if you == "r":
            return False
        elif you=="s":
            return True

    elif comp == "s":
        if you == "p":
            return False
        elif you=="r":
            return True

    
while True:
    print("Comp Turn: Rock(r), Paper(p), Scissor(s)")
    rando = random.randint(1,3)
    if rando == 1:
        comp = "r"
    elif rando == 2:
        comp = "p"
    elif rando == 3:
        comp = "s"

    you = input("Your Turn: Rock(r), Paper(p), Scissor(s) : ")
    print (f"Computer chooses: {comp}")
    print (f"You chooses: {you}")   

    a=match(comp,you)

    if a == None:
        print ("The match is tie")
    elif a :
        print ("You won the match")
    else :
        print("You lose the match")

    q = input("Do you want to play another match? y/n : ")
    if q[0] == "n":
        break
