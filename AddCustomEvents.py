import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Color Change Example")

class ColoredSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def update(self):
        self.image.fill(self.color)

sprites = pygame.sprite.Group()
sprite1 = ColoredSprite((255, 0, 0), 50, 50)
sprite1.rect.topleft = (100, 100)
sprites.add(sprite1)

sprite2 = ColoredSprite((0, 0, 255), 50, 50)
sprite2.rect.topleft = (300, 100)
sprites.add(sprite2)

def change_sprite_colors():
    for sprite in sprites:
        sprite.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
clock = pygame.time.Clock()
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            change_sprite_colors()

    sprites.update()
    screen.fill((255, 255, 255))
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()