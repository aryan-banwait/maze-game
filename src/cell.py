import pygame

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, start_point, end_point, screen=None):
        self.start_point = start_point
        self.end_point = end_point
        self.screen = screen


    def draw_line(self, fillcolor="white"):
        pygame.draw.line(
            self.screen, fillcolor, (self.start_point.x, self.start_point.y), (self.end_point.x, self.end_point.y), 2
            )
        


class Cell():
    def __init__(self, screen=None):
        self.screen = screen
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.visited = False


    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.has_top_wall:
            Line(Point(self.x1, self.y1), Point(self.x2, self.y1), self.screen).draw_line()
        else:
            Line(Point(self.x1, self.y1), Point(self.x2, self.y1), self.screen).draw_line("black")
        if self.has_bottom_wall:
            Line(Point(self.x1, self.y2), Point(self.x2, self.y2), self.screen).draw_line()
        else:
             Line(Point(self.x1, self.y2), Point(self.x2, self.y2), self.screen).draw_line("black")
        if self.has_left_wall:
            Line(Point(self.x1, self.y1), Point(self.x1, self.y2), self.screen).draw_line()
        else:
             Line(Point(self.x1, self.y1), Point(self.x1, self.y2), self.screen).draw_line("black")
        if self.has_right_wall:
            Line(Point(self.x2, self.y1), Point(self.x2, self.y2), self.screen).draw_line()
        else:
            Line(Point(self.x2, self.y1), Point(self.x2, self.y2), self.screen).draw_line("black")
    

    def draw_move(self, other_cell, undo=False):
        x_center = (self.x1 + self.x2) // 2
        y_center = (self.y1 + self.y2) // 2

        x_center2 = (other_cell.x1 + other_cell.x2) // 2
        y_center2 = (other_cell.y1 + other_cell.y2) // 2

        fill_color = "red"
        if undo:
            fill_color = "black"

        Line(Point(x_center, y_center), Point(x_center2, y_center2), self.screen).draw_line(fill_color)