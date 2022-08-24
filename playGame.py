import math
from boardManagement import *
import sys
import pygame

GAMEOVER = False
turn = 1

board = makeBoard()
# graphics()
screen = board_graphics_init()
pygame.display.set_caption('Connect4')
draw_board(board, screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not GAMEOVER:
            print(event.pos)
            print("down")
            col = int(math.floor(event.pos[0]/SQUARE_LEN))

            row = dropPiece(board, col, turn)
            if row == -1:
                print('cannot make move here, try again')
                continue
            draw_board(board, screen)
            print(board)
            if checkWin(board, col, row, turn)==True: 
                print("player "+str(turn)+" has won")
                GAMEOVER = True
                show_msg("player "+str(turn)+" has won", screen)
            if turn==1: turn=2
            else: turn=1