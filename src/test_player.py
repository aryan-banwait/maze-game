import pygame, os, sys
from player import Player

os.environ['SDL_AUDIODRIVER'] = 'dummy'
pygame.init()

running = True
screen_size = (width, height) = (1280, 720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
bg_color = "black"
hero = Player("media/hero.png", 0, 0) 
while running:
    #TERMINATION LOGIC
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #GAME LOGIC PRE INPUT
    screen.fill(bg_color)
    keys = pygame.key.get_pressed()

    #PLAYER LOGIC
    screen.blit(hero.image, hero.rect.topleft)
    hero.move(keys)
    hero.out_of_screen()

    #END LOGIC
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
