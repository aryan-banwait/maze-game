import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def move(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= 15
        if keys[pygame.K_s]:
            self.rect.y += 15
        if keys[pygame.K_a]:
            self.rect.x -= 15
        if keys[pygame.K_d]:
            self.rect.x += 15

    
    def out_of_screen(self):
        if self.rect.y > 720 - self.image.get_height():
            self.rect.y = 720 - self.image.get_height()
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > 1280 - self.image.get_width():
            self.rect.x = 1280 - self.image.get_width()
        if self.rect.x < 0:
            self.rect.x = 0
   
    
    
    