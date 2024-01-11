# Tic Tac Toe game in Python

board = [' ' for x in range(10)]

def insertBoard(letter, pos):
    global board
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le))

def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move  = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def player2Move():
    run = True
    while run:
        move = input("Please select a position to place an 'O' (1-9): ")
        try:
            move  = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O's won this time!")
            break

        if not(isWinner(board, 'X')):
            player2Move()
            printBoard(board)
        else:
            print("X's won this time! Good Job!")
            break

    if isBoardFull(board):
        print("Tie Game!")

main()
