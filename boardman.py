import numpy as np
import pygame
import sys

W, H = 7, 6
SQUARE_LEN = 100
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RADIUS = 0.45*SQUARE_LEN

def generate_board(row,col):
	board = np.zeros((row,col))
	return board

def generate_filled_cols(col):
	filled_cols = np.zeros(col)
	return filled_cols

def show_board(board):
	print(np.flip(board,0))


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
            if board[row][col]==0:
                color = BLACK
            elif board[row][col]==1:
                color = RED
            else:
                color = YELLOW
            pygame.draw.circle(screen, color, (int(col*SQUARE_LEN+SQUARE_LEN/2), int(row*SQUARE_LEN+(3*SQUARE_LEN/2))), RADIUS)
    pygame.display.update()

	
def show_msg(txt, screen):
    font = pygame.font.SysFont('Verdana', 70)
    text = font.render(txt, True, (WHITE))
    text_rect = text.get_rect(center=(W*SQUARE_LEN//2, SQUARE_LEN//2))
    screen.blit(text, text_rect)
    pygame.display.update()