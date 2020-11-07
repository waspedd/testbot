import pygame as pg

pg.init()

W = 600
H = 400

sc = pg.display.set_mode((W, H))#, pg.SCALED | pg.DOUBLEBUF | pg.RESIZABLE)
#pg.display.set_caption('<(^_^)>')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 60

clock = pg.time.Clock()

surf = pg.Surface((W, 200))
bita = pg.Surface((50, 10))

surf.fill(BLUE)
bita.fill(RED)

bx, by = 0, 150
x, y = 0, 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        surf.fill(BLUE)
        surf.blit(bita, (bx, by))
        if bx < H:
            bx += 5
        else:
            bx = 0

        if y < H:
            y += 1
        else:
            y = 0

        sc.fill(WHITE)
        sc.blit(surf, (x, y))
        pg.display.update()

    clock.tick(FPS)
