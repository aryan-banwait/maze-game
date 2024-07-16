import pygame


class Button:
    def __init__(self, x, y, width, height, text, font_type, font_size, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font_type = font_type
        self.font_size = font_size
        self.color = color    
        self.hover_color = hover_color
        


    def draw(self, screen, text_color):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=30)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=30)
        
        text_surface = pygame.font.Font(self.font_type, self.font_size).render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    
    def check_click(self, fnc):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and fnc:
                fnc()


def timer_display(screen, x, y, start_time, started_solving, reached_end):

    if not reached_end and not started_solving:
        text_surface = pygame.font.Font(None, 36).render(f"time: 0s", True, "white")
        screen.blit(text_surface, (x, y))
        return
    
    if not reached_end and started_solving:
        solving_time = (pygame.time.get_ticks() - start_time) // 1000
        text_surface = pygame.font.Font(None, 36).render(f"time: {solving_time}s", True, "white")
        screen.blit(text_surface, (x, y))
        return
    
    if reached_end:
        solved_time = (pygame.time.get_ticks() - start_time) // 1000
        text_surface = pygame.font.Font(None, 36).render(f"time: {solved_time}s", True, "white")
        screen.blit(text_surface, (x, y))
        return solved_time
    

def text_display(screen, x, y, text, font_size):
    text_surface = pygame.font.Font(None, font_size).render(text, True, "white")
    screen.blit(text_surface, (x, y))
    return
    




    
    
    

    