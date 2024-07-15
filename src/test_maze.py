import pygame, os, sys
from maze import Maze

os.environ['SDL_AUDIODRIVER'] = 'dummy'
pygame.init()

running = True
screen_info = pygame.display.Info()
screen_size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
bg_color = "black"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Maze(screen, 16, 9, 50, 50)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
