# Purpose of Program to play Tic-Tac_toe Game
# Global variables set up here

#Set up Game baord visual parameters
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

#If the game is still going. Can't have a winner if game is still going
game_still_going = True

winner = None

#Who's turn is it
current_player = "x"


#function for display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#function for playing the game
def playing_game():

    # A way to show the initial board to player
    display_board()

    while game_still_going:
        
        #let's program know how to handle the turns
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()
        
        #allows the program to know when to flip to other player
        flip_player()

    # condition for if the game has ended
    if winner == "x" or winner == "O":
        print(winner + " player won.")
    elif winner == None:
        print("The game is a Tie.")

# function for handling turns
def handle_turn(player):
    # tells the user who's turn it is
    print(player + "'s turn." )
    #asks the user where they want to place their x or o
    position = input("Chose a position from 1-9: ")
    
    valid = False
    while not valid:

        #Just in case user puts incorrect number as input and the while loop just in case the user continues to do it
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Incorrect position number, Chose a position from 1-9:")

        #How the pieces are positioned
        position = int(position) - 1

        #Just in case player trys to put x or o in a position that is already filled
        if board[position] == "_":
            valid = True
        else:
            print("You can't place piece there, Go again.")


    board[position] = player
    
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

#function for check win
def check_if_win():

    #acces global variables from top
    global winner

    # check rows
    row_winner = check_row()
    # check columns
    column_winner = check_column()
    # check diagonals
    diagonal_winner = check_diagonals()
    
    #Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_row():
    # need to access global variable game_still_going since checking would be the game still going
    global game_still_going
    #since three in a row would be the same value i.e. "x x x" or "o o o"
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    
    #If any row does have a match, program will know there is a win 
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]  

def check_column():
    # need to access global variable game_still_going since checking would be the game still going
    global game_still_going
    #since three in a column would be the same value i.e. in a vertical direction"x x x" or "o o o"
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    
    #If any column does have a match, program will know there is a win 
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2] 
    return

def check_diagonals():
    # need to access global variable game_still_going since checking would be the game still going
    global game_still_going
    #since three in a diagonal would be the same value i.e. in a diagonal direction"x x x" or "o o o"
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[6] == board[4] == board[2] != "_"
    
    #If any diagonal does have a match, program will know there is a win 
    if diagonal_1 or diagonal_2:
        game_still_going = False
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

# function to check tie
def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
    return

def flip_player():
    #global variable that is needed
    global current_player
    #If the current playr was x, then changes to o
    if current_player == "x":
        current_player = "o"
    #If the current player was 0, then changes to x
    elif current_player == "o":
        current_player = "x"
    return

playing_game()