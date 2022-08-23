import numpy as np

def makeBoard(w=7, h=6):
    board = [[0 for i in range(w)] for j in range(h)]
    return np.array(board)

def dropPiece(board, col, turn):
    if isValidMove(board, col):
        board[getRow(board, col)][col] = turn

def getRow(board, col):
    for row in range(len(board)-1, -1, -1):
        if board[row][col]==0:
            return row

def isValidMove(board, col):
    return board[0][col] == 0

makeBoard()