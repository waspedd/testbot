import pygame
import random

WIDTH = 400
HEIGHT = 600
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Playar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


pygame.init()
# команда запускает pygame

pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
''' создает окно программы размер который мы
 указали в настройках до запуска'''

pygame.display.set_caption('mu first game')
clock = pygame.time.Clock()
# clock что бы убедится в правельной скорости

all_sprites = pygame.sprite.Group()
playar = Playar()
all_sprites.add(playar)

running = True  # цикл игры
while running:
    # процесс ввода
    # обновление
    # визуализация
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
