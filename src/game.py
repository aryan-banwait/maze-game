import pygame, os, sys, time
from maze import Maze
from player import Player
from buttons import *

def play_game():
    os.environ['SDL_AUDIODRIVER'] = 'dummy'
    pygame.init()

    info = pygame.display.Info()
    screen_width = info.current_w
    screen_height = info.current_h
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size, pygame.NOFRAME)
    clock = pygame.time.Clock()
    
    bg_color = "black"
    pregame_lobby_running = True
    chosen_difficulty = ""

    easy_btn = Button(
        (info.current_w // 2) - 275,
        (info.current_h // 2),
        150,
        75,
        "easy",
        None,
        36,
        "green",
        "green"  
    )
    
    medium_btn = Button(
        (info.current_w // 2) - 75,
        (info.current_h // 2),
        150,
        75,
        "medium",
        None,
        36,
        "yellow",
        "yellow"        
    )

    hard_btn = Button(
        (info.current_w // 2) + 125,
        (info.current_h // 2),
        150,
        75,
        "hard",
        None,
        36,
        "red",
        "red"  
    )

    exit_game_btn = Button(
    info.current_w - 100,
    0,
    100,
    50,
    "exit game",
    None,
    24,
    (200, 0, 0),
    (255, 100, 100) 
    )


    def clicked_easy():
        nonlocal chosen_difficulty
        chosen_difficulty = "easy"
        
    
    def clicked_medium():
        nonlocal chosen_difficulty
        chosen_difficulty = "medium"
        
    
    def clicked_hard():
        nonlocal chosen_difficulty
        chosen_difficulty = "hard"

    def exit_game():
        pygame.quit()
        sys.exit()
        
    
    while pregame_lobby_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game()

        screen.fill(bg_color)
        text_display(screen, (info.current_w // 2) - 200, (info.current_h // 2) - 125, "Choose a difficulty level:", 48)

        easy_btn.draw(screen, "black")
        medium_btn.draw(screen, "black")
        hard_btn.draw(screen, "black")
        exit_game_btn.draw(screen, "white")

        easy_btn.check_click(clicked_easy)
        medium_btn.check_click(clicked_medium)
        hard_btn.check_click(clicked_hard)
        exit_game_btn.check_click(exit_game)
    
        if chosen_difficulty != "":
            print(chosen_difficulty)
            break

        pygame.display.flip()
        clock.tick(60)

    
    if chosen_difficulty is None or chosen_difficulty == "":
        sys.exit()


    start_time = pygame.time.get_ticks()
    game_running = True
    requested_to_solve_maze = False
    user_started_solving = False
    user_reached_end = False
    after_game = True
    user_requests_new_game = False

    player_size = 0
    player_pos = (0, 0)
    player = None
    maze_cols = 0
    maze_rows = 0
    maze_cell_size = 0
    game_maze = None


    if chosen_difficulty == "easy":
        player_size = 40
        player_pos = (60, 60)
        player = Player("media/pac-ghost.png", player_pos[0], player_pos[1], player_size)
        maze_cols = 16
        maze_rows = 10
        maze_cell_size = 75
        game_maze = Maze(screen, maze_cols, maze_rows, 50, 50, maze_cell_size)
    elif chosen_difficulty == "medium":
        player_size = 35
        player_pos = (60, 60)
        player = Player("media/pac-ghost.png", player_pos[0], player_pos[1], player_size)
        maze_cols = 20
        maze_rows = 12
        maze_cell_size = 60
        game_maze = Maze(screen, maze_cols, maze_rows, 50, 50, maze_cell_size)
    elif chosen_difficulty == "hard":
        player_size = 30
        player_pos = (60, 60)
        player = Player("media/pac-ghost.png", player_pos[0], player_pos[1], player_size)
        maze_cols = 25
        maze_rows = 16
        maze_cell_size = 50
        game_maze = Maze(screen, maze_cols, maze_rows, 50, 50, maze_cell_size)
    else:
        sys.exit()

    maze_exit = game_maze.cells[game_maze.cols - 1][game_maze.rows - 1]


    def solve_maze():
        nonlocal game_running 
        nonlocal requested_to_solve_maze
        requested_to_solve_maze = True
        game_running = False


    def exit_game():
        pygame.quit()
        sys.exit()


    def play_again():
        nonlocal game_running
        nonlocal after_game
        nonlocal user_requests_new_game
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

    if user_requests_new_game:
        play_game()
        
    pygame.quit()