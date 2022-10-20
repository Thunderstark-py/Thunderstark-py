#ThunderStark
import random
ls=['r','p','s']
global upt
global bpt
upt=0
bpt=0

def prnt(inp):
    if inp=="s":
        return "Scissor"
    elif inp=="r":
        return "Rock"
    else:
        return "Paper"


def tmpl(w):
    global upt
    global bpt
    if w=='u':
        print("\n")
        upt+=1
        print("|User V/S Bot|")
        print(prnt(ch),"V/S",prnt(btch))
        print(upt,"  |  ",bpt)
        print("***User Wins***")
    elif w=='t':
        print("\n")
        print("|User V/S Bot|")
        print(prnt(ch),"V/S",prnt(btch))
        print(upt,"  |  ",bpt)
        print("***Tie***")
    else:
        print("\n")
        bpt+=1
        print("|User V/S Bot|")
        print(prnt(ch),"V/S",prnt(btch))
        print(upt,"  |  ",bpt)
        print("***Bot Wins***")


while upt!=7 and bpt!=7:
    btch=random.choice(ls)
    print("\n")
    print('''    p for Paper
    s for Scissor
    r for Rock''')

    ch=input("Enter your choice= ")
    if ch in "rps":
        if ch==btch:
            tmpl('t')
        elif ch=='r' and btch=='s' or ch=='p' and btch=='r' or ch=='s' and btch=='p':
            tmpl("u")
        else:
            tmpl('b')
    else:
        print('''
            Wrong input
                    Give the input again..
        ''')
else:
    print("Game is completed")
    if upt==7:
        print("****User Wins Finally****")
    else:
        print("****Bot Wins Finally****")
#ThunderStark