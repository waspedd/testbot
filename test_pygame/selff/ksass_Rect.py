import pygame  # подключение библиотеки

pygame.init()  # инициализация библиотеки

W = 600  # ввод переменных отвечающих за разрешение
H = 400

sc = pygame.display.set_mode((W, H))  # инициализация окна с указанным разрешением
# и доп ф-ии.

WHITE = (255, 255, 255)  # определение цветов импользуемых в программе
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 60  # присвоение переменной отвечающей за фпс
clock = pygame.time.Clock()  # опрп

ground = H - 70
jump_force = 20
move = jump_force + 1

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx=W // 2)
rect.bottom = ground

while True:
    for event in pygame.event.get():  # главный цикл с проверкой на определенное событие
        if event.type == pygame.QUIT:  # если событие == выход
            exit()  # выходим из программы

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force

    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
            else:
                rect.bottom = ground
                move = jump_force+1

    sc.fill(WHITE)
    sc.blit(hero, rect)
    pygame.display.update()

    clock.tick(FPS)
