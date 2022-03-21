import random
name=input("enter a name")
if name>"abcdefghijklmnopqrstuvwxyz":
    print("-------------***WELCOME TO MY GAME--------------**")
    print("COWBULL")
numberlist=[]
def makenumber():
    for i in range (4):
        x=random.randrange(0,9)
        numberlist.append(x)
    return numberlist
def playgame():
    b=makenumber()
    print("your secret number = ",b)
    tries=0
    while tries<5:
        cows=0
        bulls=0
        choice=input("enter a  4 digit")
        if len(choice)==4:
            guess=[]
            for i in range(len(choice)):
                guess.append(int(choice[i]))
            print(guess)
            for i in range(len(guess)):
                if (guess[i] in b):
                    cows+=1
                if guess[i]==b[i]:
                    bulls+=1
        else:
            print("sorry enter only 4 digit")
        print("BULLS:",bulls ,"COWS:",cows)
        if bulls==len(b):
            print("---------------**** congratulations_____***you won after")
            break
        tries=tries+1
    if bulls<len(b):
        print("sorry you lose game ")
        
playgame()