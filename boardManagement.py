import numpy as np
import pygame

W, H = 7, 6
SQUARE_LEN = 100
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RADIUS = 0.45*SQUARE_LEN

def makeBoard(w=7, h=6):
    board = [[0 for i in range(w)] for j in range(h)]
    W, H = w, h
    return np.array(board)

def dropPiece(board, col, turn):
    if isValidMove(board, col):
        row = getEmptyRow(board, col)
        board[row][col] = turn
        return row

def getEmptyRow(board, col):
    for row in range(H-1, -1, -1):
        if board[row][col]==0:
            return row

def isValidMove(board, col):
    return board[0][col] == 0

def checkWin(board, col, row, turn):
    # checking horizontally
    cnt=0
    for i in range(W):
        if board[row][i]==turn: cnt+=1
        else: cnt=0
        if cnt>=4: return True   
    
    # checking vertically
    cnt =0
    for i in range(H):
        if board[i][col]==turn: cnt+=1
        else: cnt=0
        if cnt>=4: return True

    # checking diagonal \
    cnt=1
    for i in range(1, W):
        if row+i>=H or col+i>=W : break
        if board[row+i][col+i]==turn: cnt+=1
        else: break
    for i in range(1, W):
        if row-i<0 or col-i<0 : break
        if board[row-i][col-i]==turn: cnt+=1
        else: break
    if cnt>=4 : return True

    # checking diagonal /
    cnt=1
    for i in range(1, W):
        if row+i>=H or col-i<0 : break
        if board[row+i][col-i]==turn: cnt+=1
        else : break
    for i in range(1, W):
        if row-i<0 or col+1>=H : break
        if board[row-i][col+1]==turn : cnt+=1
        else : break
    if cnt>=4 : return True

    return False

def board_graphics_init():
    pygame.init()
    
    B_W = W*SQUARE_LEN
    B_H = (H+1)*SQUARE_LEN
    screen = pygame.display.set_mode((B_W, B_H))
    return screen

def draw_board(board, screen):
    for col in range(W):
        for row in range(H):
            pygame.draw.rect(screen, BLUE, (col*SQUARE_LEN, row*SQUARE_LEN+SQUARE_LEN, SQUARE_LEN, SQUARE_LEN))
            pygame.draw.circle(screen, BLACK, (int(col*SQUARE_LEN+SQUARE_LEN/2), int(row*SQUARE_LEN+(3*SQUARE_LEN/2))), RADIUS)