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
player = 1

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]

            # Verifica se está fora do tabuleiro
            if 50 <= x <= 450 and 100 <= y <= 500:
                row_clicked = int((y - 100) // 133)
                col_clicked = int((x - 50) // 133)
                
                if is_available(row_clicked,col_clicked):
                    if player == 1:
                        mark_square(row_clicked,col_clicked,1)
                        player = 2
                    elif player == 2:
                        mark_square(row_clicked,col_clicked,2)
                        player = 1
                else:
                    print("Quadrado ja ocupado")
            #Se estiver fora
            else:
                print('fora')
            print(board)

    pygame.display.update()