board=[' ' for x in range(10)]

def printBoard(board):
    print(' ','|',' ','|')
    print(board[1],'|',board[2],'|',board[3])
    print(' ','|',' ','|')
    print('----------')
    print(' ','|',' ','|')
    print(board[4],'|',board[5],'|',board[6])
    print(' ','|',' ','|')
    print('----------')
    print(' ','|',' ','|')
    print(board[7],'|',board[8],'|',board[9])
    print(' ','|',' ','|')

def insertLetter(pos,let):
    board[pos]=let

def isBoardfull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def isSpaceFree(pos):
    return board[pos]==' '

def isWinner(bo,let):
    return bo[1]==let and bo[2]==let and bo[3]==let or bo[4]==let and bo[5]==let and bo[6]==let or bo[7]==let and bo[8]==let and bo[9]==let or \
           bo[1]==let and bo[4]==let and bo[7]==let or bo[2]==let and bo[5]==let and bo[8]==let or bo[3]==let and bo[6]==let and bo[9]==let or \
           bo[1]==let and bo[5]==let and bo[9]==let or bo[3]==let and bo[5]==let and bo[7]==let

def playerMove():
    run=True
    while run:
        move=input("Please select a position from 1-9:")
        try:
            move=int(move)
            if move>0 and move<10:
                if isSpaceFree(move):
                    board[move]='X'
                    run=False
                else:
                    print('This space is already occupied')
            else:
                print('You have to input within the range(1~9)')
        except:
            print('It must be a number')

def compMove():
    possibleMoves=[x for x,y in enumerate(board) if y==' ' and x>0]
    move=0
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy=board[:] #mistake
            boardCopy[i]=let
            if isWinner(boardCopy,let):
                move=i
                return move
        
    cornersOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen)>0:
        move=selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move=5
        return move
    
    edgeOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgeOpen.append(i)
    if len(edgeOpen)>0:
        move=selectRandom(edgeOpen)
            
    return move
     
def selectRandom(lst):
    import random
    move=random.choice(lst)
    return move

def main():
    print('Welocme to Tic Tac Toe game. \n It includes 9 position(1-9) starting from the top left')
    printBoard(board)
    while not isBoardfull(board):
        if not isWinner(board,'O'):
            playerMove()
            printBoard(board)
        else:
            print(board)
            print('Computer wins this time!')
            break
        if not isWinner(board,'X'):
            move=compMove()
            if move!=0:
                insertLetter(move,'O')
                print('The computer has move to position',move,'.')
                printBoard(board)
            else:
                print('Tie Game, there is no space left to move')
        else:
            print('You win!!')
            break
    if isBoardfull(board):
        print('Tie Game, the board is full.')
main()
while True:
    answer=input('Would you like to play again (Y/N)')
    if answer.lower()=='y' or answer.lower()=='yes':
        board=[' ' for x in range(10)]
        main()
    else:
        break

