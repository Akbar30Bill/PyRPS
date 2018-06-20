import getch
from subprocess import call
from random import randint as rand

def i_am_the_winnner(a , b):
    if a == 1:
        if b == 1:
            return 0
        if b == 2:
            return 1
        if b == 3:
            return -1
    if a == 2:
        if b == 1:
            return 1
        if b == 2:
            return 0
        if b == 3:
            return -1
    if a == 3:
        if b == 1:
            return -1
        if b == 2:
            return 1
        if b == 3:
            return 0
    return

def play():
    score1 = 0
    score2 = 0
    call("clear")
    i = input("count of rounds to play?")
    i = int(i)
    call("clear")
    count_of_rounds = i
    while i > 0:
        print ( "\nROCK / PAPER / SCISSORS (r,p,s , or any other key to skip round):" , end = "")
        in_key1 = getch.getche()
        print ("\n")
        in_key2 = rand(1,3)
        if in_key1 == 'r':
            if i_am_the_winnner(1 , in_key2) == 1:
                score1 = score1 + 1
                print ("\tone for player1")
                print ("\t\tplayer1 : %d" % score1)
                print ("\t\tplayer2 : %d" % score2)
            elif i_am_the_winnner(3 , in_key2) == -1:
                score2 = score2 + 1
                print ("\tone for player2")
                print ("\t\tplayer1 : %d" % score1)
                print ("\t\tplayer2 : %d" % score2)
            else:
                print ("\tRound Draw")
                continue
        elif in_key1 == 'p':
            if i_am_the_winnner(2 , in_key2) == 1:
                score1 = score1 + 1
                print ("\tone for player1")
                print ("\t\tplayer1 : %d" % score1)
                print ("\t\tplayer2 : %d" % score2)
            elif i_am_the_winnner(3 , in_key2) == -1:
                score2 = score2 + 1
                print ("\tone for player2")
                print ("\t\tplayer1 : %d" % score1)
                print ("\t\tplayer2 : %d" % score2)
            else:
                print ("\tRound Draw")
                continue
        elif in_key1 == 's':
            if i_am_the_winnner(3 , in_key2) == 1:
                score1 = score1 + 1
                print ("\tone for player1")
                print ("\t\tplayer1 : %d" % score1)
                print ("\t\tplayer2 : %d" % score2)
            elif i_am_the_winnner(3 , in_key2) == -1:
                score2 = score2 + 1
                print ("\tone for player2")
                print ("\t\tplayer1 : %d" % score1)
                print ("\t\tplayer2 : %d" % score2)
            else:
                print ("\tRound Draw")
                continue
        i = i - 1
        if score1 > count_of_rounds / 2:
            print ( "you won" )
            return
        elif score2 > count_of_rounds / 2:
            print ( "you lose!" )
            return
    if score1 > score2 or score1 > count_of_rounds / 2:
        print ( "you won" )
        return
    elif score1 < score2 or score2 > count_of_rounds / 2:
        print ( "you lose!" )
        return
    else:
        print ( "DRAW" )
try:
    play()
except ValueError:
    print("you should have enter a number BLYAT")
