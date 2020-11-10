import pygame as pg

pg.init()

heigt = 500
width = 500

sc = pg.display.set_mode((heigt, width), pg.DOUBLEBUF | pg.RESIZABLE)

pg.display.set_caption('test_game')

WalkRight = [pg.image.load('right_1.png'), pg.image.load('right_2.png'),
             pg.image.load('right_3.png'), pg.image.load('right_4.png'),
             pg.image.load('right_5.png'), pg.image.load('right_6.png')]

WalkLeft = [pg.image.load('left_1.png'), pg.image.load('left_2.png'),
            pg.image.load('left_3.png'), pg.image.load('left_4.png'),
            pg.image.load('left_5.png'), pg.image.load('left_6.png')]

bg = pg.image.load('bg.jpg')
playerStand = pg.image.load('idle.png')

x = 50
y = 425
pers_heigt = 60
pers_width = 71
pers_speed = 5
isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = 'right'

clock = pg.time.Clock()
FPS = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class snaryad():
    def __init__(self, x, y, radius, color, facting):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facting = facting
        self.vel = 8 * facting

    def draw(self, sc):
        pg.draw.circle(sc, self.color, (self.x, self.y), self.radius)


def drawWindow():
    global animCount
    sc.blit(bg, (0, 0))  # после каждого события перерисовывает фон указанным цветом

    if animCount + 1 >= 50:
        animCount = 0

    if left:
        sc.blit(WalkLeft[animCount // 10], (x, y))
        animCount += 1
    elif right:
        sc.blit(WalkRight[animCount // 10], (x, y))
        animCount += 1
    else:
        sc.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(sc)

    pg.display.update()


run = True
bullets = []
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pg.key.get_pressed()

    if keys[pg.K_f]:
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(snaryad(round(x + pers_width // 2),
                                   round(y + pers_heigt // 2),
                                   5, RED, facing))

    if keys[pg.K_LEFT] and x > 5:
        x -= pers_speed  # в кейс поместили все нажатые кнопки
        left = True
        right = False
        lastMove = 'left'
    elif keys[pg.K_RIGHT] and x < 500 - pers_width - 5:  # выбор событий из кейс
        x += pers_speed  # и присвоение им новых координатов
        left = False
        right = True
        lastMove = 'right'

    else:
        left = False
        right = False
        animCount = 0
    if not isJump:
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
    drawWindow()
    clock.tick(FPS)
