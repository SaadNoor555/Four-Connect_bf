
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

def check_valid_location(board, col):  #check if the selected column is full or not
	return filled_cols== 0

def place_piece(board, row, col, piece):
    board[row][col] = piece
    filled_cols[col] = row

def get_next_open_row(board, col):
	return int(filled_cols[col]+1) 

place_piece(gameboard, 0, 4, 1)
place_piece(gameboard, 1, 4, 1)
place_piece(gameboard, 2, 4, 1)

print(check_valid_location(gameboard, 4))

print(get_next_open_row(gameboard,4))

boardman.show_board(gameboard)

print(filled_cols)

