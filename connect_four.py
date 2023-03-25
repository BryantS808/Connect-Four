#Connect 4 game to try get practice on python 
#Player 1 = x
#player 2 = o 
rows = 6
cols = 7
turn = 0 
player_num =1
board = [[0 for i in range(cols)] for j in range(rows)]



def display_board():
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

def player_turn():
    global player_num
    global turn
    print ("Player ", player_num, "'s turn.")

    valid = False
    col = 0
    while valid == False:
        col = input("Pick a column to place your chip: ")
        col = int(col)
        valid = check_valid_col(col)
    col = col -1
    row = drop_token(col)

    #check win
    win = check_win(row, col)
    #change turns
    
    if player_num == 1:
        player_num = 2
    else:
        player_num = 1
    turn +=1
    return win 



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
    #check for a diagonal from that specific row or col
    global player_num
    if((check_horizontal(row,col) or check_vertical(row,col) or check_forward_diag(row,col) or check_back_diag(rows,col)) == True ):
        print("Player ", player_num, "wins.")
        return True
    else:
        return False



def check_horizontal(row,col):
    #since its only connect 4 its easy to brute force it with only 4 options
    #X - currently placed token, Xxxx or xXxx or xxXx or xxxX
    global player_num
    token = None 
    if player_num == 1:
        token = 'x'
    else:
        token = 'o'

    
    #   Xxxx
    #should short circuit before reaching into out of range idx
    if(col +3 < cols) and (board[row][col+1] == board[row][col+2] == board[row][col+3] == token):
            return True
    #xXxx
    elif(col -1 >= 0) and (board[row][col-1] == board[row][col+2] == board[row][col+3] == token):
         return True
    #xxXx
    elif(col -2 >= 0) and (board[row][col-2] == board[row][col-1] == board[row][col+1] == token):
            return True
    #xxxX  
    elif(col -3 >= 0 ) and(board[row][col-3] == board[row][col-2] == board[row][col-1] == token):
            return True
    else:
        return False


def check_vertical(row, col):
    #the only possible way for a vertical win is from top down, so I can check just going down
    global player_num
    token = None 
    if player_num == 1:
        token = 'x'
    else:
        token = 'o'

    #if the deepest row placed was greater than 2 its not high enough for vertical win
    if row > 2:
        return False
    else:
        if(board[row+1][col] == board[row+2][col] == board[row+3][col] == token):
            return True

def check_forward_diag(row,col):
    global player_num
    token = None 
    if player_num == 1:
        token = 'x'
    else:
        token = 'o'
    
    if(col +3 < cols and row +3 < rows) and (board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == token):
        return True
    
    elif(col -1 >= 0 and row +2 < rows) and (board[row-1][col-1] == board[row+2][col+2] == board[row+3][col+3] == token):
         return True
    #xxXx
    elif(col -2 >= 0 and row + 1< rows) and (board[row-2][col-2] == board[row-1][col-1] == board[row+1][col+1] == token):
            return True
    #xxxX  
    elif(col -3 >= 0 and row < rows) and(board[row-3][col-3] == board[row-2][col-2] == board[row-1][col-1] == token):
            return True
    else:
        return False

def check_back_diag(row,col):
    global player_num
    token = None 
    if player_num == 1:
        token = 'x'
    else:
        token = 'o'

    #x
    #.x
    #..x
    #...X
    if(col - 3 >= 0 and row -3 >= 0) and (board[row-1][col-1] == board[row-2][col-2] == board[row-3][col-3] == token):
        return True
    #x
    #.x
    #..X
    #...x
    elif(col +1 <cols and row -2 <=0) and (board[row+1][col+1] == board[row-2][col-2] == board[row-3][col-3] == token):
         return True
    #x
    #.X
    #..x
    #...x
    elif(col +2 < cols and row - 1 <= 0) and (board[row+2][col+2] == board[row+1][col+1] == board[row-1][col-1] == token):
            return True
    #X
    #.x
    # ..x
    # ...x  
    elif(col + 3 < cols and row >= 0) and ((board[row+3][col+3] == board[row+2][col+2] == board[row+1][col+1] == token)):
        return True
    else:
        return False


win = False
display_board()
while(win == False):
    win = player_turn()
    display_board()



