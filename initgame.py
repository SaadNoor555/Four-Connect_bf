
import boardman

ROW_no= 6
COLUMN_no = 7

PLAYER_turn = 0
AI_turn = 1


BLANK = 0
PLAYER_piece= 1
AI_piece = 2


gameboard = boardman.generate_board(ROW_no, COLUMN_no)
filled_cols = boardman.generate_filled_cols(COLUMN_no)
game_over = False
turn = PLAYER_turn

def check_valid_location( col):  #check if the selected column is full or not
	return int(filled_cols[col]) < ROW_no

def place_piece(board, row, col, piece):
    board[row][col] = piece
    filled_cols[col] = int(row+1)

def get_next_open_row(col):
	return int(int(filled_cols[col])) 


while not game_over: 
    if turn == PLAYER_turn:
        col = int(input("Player input column no: "))
        if(check_valid_location(col)):
            place_piece(gameboard, get_next_open_row(col), col, PLAYER_piece)
        else : 
            print("invalid col")
    else :
        col = int(input("AI input column no: "))
        if(check_valid_location(col)):
            place_piece(gameboard, get_next_open_row(col), col, AI_piece)
        else : 
            print("invalid col")
    
    turn = (turn+1) %2
    boardman.show_board(gameboard)


# place_piece(gameboard, 0, 4, 1)
# place_piece(gameboard, 1, 4, 1)
# place_piece(gameboard, 5, 4, 1)

# print(check_valid_location(gameboard, 4))
# print(get_next_open_row(gameboard,4))
# print(filled_cols)


boardman.show_board(gameboard)