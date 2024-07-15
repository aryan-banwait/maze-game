import pygame

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
        


    
    
    

    