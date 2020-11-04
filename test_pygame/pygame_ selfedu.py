import pygame as pg

pg.init()

W = 800
H = 600

sc = pg.display.set_mode((W, H), pg.RESIZABLE | pg.SCALED | pg.DOUBLEBUF)
pg.display.set_caption('моя вторая программа на PyGame')

color = (150, 100, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# pg.draw.rect(sc, color, (20, 10, 50, 100))
''' B draw.rect цвет    прописывается в формате RGB
                размеры (начало координат(х,у), высота, ширина))
                толщина линии (для отрисовки незакрашенного примитива),
'''
pg.display.update()

clock = pg.time.Clock()
FPS = 100

x = W // 2
y = H // 2
speed = 5

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        x -= speed
    elif keys[pg.K_RIGHT]:
        x += speed
    elif keys[pg.K_UP]:
        y -= speed
    elif keys[pg.K_DOWN]:
        y += speed

    sc.fill(WHITE)
    # pg.draw.rect(sc, BLUE, (x, y, 50, 50)) #квадрат размером 50 на 50
    pg.draw.circle(sc, GREEN, [x,y], (25)) #круг радиусом 25

    pg.display.update()

    clock.tick(FPS)  # fps
