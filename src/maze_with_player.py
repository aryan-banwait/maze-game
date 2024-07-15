import pygame, os, sys, time
from maze import Maze
from player import Player

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
game_maze = Maze(screen, 25, 15, 50, 50)

player = Player("media/pac-ghost.png", 60, 60)

requested_solve = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                running = False
            if event.key == pygame.K_0:
                requested_solve = True
                running = False
        
                
    screen.fill(bg_color)
    game_maze.draw()

    
    if screen.get_rect().contains(player.rect):
        screen.blit(player.image, player.rect.topleft)
        player.move(pygame.key.get_pressed(), game_maze)

    
    pygame.display.flip()
    clock.tick(60)


screen.fill(bg_color)
game_maze.draw()
if requested_solve:
    game_maze.solve()

pygame.display.flip()
after_game = True

while after_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            after_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                after_game = False

#TODO: Add solve button that basically does the same as pressing K_0 to solve.
#TODO: Add timer that starts when first pygame.keypress is detected and stops when player visits last cell or solve is pressed
            

pygame.quit()
sys.exit()