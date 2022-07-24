import random 
l = ['rock','scissor','paper']
'''
1 rock vs scissor = rock wins
2 rock vs paper = paper wins
3 scissor vs paper = scissor wins
'''
while True:
    Cchoice = 0
    ccount = 0 
    ucount = 0
    user = int(input('''
    Game start
    1 = yes
    2 = no
    3 = exit
            '''))
    if user == 1:
        for a in range(1,6):
            userinput = int(input('''
            1 = rock
            2 = scissor
            3 = paper                       
                '''))
            if userinput == 1:
                Uchoice = 'rock'
            elif userinput == 2:
                Uchoice = 'scissor'
            elif userinput == 3:
                Uchoice = 'paper'
            Cchoice = random.choice(l)
            if Cchoice == Uchoice:
                print('COMPUTER CHOICE IS = ',Cchoice)
                print('User choice is = ',Uchoice)
                print('GAME IS DRAW')
                ucount = ucount+1
                count = ccount+1
            elif (Uchoice=='rock' and Cchoice == 'scissor') or (Uchoice == 'paper' and Cchoice=='rock') or (Uchoice == 'scissor' and Cchoice == 'paper') :
                print('user value =',Uchoice)
                print('computer choice is = ',Cchoice)
                print('you won  the game')
                ucount = ucount+1
            else:
                print("Computer score= ",ccount)
                print("User score= ", ucount)
                print("Computer wins :> ")
                ccount=ccount+1    
            
        if ucount == ccount:
            print('computer score is = ',ccount)
            print('user score is = ',ucount)
            print('game is draw')
        elif ucount > ccount:
            print('computer score is = ',ccount)
            print('user score is = ',ccount)
            print('user won')
        else:
            print("Computer score is= ", ccount)
            print("User score= ", ucount)
            print("Game Won Computer ")
    else:
        break

            
            
                