import pygame
import numpy as np
from pygame.locals import *
#função para fechar a janela
from sys import exit

pygame.init()
height = 500
width = 500
bg_color = (152, 161, 188)
line_color = (85, 88, 121)
line_width = 10
rows = 3
colluns = 3
board = np.zeros((rows,colluns))

screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("Jogo da velha")
screen.fill(bg_color)

pygame.draw.line(screen, line_color, (50, 100 + 133), (450, 100 + 133), line_width)  # primeira linha horizontal
pygame.draw.line(screen, line_color, (50, 100 + 266), (450, 100 + 266), line_width)  # segunda linha horizontal

# Linhas verticais (dividem as colunas)
pygame.draw.line(screen, line_color, (50 + 133, 120), (50 + 133, 480), line_width)   # primeira linha vertical
pygame.draw.line(screen, line_color, (50 + 266, 120), (50 + 266, 480), line_width)   # segunda linha vertical

def is_available(row,col):
   if board[row][col] == 0:
       return True
   else:
       return False
   
def if_full():
    for r in range(rows):
        for c in range(colluns):
            if board[r][c] == 0:
                return False
    return True
   
def mark_square(row,col,player):
    board[row][col] = player


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()