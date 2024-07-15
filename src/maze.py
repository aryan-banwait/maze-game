import random
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
        self.cell_size = 50
        self.cells = []

        if self.seed:
            random.seed(seed)

        self.create_cells()
        self.create_exit()
        self.break_walls_r(0, 0)
        self.reset_visited()


    def create_cells(self):
        for i in range(self.cols):
            cell_col = []
            for j in range(self.rows):
                cell_col.append(Cell(self.screen))
            self.cells.append(cell_col)

    
    def create_exit(self):
        self.cells[self.cols - 1][self.rows - 1].has_bottom_wall = False
        self.draw_cells(self.cols - 1, self.rows - 1)    


    def break_walls_r(self, i, j):
        self.cells[i][j].visited = True

        while True:
            next_index_list = []

            if i > 0 and not self.cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            if i < self.cols - 1 and not self.cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))   
            if j > 0 and not self.cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            if j < self.rows - 1 and not self.cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                return

            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            if next_index[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            self.break_walls_r(next_index[0], next_index[1])
    

    def draw_cells(self, i, j):
        if self.screen is None:
            return
        
        x1 = self.x1 + i * self.cell_size
        y1 = self.y1 + j * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.cells[i][j].draw(x1, y1, x2, y2)


    def draw(self):
         for i in range(self.cols):
            for j in range(self.rows):
                self.draw_cells(i, j)
    

    def reset_visited(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.cells[i][j].visited = False

    