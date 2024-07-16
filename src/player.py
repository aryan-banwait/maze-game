import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, size):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def move(self, keys, maze):
        move_x, move_y = 0, 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move_y = -5
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move_y = 5
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move_x = -5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move_x = 5

        if not self.check_collision(move_x, move_y, maze):
            self.rect.x += move_x
            self.rect.y += move_y
        self.out_of_screen()

    def check_collision(self, move_x, move_y, maze):
        future_rect = self.rect.move(move_x, move_y)
        for col in maze.cells:
            for cell in col:
                if cell.has_top_wall and future_rect.colliderect(pygame.Rect(cell.x1, cell.y1, cell.x2 - cell.x1, 2)):
                    return True
                if cell.has_bottom_wall and future_rect.colliderect(pygame.Rect(cell.x1, cell.y2, cell.x2 - cell.x1, 2)):
                    return True
                if cell.has_left_wall and future_rect.colliderect(pygame.Rect(cell.x1, cell.y1, 2, cell.y2 - cell.y1)):
                    return True
                if cell.has_right_wall and future_rect.colliderect(pygame.Rect(cell.x2, cell.y1, 2, cell.y2 - cell.y1)):
                    return True
        return False

    def out_of_screen(self): 
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h

        if self.rect.y > screen_height - self.image.get_height():
            self.rect.y =  screen_height - self.image.get_height()
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > screen_width - self.image.get_width():
            self.rect.x = screen_width - self.image.get_width()
        if self.rect.x < 0:
            self.rect.x = 0
   
    
        
    
    