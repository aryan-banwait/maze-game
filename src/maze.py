import pygame, random
screen = pygame.display.set_mode(1280, 720)

class Maze():
    def __init__(self, scree, rows, cols, seed=None):
        self.maze_rect = screen.get_rect()
        self.maze_rect.topleft = (0, 0)
        self.rows = rows
        self.cols = cols
        self.seed = seed
        self.cell_size = (72, 72)

        if self.seed:
            random.seed(seed)
        
        self.create_cells()
        self.create_entrance_and_exit()
        self.break_walls_r()

#TODO: CREATE METHODS TO MAKE MAZE, PS. ANIMATION NOT REQUIRED

    def create_cells(self):
        return
    
    
    def create_entrance_and_exit(self):
        return
    

    def break_walls_r(self):
        return

    