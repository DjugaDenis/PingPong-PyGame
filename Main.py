import pygame
import sys
from Game import Game
from Menu import Menu

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("PingPong")

font_1 = pygame.font.SysFont(None, 140, True, False)
font_2 = pygame.font.SysFont(None, 70, True, False)

surface = pygame.display.get_surface()

run = True

FPS = 60
clock = pygame.time.Clock()

def start():
    if Game.play() == 1:
        return "Player 1"
    else:
        return "Player 2"

Menu.start()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.VIDEORESIZE:
            WINDOW_SIZE = (surface.get_width(), surface.get_height())
            SCREEN_WIDTH = surface.get_width()
            SCREEN_HEIGHT = surface.get_height()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                run = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)

    if run == True:
        winner = start()

    run = False

    screen.fill([20, 20, 20])
    text_1 = f"{winner} win!"
    text_r_1 = font_1.render(text_1, True, (0, 255, 0))
    text_2 = "R - reset     Esc - exit"
    text_r_2 = font_2.render(text_2, True, (0, 255, 0))
    text_width_1, text_height_1 = font_1.size(text_1)
    text_width_2, text_height_2 = font_2.size(text_2)
    screen.blit(text_r_1, (SCREEN_WIDTH / 2 - text_width_1 / 2, SCREEN_HEIGHT / 2 - text_height_1 / 2))
    screen.blit(text_r_2, (SCREEN_WIDTH / 2 - text_width_2 / 2, SCREEN_HEIGHT / 2 + text_height_1 /2))

    pygame.display.flip()