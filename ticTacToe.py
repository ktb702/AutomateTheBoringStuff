#create a tic tac toe game using dict
import random

#global variables
board = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ', 'midM': ' ', 'midR': ' ', 'lowL': ' ', 'lowM': ' ', 'lowR': ' '}

def compTurn(comp, player):
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
    
    elif board['lowL']== comp and board['lowM'] == comp and board['lowR']== ' ':
        board['lowR'] = comp
    elif board['lowL']== comp and board['lowM'] == ' ' and board['lowR']== comp:
        board['lowM'] = comp
    elif board['lowL']== ' ' and board['lowM'] == comp and board['lowR']== comp:
        board['lowL'] = comp
    
    # block players winning move
    if board['topL']== player and board['topM'] == player and board['topR']== ' ':
        board['topR'] = comp
    elif board['topL']== player and board['topM'] == ' ' and board['topR']== player:
        board['topM'] = comp
    elif board['topL']== ' ' and board['topM'] == player and board['topR']== player:
        board['topL'] = comp
    
    elif board['midL']== player and board['midM'] == player and board['midR']== ' ':
        board['midR'] = comp
    elif board['midL']== player and board['midM'] == ' ' and board['midR']== player:
        board['midM'] = comp
    elif board['midL']== ' ' and board['midM'] == player and board['midR']== player:
        board['midL'] = comp
    
    elif board['lowL']== player and board['lowM'] == player and board['lowR']== ' ':
        board['lowR'] = comp
    elif board['lowL']== player and board['lowM'] == ' ' and board['lowR']== player:
        board['lowM'] = comp
    elif board['lowL']== ' ' and board['lowM'] == player and board['lowR']== player:
        board['lowL'] = comp

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


def playerTurn(player):
    move = input('Where would you like to move? Type the row name (top, mid, or low) followed by the column name (L, M, R). No spaces!')
    if board[move] != ' ': # if space is already occupied
        move = input('That space is already taken, please choose another move')
    try:
        board[move] = player
    except KeyError as error:
        move = input('Please enter a valid move. You may use one of the following commands: topL, topM, topR, midL, midM, midR, lowL, lowM, lowR')

def isWinner(let):
    #checks to see if either the player or comp won after their turn
    if ((board['topL'] == let and board['topM'] == let and board['topR'] == let) or #possible win - topL, topM, topR 
        (board['midL'] == let and board['midM'] == let and board['midR'] == let) or #possible win - midL, midM, midR
        (board['lowL'] == let and board['lowM'] == let and board['lowR'] == let) or #possible win - lowL, lowM, lowR
        (board['topL'] == let and board['midL'] == let and board['lowL'] == let) or #possible win - topL, midL, lowL
        (board['topM'] == let and board['midM'] == let and board['lowM'] == let) or #possible win - topM, midM, lowM
        (board['topR'] == let and board['midR'] == let and board['lowR'] == let) or #possible win - topR, midR, lowR
        (board['topL'] == let and board['midL'] == let and board['lowL'] == let) or #possible win - topL, midL, lowL
        (board['topL'] == let and board['midM'] == let and board['lowR'] == let) or #possible win - topL, midM, lowR
        (board['topR'] == let and board['midM'] == let and board['lowL'] == let)):  #possible win - topR, midM, lowL
        gameOver = True
        print('Congrats ' + let + ', you win!')
        return gameOver
    
    else:
        #checks to see if the board is full and the game ends in a draw
        count = 0
        for key in board:
            if board[key] == ' ':
                count += 1
        if count == 0: #if there are no empty space then it's a draw
            gameOver = True
            print("It's a draw.")
            return gameOver

def printBoard():
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

def main():
    gameOver = False
    print('Welcome to Tic Tac Toe!')
    player = input('Would you like to be X or O?')
    player = player.upper()
    if player != 'X' and player != 'O':
        player = input('That is not a valid selection. Please choose X or O: ')
    comp = 'X' if player != 'X' else 'O'
    print('comp is ' + comp + ', player is ' + player) #debugging

    #randomly choose who will go first
    turn = random.randint(0, 1)
    if turn == 0:
        print('The computer will go first')
    else:

        print('You will go first')

    while (not gameOver):
        if turn == 0: #computer's turn
            compTurn(comp, player)
            letter = comp
            turn = 1 #switch to player's turn
        else: #player's turn
            printBoard()
            playerTurn(player)
            letter = player
            turn = 0 #switch to computer's turn
        
        #check to see if either player won the game with the last move 
        gameOver = isWinner(letter)
    
    newGame = input('Would you like to play again? (y/n)')
    print()
    if newGame == 'y': #.tolower() 
        main()

if __name__ == '__main__':
    main()