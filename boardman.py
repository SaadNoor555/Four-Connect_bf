import numpy as np


def generate_board(row,col):
	board = np.zeros((row,col))
	return board

def generate_filled_cols(col):
	filled_cols = np.zeros(col)
	return filled_cols

def show_board(board):
	print(np.flip(board,0))

