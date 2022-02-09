import pygame
import sys
from src.chess_game import Game
from pygame.locals import (
    MOUSEBUTTONUP,
    MOUSEBUTTONDOWN,
)

g1= Game()
g1.create_figures()
click_check=False
#g1.member_move(0,1,0,2)
size= {
    "height":800,
    "width":800, 
}

screen = pygame.display.set_mode(
        [size["width"], size["height"]])

pygame.init()

while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if click_check == False:
            if event.type == MOUSEBUTTONDOWN:
                mouse_dict={
                    "x": mouse_pos[0]//100,
                    "y": mouse_pos[1]//100,
                }
            g1.member_chose(mouse_dict)
        if click_check == True:
            if event.type == MOUSEBUTTONDOWN:
                mouse_dict={
                    "x": mouse_pos[0]//100,
                    "y": mouse_pos[1]//100,
                }
            
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((255,255,255))