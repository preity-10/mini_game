import sys
import random
import math

score=[0]
board = [1 for j in range(0,25)]

def print_board():
    x = 1
    n = int(math.sqrt(len(board)))
    for i in range(0,len(board)):
        end = '       |      '
        if(x % n ==0):
            end= ' \n'
            end += '---------------------------------------------------------------\n'

        char=' '
        if(board[i] % 2 == 0)   :
            char = board[i]
        x += 1
        print(char,end=end)

def space_exist():
    c=0
    for i in range(0,len(board)):
        if  board[i] % 2 == 0:
            c += 1
    if c != len(board):
        return True
    else:
        return False

def make_move(board, move,score):
    n = int(math.sqrt(len(board)))
    if( move == 'S'):
        row = 0
        for i in range( (n**2)-(n+1), -1, -1):
            if( (i+1) % n == 0):
                row +=1
            if(board[i] != 1):
                move_du(n,move,i, row,score)

    elif( move =='W'):
        row = 0
        for i in range( n, n**2):
            if( (i) % n == 0):
                row +=1
            if(board[i] != 1):
                move_du(n,move,i, row,score)

    elif( move == 'A'):
        row = 0
        for i in range( 1, n**2):
            row += 1
            if( i % n == 0):
                row = 0
            elif(board[i] != 1):
                move_lr(n,move,i, row,score)

    elif( move == 'D'):
        row = 0
        for i in range( (n**2)-2, -1, -1):
            row += 1
            if( (i+1) % n == 0):
                row = 0
            elif(board[i] != 1):
                move_lr(n,move,i, row,score)
    else:
        print("\nSorry! Some error has occured, Please try again later\n")

    return generate_rand(board)


def move_du(n,move,i, row,score):
    k= 1

    if(move == 'S'):
        if ( board[i+n] == 1):
            for k in range(1,row+1):
                x = i + (k*n)
                if( board[x] != 1 ):
                    break

            if(k == row and board[x] == 1):
                board[x] = board[i]

            elif( board[x] == board[i] ):
                board[x] *= 2
                score[0] += board[x]
            else:
                board[i+((k-1)*n)] = board[i]
            board[i] = 1

        elif( board[i+n] == board[i]):
            board[i+n] *= 2
            board[i] = 1
            score[0] += board[i+n]

    elif(move == 'W'):
        if ( board[i-n] == 1):
            for k in range(1,row+1):
                x = i - (k*n)
                if( board[x] != 1 ):
                    break

            if(k == row and board[x] == 1):
                board[x] = board[i]

            elif( board[x] == board[i] ):
                board[x] *= 2
                score[0] += board[x]
            else:
                board[i-((k-1)*n)] = board[i]
            board[i] = 1

        elif( board[i-n] == board[i]):
            board[i-n] *= 2
            board[i] = 1
            score[0] += board[i-n]

def move_lr(n,move,i,row,score):
    k= 1

    if(move == 'D'):
        if ( board[i+1] == 1):
            for k in range(1,row+1):
                x = i + k
                if( board[x] != 1 ):
                    break

            if(k == row and board[x] == 1):
                board[i+k] = board[i]

            elif( board[x] == board[i] ):
                board[x] *= 2
                score[0] += board[x]
            else:
                board[i+(k-1)] = board[i]
            board[i] = 1

        elif( board[i+1] == board[i]):
            board[i+1] *= 2
            board[i] = 1
            score[0] += board[i+1]

    elif(move == 'A'):
        if ( board[i-1] == 1):
            for k in range(1,row+1):
                x = i - k
                if( board[x] != 1 ):
                    break

            if(k == row and board[x] == 1):
                board[x] = board[i]

            elif( board[x] == board[i] ):
                board[x] *= 2
                score[0] += board[x]
            else:
                board[i-(k-1)] = board[i]
            board[i] = 1

        elif( board[i-1] == board[i]):
            board[i-1] *= 2
            board[i] = 1
            score[0] += board[i-1]

def generate_rand(board):
    n= random.randrange(2,5,2)
    block = random.randrange(0,len(board))
    try:
        if board[block] == 1:
            board[block] = n
        else:
            generate_rand(board)

    except RecursionError:
        print("Thanks for your time, Your score is: ",score)





print('******\n 2048 \n******\n')
n = int(math.sqrt(len(board)))
board[0]=2
board[(n*n)-2*n]=2
print_board()

while space_exist():
    print("*** score:",score," ***")
    print('\n\n# Choose dirn to move the block:-> \n[S,A,W,D : for down, left, top, right respectively] : ',end=' ')
    move = input()

    if (move != 'S' and move != 'A' and move != 'W' and move != 'D'):
        print('\n >> Invalid direction ! Try again !\n')
    else:
        make_move(board, move,score)
        print_board()


print()
print_board()
for i in range(0,n):
    if board[i] == 2048:  #2048
        print("**** you win ****\nAnd score is: ",score)
        break

print("\nSo your final score is: ",score)
