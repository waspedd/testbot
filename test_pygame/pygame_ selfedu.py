import pygame
pygame.init()

sc = pygame.display.set_mode((600, 600), pygame.RESIZABLE | pygame.SCALED | pygame.DOUBLEBUF)
pygame.display.set_caption('моя вторая программа на PyGame')

color = (150, 100, 255)
GREEN = (0, 255, 0)


pygame.draw.lines(sc, color, True, [(280, 50), (300, 50), (400, 500)], 2)
pygame.draw.ellipse(sc, GREEN, (300, 300, 100, 100))
pygame.draw.line(sc, GREEN, (200, 50), (350, 100))
pygame.draw.rect(sc, color, (10, 10, 50, 100), 5)
''' B draw.rect цвет    прописывается в формате RGB
                размеры (начало координат(х,у), высота, ширина))
                толщина линии (для отрисовки незакрашенного примитива),
'''
pygame.display.update()

clock = pygame.time.Clock()
FPS = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS) #fps
