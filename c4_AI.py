from boardManagement import *
import math
import random


PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2
WINDOW_LEN = 4

def evaluate_window(window, piece):
	score = 0
	opp_piece = PLAYER_PIECE
	if piece == PLAYER_PIECE:
		opp_piece = AI_PIECE

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
		score -= 4
		
	return score

def score_position(board, piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, len(board[0])//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(len(board)):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(len(board[0])-3):
			window = row_array[c:c+SQUARE_LEN]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(len(board[0])):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(len(board)-3):
			window = col_array[r:r+SQUARE_LEN]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(len(board)-3):
		for c in range(len(board[0])-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LEN)]
			score += evaluate_window(window, piece)

	for r in range(len(board)-3):
		for c in range(len(board[0])-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LEN)]
			score += evaluate_window(window, piece)

	return score

def is_terminal_node(board):
	for r in range(len(board)):
		for c in range(len(board[0])):
			if board[r][c]!=0:
				if checkWin(board, c, r, board[r][c]):
					return board[r][c]
	if len(get_valid_locations(board))==0:
		return 0
	return -1

def minimax(board, depth, alpha, beta, maximizingPlayer):
	valid_locations = get_valid_locations(board)
	is_terminal = is_terminal_node(board)
	if depth == 0 or is_terminal!=-1:
		if is_terminal!=-1:
			if is_terminal==AI_PIECE:
				return (None, 100000000000000)
			elif is_terminal==PLAYER_PIECE:
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_position(board, AI_PIECE))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			b_copy = board.copy()
			dropPiece(b_copy, col, AI_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			b_copy = board.copy()
			dropPiece(b_copy, col, PLAYER_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value

def get_valid_locations(board):
	valid_locations = []
	for col in range(len(board[0])):
		if isValidMove(board, col):
			valid_locations.append(col)
	return valid_locations

