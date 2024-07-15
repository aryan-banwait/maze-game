import pygame, os, sys
from maze import Maze

os.environ['SDL_AUDIODRIVER'] = 'dummy'
pygame.init()

running = True
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen_size = (screen_width, screen_height) 
screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN | pygame.NOFRAME)
clock = pygame.time.Clock()
bg_color = "black"
game_maze = Maze(screen, 25, 14, 50, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                running = False
                
    screen.fill(bg_color)
    game_maze.draw()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
