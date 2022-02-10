import pygame
import sys
from src.chess_game import Game
from pygame.locals import (
    MOUSEBUTTONUP,
    MOUSEBUTTONDOWN,
)

g1= Game()
g1.write_figures()

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
       
        if event.type == MOUSEBUTTONDOWN:
            mouse_dict={
                "x": mouse_pos[0]//100,
                "y": mouse_pos[1]//100,
            }
            click_check = g1.member_chose(mouse_dict)

        
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((234,205,174))
    g1.draw_figures(screen)
    pygame.display.flip()