import pygame as pg

pg.init()

heigt = 400
width = 600

sc = pg.display.set_mode((heigt, width), pg.DOUBLEBUF | pg.RESIZABLE )

pg.display.set_caption('test_game')

x = 50
y = 50
pers_heigt = 40
pers_width = 40
pers_speed = 5
isJump = False
jumpCount = 10

clock = pg.time.Clock()
FPS = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > 5:
        x -= pers_speed  # в кейс поместили все нажатые кнопки
    if keys[pg.K_RIGHT] and x < 400 - pers_width - 5:  # выбор событий из кейс
        x += pers_speed  # и присвоение им новых координатов
    if not isJump:
        if keys[pg.K_UP] and y > 5:
            y -= pers_speed
        if keys[pg.K_DOWN] and y < 600 - pers_heigt - 5:
            y += pers_speed
        if keys[pg.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    sc.fill(WHITE)  # после каждого события перерисовывает фон указанным цветом
    pg.draw.rect(sc, BLUE, (x, y, pers_width, pers_heigt))

    pg.display.update()
    clock.tick(FPS)
