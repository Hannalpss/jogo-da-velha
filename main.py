import pygame
from pygame.locals import *
#função para fechar a janela
from sys import exit

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Jogo da velha")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()