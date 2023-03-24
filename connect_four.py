#Connect 4 game to try get practice on python 
#Player 1 = x
#player 2 = 0 
rows = 6
cols = 7
turn = 0 
player_num =1
board = [[0 for i in range(cols)] for j in range(rows)]



def display_board(board):
    for i in range(0, rows):
        for j in range (0, cols):
            #print the Board frame and what token may be in it if not then pritn a space
            print("| ", (board[i][j] if board[i][j] != 0 else " "), end = " ")
        print ("|")
    for i in range (0, cols *5 +1):
        print("-", end = "")
    print("")
    for i in range (0, cols):
        print(" ", i+1, " ", end ="")
    print("")

def player_turn(board):
    global player_num
    global turn
    print ("Player ", player_num, "'s turn.")

    valid = False
    col = 0
    while valid == False:
        col = input("Pick a column to place your chip: ")
        col = int(col)
        valid = check_valid_col(col)
    row = drop_token(col-1)

    #check win
    
    #change turns
    if player_num == 1:
        player_num = 2
    else:
        player_num = 1
    turn +=1
    



def check_valid_col(col):
    print(type(col))
    if isinstance(col, int) ==  False:
        print("You did not enter a valid integer")
        return False
    if col > cols or cols < 1:
        print("Please enter an intger from 1 to ", cols)
        return False
    if board[0][col-1] != 0:
        print("That column is full please pick another")
        return False
    
    return True

def drop_token(col):
    #find deepest row
    row = 0
    while row +1 <= rows -1 and board[row+1][col] == 0:
        row +=1

    #place token
    if player_num == 1:
        board[row][col] = 'x'
    else:
        board[row][col] = 'o'
    return row

def check_win(row, col):
    


