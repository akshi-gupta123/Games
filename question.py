import random
import string
print("We are going to play games\n")
print("Enter 1 to play HANGMAN")
print("Enter 2 to play STONE-PAPER-SCISSOR")
print("Enter 3 to play DICE ROLL")
print("Enter 4 to play GUESS THE NUMBER")
choice=int(input("Enter the number you want to play\n"))
if choice==1:
    print("WELCOME TO HANGMAN GAME")
    print("\nYOU HAVE TO GUESS THE CHARACTERS OF HIDDEN WORD\n")
    letter=["hello","hangman","word","story","books","cooking"]
    word=random.choice(letter)
    turns=10
    words=""
    while turns>0:
        count=0
        game=input("Character is :")
        words=words+game
        if game not in word:
            turns=turns-1
            print("Wrong input")
            print("Try again")
        print("Now",+turns,"turns left")
        if turns==0:
            print("You loss")
            break
        for i in word:
            if i in words:
                print(i)
            else:
                print("*")
                count=count+1
        if count==0:
            print("You won")
            break
    print("Word is :",word)
    print("Thanks for playing the game")
if choice==2:
    print("WELCOME TO GAME")
    print("Player VS Computer")
    print("STONE PAPER SCISSOR")
    choice="yes"
    while choice=="yes" or choice=="y":
        print("\nEnter your choice")
        n=input()
        x="scissor","stone","paper"
        print("\nComputer choice is")
        comp=random.choice(x)
        print(comp)
        if n=="stone" and comp=="scissor":
            print("You won")
        elif n=="scissor" and comp=="paper":
            print("You won")
        elif n=="paper" and comp=="stone":
            print("You won")
        elif n==comp:
            print("Draw")
        else:
            print("Computer won you lose")
        choice=input("\nDo u want to continue") 
    print("Thanks for playing the game")
if choice==3:
    print("WELCOME TO ROLLONG THE DICE")
    choice="yes"
    l=[]
    n=[]
    while choice=="Yes" or choice=="yes":
        print("ROLLING THE DICE")
        print("You are player 1 ")
        t=random.randint(1,6)
        print("Player 1:",t)
        m=random.randint(1,6)
        print("Player 2:",m)
        l.append(t)
        n.append(m)
        if m>t:
            print("Computer is leading this time")
        elif m<t:
            print("You are leading this time")
        else:
            print("Equal")
        choice=input("Do you want to continue")
    sum1=0
    sum2=0
    for i in l:
        sum1=sum1+i
    for j in n:
        sum2=sum2+j
    if sum1>sum2:
        print("You won the match and your score is :",sum1,"computer score is :",sum2)
    else:
        print("You loose and your score is :",sum1,"computer score is :",sum2)
    print("Thank you for playing the game")

if choice==4:
    print("WELCOME TO GUESS THE NUMBER")
    num=str(random.randint(10000,1000000))
    turns=5
    numbers=""
    while turns>0:
        count=0
        charc=input("Enter the number:")
        numbers=numbers+charc
        if charc not in num:
            turns=turns-1
            print("Wrong guess")
            print("Try again")
        print("Now",turns,"turns left")
        if turns==0:
            print("You loss")
            break
        for i in num:
            if i in numbers:
                print(i)
            else:
                print("*")
                count=count+1
        if count==0:
            print("You won")
            break
    print("Number is :",num)
    print("Thank you for playing the game")

