import pygame, random
from cell import Cell

class Maze():
    def __init__(self, screen, cols, rows, x1, y1, seed=None):
        self.screen = screen
        self.x1 = x1
        self.y1 = y1
        self.maze_rect = self.screen.get_rect()
        self.maze_rect.topleft = (self.x1, self.y1)
        self.rows = rows
        self.cols = cols
        self.seed = seed
        self.cell_size = 72
        self.cells = []

        if self.seed:
            random.seed(seed)
        
        self.create_cells()
        self.create_exit()
        self.break_walls_r()


    def create_cells(self):
        for i in range(self.cols):
            cell_col = []
            for j in range(self.rows):
                cell_col.append(Cell(self.screen))
            self.cells.append(cell_col)
        for i in range(self.cols):
            for j in range(self.rows):
                self.draw_cells(i, j)

    
    def draw_cells(self, i, j):
        if self.screen is None:
            return
        
        x1 = self.x1 + i * self.cell_size
        y1 = self.y1 + j * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.cells[i][j].draw(x1, y1, x2, y2)

    
    def create_exit(self):
        self.cells[self.cols - 1][self.rows - 1].has_bottom_wall = False
        self.draw_cells(self.cols - 1, self.rows - 1)    

    def break_walls_r(self):
        return

    