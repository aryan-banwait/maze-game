import pygame, os, sys
from maze import Maze
from player import Player
from buttons import *

os.environ['SDL_AUDIODRIVER'] = 'dummy'
pygame.init()

running = True
requested_solve = False
started_solving = False
reached_end = False

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen_size = (screen_width, screen_height) 
screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN | pygame.NOFRAME)
clock = pygame.time.Clock()

bg_color = "black"
game_maze = Maze(screen, 25, 15, 50, 50)
maze_exit = game_maze.cells[game_maze.cols - 1][game_maze.rows - 1]
player = Player("media/pac-ghost.png", 60, 60)
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not started_solving:
                started_solving = True
            if event.key == pygame.K_ESCAPE: 
                running = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_0:
                requested_solve = True
                running = False
        
                
    screen.fill(bg_color)
    game_maze.draw()
    
    if screen.get_rect().contains(player.rect):
        screen.blit(player.image, player.rect.topleft)
        player.move(pygame.key.get_pressed(), game_maze)

    maze_exit_rect = pygame.Rect(maze_exit.x1, maze_exit.y2, game_maze.cell_size, game_maze.cell_size)
    if maze_exit_rect.colliderect(player.rect):
        reached_end = True
        running = False
    timer_display(screen, info.current_w - 150, 60, start_time, started_solving, reached_end)
    
    pygame.display.flip()
    clock.tick(60)


screen.fill(bg_color)
game_maze.draw()
if requested_solve:
    game_maze.solve()

if reached_end:
    timer_display(screen, info.current_w - 150, 60, start_time, started_solving, reached_end)
    screen.blit(player.image, player.rect.topleft)

pygame.display.flip()
after_game = True

while after_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            after_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                after_game = False
            

pygame.quit()
sys.exit()