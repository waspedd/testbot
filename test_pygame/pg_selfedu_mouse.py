import pygame as pg

pg.init()

W = 600
H = 400

sc = pg.display.set_mode((W, H), pg.DOUBLEBUF | pg.RESIZABLE | pg.SCALED)  # создал окно программы, добавил бафы
pg.display.set_caption('событие от мыши')  # изменил название окна

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

FPS = 60
clock = pg.time.Clock()

sp = None
sc.fill(WHITE)
pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        pressed = pg.mouse.get_pressed()
        if pressed[0]:
            pos = pg.mouse.get_pos()

            if sp is None:
                sp = pos

            w = pos[0] - sp[0]
            h = pos[1] - sp[1]

            sc.fill(WHITE)
            pg.draw.rect(sc, RED, (sp[0], sp[1], w, h))
            pg.display.update()
        else:
            sp = None


    clock.tick(FPS)
