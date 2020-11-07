import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(center=(W // 2, H // 2))

sc.fill(WHITE)
sc.blit(hero, (rect))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)
