
import boardman

ROW_no= 6
COLUMN_no = 7

PLAYER_turn = 0
AI_turn = 1


BLANK = 0
PLAYER_piece= 1
AI_piece = 2


gameboard = boardman.generate_board(ROW_no, COLUMN_no)

boardman.show_board(gameboard)