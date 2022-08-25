
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


def winning_move(board, piece):
	# Check horizontal
	for c in range(COLUMN_no-3):
		for r in range(ROW_no):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical
	for c in range(COLUMN_no):
		for r in range(ROW_no-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check right diaganols
	for c in range(COLUMN_no-3):
		for r in range(ROW_no-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check left sdiaganols
	for c in range(COLUMN_no-3):
		for r in range(3, ROW_no):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def check_game_over(board, player, name):
    if(winning_move(board, player)):
        print(name + " wins!")
        return True
    else:
        return False
    

while not game_over: 
    if turn == PLAYER_turn:
        col = int(input("Player input column no: "))
        if(check_valid_location(col)):
            place_piece(gameboard, get_next_open_row(col), col, PLAYER_piece)
        else : 
            print("invalid col")

        if(check_game_over(gameboard, PLAYER_piece, "Player")):
            game_over = True
        
    else :
        col = int(input("AI input column no: "))
        if(check_valid_location(col)):
            place_piece(gameboard, get_next_open_row(col), col, AI_piece)
        else : 
            print("invalid col")

        if(check_game_over(gameboard, AI_piece, "AI")):
            game_over = True
            break

    boardman.show_board(gameboard)
    turn = (turn+1) %2




# place_piece(gameboard, 0, 4, 1)
# place_piece(gameboard, 1, 4, 1)
# place_piece(gameboard, 5, 4, 1)

# print(check_valid_location(gameboard, 4))
# print(get_next_open_row(gameboard,4))
# print(filled_cols)


boardman.show_board(gameboard)

commit check