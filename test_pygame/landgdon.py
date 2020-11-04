import pygame as pg
from time import  time

class App:
    def __init__(self, WIDTH=1000, HEIGT=700, CELL_SIZE=12):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGT])
        self.cloock = pg.time.Clock

        self.CRLL_SIZE = CELL_SIZE
        self.ROWS, self.COLS = HEIGT // CELL_SIZE, WIDTH // CELL_SIZE
        self.grid = [[0 for col in range(self.COLS)] for row in range(self.ROWS)]

    def run(self):
        while True:
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.cloock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
