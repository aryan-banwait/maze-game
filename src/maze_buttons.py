import pygame, os, sys, time
from maze import Maze
from player import Player
from buttons import *

os.environ['SDL_AUDIODRIVER'] = 'dummy'
pygame.init()

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size, pygame.NOFRAME)
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

game_running = True
requested_to_solve_maze = False
user_started_solving = False
user_reached_end = False
after_game = True
user_requests_new_game = False

bg_color = "black"
game_maze = Maze(screen, 25, 15, 50, 50, 50)
maze_exit = game_maze.cells[game_maze.cols - 1][game_maze.rows - 1]
player = Player("media/pac-ghost.png", 60, 60, 30)


def solve_maze():
    global game_running 
    global requested_to_solve_maze
    requested_to_solve_maze = True
    game_running = False

def exit_game():
    pygame.quit()
    sys.exit()


def play_again():
    global game_running
    global after_game
    global user_requests_new_game
    game_running = False
    after_game = False
    user_requests_new_game = True


solve_game_maze_btn = Button(
    game_maze.x1 + (game_maze.cols * game_maze.cell_size) + 50,
    (info.current_h // 2) - 100,
    100,
    50,
    "solve game",
    None,
    24,
    (0, 0, 128),
    (100, 100, 200) 
)

play_again_btn = Button(
    game_maze.x1 + (game_maze.cols * game_maze.cell_size) + 50,
    info.current_h // 2,
    100,
    50,
    "new game",
    None,
    24,
    (0, 0, 128),
    (100, 100, 200) 
)

exit_game_btn = Button(
    game_maze.x1 + (game_maze.cols * game_maze.cell_size) + 50,
    (info.current_h // 2) + 100,
    100,
    50,
    "exit game",
    None,
    24,
    (0, 0, 128),
    (100, 100, 200) 
)

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            exit_game()

        if event.type == pygame.KEYDOWN:
            if not user_started_solving:
                user_started_solving = True
                start_time = pygame.time.get_ticks()

            if event.key == pygame.K_ESCAPE:
                 game_running = False
                 exit_game()


    screen.fill(bg_color)
    game_maze.draw()

    solve_game_maze_btn.draw(screen, "white")
    play_again_btn.draw(screen, "white")
    exit_game_btn.draw(screen, "white")

    solve_game_maze_btn.check_click(solve_maze)
    play_again_btn.check_click(play_again)
    exit_game_btn.check_click(exit_game)

    
    if screen.get_rect().contains(player.rect):
        screen.blit(player.image, player.rect.topleft)
        player.move(pygame.key.get_pressed(), game_maze)


    maze_exit_rect = pygame.Rect(maze_exit.x1, maze_exit.y2, game_maze.cell_size, game_maze.cell_size)
    if maze_exit_rect.colliderect(player.rect):
        user_reached_end = True
        game_running = False
    timer_display(screen, (info.current_w // 2) - 50, 10, start_time, user_started_solving, user_reached_end)
    

    pygame.display.flip()
    clock.tick(60)


screen.fill(bg_color)
solve_game_maze_btn.draw(screen, "white")
play_again_btn.draw(screen, "white")
exit_game_btn.draw(screen, "white")

game_maze.draw()
if requested_to_solve_maze:
    game_maze.solve()
    time.sleep(3)

if user_reached_end:
    final_time = timer_display(screen, (info.current_w // 2) - 50, 10, start_time, user_started_solving, user_reached_end)
    screen.blit(player.image, player.rect.topleft)

pygame.display.flip()


while after_game:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
                    exit_game()
        
    screen.fill(bg_color)
    game_maze.draw()
    solve_game_maze_btn.draw(screen, "white")
    play_again_btn.draw(screen, "white")
    exit_game_btn.draw(screen, "white")

    play_again_btn.check_click(play_again)
    exit_game_btn.check_click(exit_game)

    if user_reached_end:
        text_display(screen, (info.current_w // 2) - 50, 10, f"time: {final_time}s", 36)
        screen.blit(player.image, player.rect.topleft)

    
    pygame.display.flip()
    clock.tick(60)
                

pygame.quit()
sys.exit()
