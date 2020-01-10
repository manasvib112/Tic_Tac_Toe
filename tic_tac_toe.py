import random

m=[['0','1','2'],['3','4','5'],['6','7','8']]
player=1
count=1  

def printgrid():
    global m
    global player
    # print '\n'*100
    # print '\r'
    for i in range(3):
        print'----------'
        for j in range(3): 
            print'|'+ (m[i][j]),
        print'|'
    print'----------'

def inputvalue(a):
    global m
    global player
    i=int(a/3)
    j=a%3
    if(a>8 or m[i][j]=='x' or m[i][j]=='o'):
        print'invalid move! try again'
        return False
    elif(player==1):
        m[i][j]='x'
    elif(player==2):
        m[i][j]='o'
    return True
            
def check_row(mode=1):
    global m
    global player
    for i in range(3):
        if(m[i][0]==m[i][1] and m[i][0]==m[i][2]):
            if(mode==2 and player==2):
                print 'Computer wins!!'
            else:
                print 'player ' + str(player) + ' wins'
            printgrid()
            return True
    return False

def check_column(mode=1):
    global m
    global player
    for j in range(3):
        if(m[0][j]==m[1][j] and m[0][j]==m[2][j]):
            if(mode==2 and player==2):
                print 'Computer wins!!'
            else:
                print 'player ' + str(player) + ' wins'
            printgrid()
            return True
    return False


def check_diag(mode=1):
    global m
    global player
    if(m[0][0]==m[1][1] and m[0][0]==m[2][2]):
        if(mode==2  and player==2):
            print 'Computer wins!!'
        else:
            print 'player ' + str(player) + ' wins'
        printgrid()
        return True
    if(m[0][2]==m[1][1] and m[1][1]==m[2][0]):
        if(mode==2  and player==2):
            print 'Computer wins!!'
        else:
            print 'player ' + str(player) + ' wins'
        printgrid()
        return True
    return False

def playgame():
    global m
    global player
    global count
    if(count>9):
        print 'The game has tied!!'
        printgrid()
        return
    print'player '+str(player)+'s turn.'
    printgrid()
    val=input()
    while (not inputvalue(val)):
        printgrid()
        val=input()
    count+=1
    if(not check_row()):
        if(not check_column()):
            if(not check_diag()):
                if(player==2):
                    player=1
                else:
                    player=2
                playgame()

def compTurn():
    global m
    i=random.randint(0,2)
    j=random.randint(0,2)
    while(m[i][j]=='x' or m[i][j]=='o'):
        i=random.randint(0,2) 
        j=random.randint(0,2)  
    m[i][j]='o'

def playComp():
    global m
    global player
    global count
    if(count>9):
        print 'The game has tied!!'
        printgrid()
        return
    if(player==1):
        print'player '+str(player)+'s turn.'
        printgrid()
        val=input()
        while (not inputvalue(val)):
            printgrid()
            val=input()
    elif(player==2):
        compTurn()
    count+=1
    if(not check_row(2)):
        if(not check_column(2)):
            if(not check_diag(2)):
                if(player==2):
                    player=1
                else:
                    player=2
                playComp()

 
print 'Select Mode (1/2)'
print '1: Player vs Player'
print '2: Player vs Computer'
mode=input()
cond=True
while cond:
    if(mode==1):
        playgame()
        cond=False
    elif(mode==2):
        playComp()
        cond=False
    else:
        print 'Sorry! I did not get you, Please press 1 or 2'
        mode=input()
