from IPython.display import clear_output
import random

the_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_board(board): 
 
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  
    print('-----------')
 
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
 
    print('-----------')
  
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    
    choice = 'wrong'
    choice2 = 'wrong'
    
    while choice and choice2 not in ['X', 'O']:
        
        choice = input("Choose X or O as a player 1: ")
        player1 = choice
        choice2 = input("Please choose the opposite as player 2: ")
        player2 = choice2
        
        if choice and choice2 not in ['X','O']:          
            print("Sorry, I didn't understand. Please make sure to choose X or O.")
    if choice and choice2 == 'X' or 'O': 
        return (choice, choice2)
    else:
        return False        
    

def desired_marker(board, marker, position):
    # do i want a dict? assigning the marker to a board index / position
    
    position = int(input("Please choose a position between 1-9 to place your marker"))
    board[position] = marker
    

def win_check(board, mark):
    if mark != 'X' or 'O':
        return (
            print("Please provide X or O as your mark")
        ) 
    else:
        return (
        (board[0:3] == mark) or
        (board[3:6] == mark) or
        (board[6:9] == mark) or
        (board[7] and board[4] and board[1] == mark) or
        (board[8] and board[5] and board[2] == mark) or
        (board[9] and board[6] and board[3] == mark) or
        (board[9] and board[5] and board[1] == mark)
    )
        
def choose_first():
    number = random.randint(0,5)
    if number <= 3:
        return True and print("Player 1 may go first")
    else:
        return print("Player 2 may go first")

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    ## i wrote the code as following:
    # for i in board:
    #     if i != ' ':
    #         return True
    #     else:
    #         return False
    for i in range(1,10):
            if space_check(board, i):
                return False
    return True

def player_choice(board):
    position = int(input("Choose a position for your marker \n Numbers 0 to 2 are the Top position from left to right \n Numbers 3 -5 the middle from left to right and \n numbers 6-8 the bottom. Type here: "))
    if space_check(board, position) == True:
        return position
    else:
        print("Try again with another position!")

def replay():
    
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y','N']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? Y or N ")

        
        if choice not in ['Y','N']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()
            
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
            
    
    # Optionally you can clear everything after running the function
    # clear_output()
    
    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False
    
    
    
#### Here starts the script code

print("Welcome to Tic Tac Toe!")

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn)
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            desired_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            desired_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break