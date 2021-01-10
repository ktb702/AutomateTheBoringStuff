#create a tic tac toe game using dict
import random

#global variables
board = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ', 'midM': ' ', 'midR': ' ', 'lowL': ' ', 'lowM': ' ', 'lowR': ' '}
gameOver = False

def play(turn, player, comp):
    if turn == 0: #it's the computer's turn
        # make winning move
        if board['topL']== comp and board['topM'] == comp and board['topR']== ' ':
            board['topR'] = comp
        elif board['topL']== comp and board['topM'] == ' ' and board['topR']== comp:
            board['topM'] = comp
        elif board['topL']== ' ' and board['topM'] == comp and board['topR']== comp:
            board['topL'] = comp
        
        elif board['midL']== comp and board['midM'] == comp and board['midR']== ' ':
            board['midR'] = comp
        elif board['midL']== comp and board['midM'] == ' ' and board['midR']== comp:
            board['midM'] = comp
        elif board['midL']== ' ' and board['midM'] == comp and board['midR']== comp:
            board['midL'] = comp
        
        # block players winning move
        # move on corner
        elif board['topL'] == ' ':
            board['topL'] = comp
        elif board['topR'] == ' ':
            board['topR'] = comp
        elif board['lowL'] == ' ':
            board['lowL'] = comp
        elif board['lowR'] == ' ':
            board['lowR'] = comp

        # move on center
        elif board['midM'] == ' ':
            board['midM'] = comp

        # move on side
        elif board['midL'] == ' ':
            board['midL'] = comp
        elif board['midR'] == ' ':
            board['midR'] = comp
        elif board['topM'] == ' ':
            board['topM'] = comp
        elif board['lowM'] == ' ':
            board['lowM'] = comp

        printBoard()
        turn = 1 # switch to the player's turn

    else: #it's the player's turn
        printBoard()
        move = input('Where would you like to move? Type the row name (top, mid, or low) followed by the column name (L, M, R). No spaces!')
        if board[move] != ' ': # if space is already occupied
            move = input('That space is already taken, please choose another move')
        try:
            board[move] = player
        except KeyError as error:
            move = input('Please enter a valid move. You may use one of the following commands: topL, topM, topR, midL, midM, midR, lowL, lowM, lowR')
        
        turn = 0 # switch to the computer's turn

def isWinner():
    #checks to see if either the player or comp won after their turn
    #possible win - topL, topM, topR
    #possible win - midL, midM, midR
    #possible win - lowL, lowM, lowR
    #possible win - topL, midL, lowL
    #possible win - topM, midM, lowM
    #possible win - topR, midR, lowR
    #possible win - topL, midL, lowL
    #possible win - topL, midM, lowR
    #possible win - topR, midM, lowL


    #checks to see if the board is full and the game ends in a draw
    for key in board:
        if board[key] == ' ':
            break # board is not full yet
        else:
            gameOver = True

def printBoard():
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

def main():
    print('Welcome to Tic Tac Toe!')
    player = input('Would you like to be X or O?')
    player = player.upper()
    comp = 'X' if player != 'X' else 'O'
    print('comp is ' + comp + ', player is ' + player) #debugging

    #randomly choose who will go first
    turn = random.randint(0, 1)
    if turn == 0:
        print('The computer will go first')
    else:
        print('You will go first')

    while (not gameOver):
        play(turn, player, comp)
        isWinner()
    
    # print out who won

    newGame = input('Would you like to play again? (y/n)')
    if newGame.tolower() == 'y':
        main()

if __name__ == '__main__':
    main()