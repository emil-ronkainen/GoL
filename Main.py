import pygame, sys
from Map import Map
from Consts import Consts as C

class Main:

    def __init__(self):
        self.map = Map()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(C.SIZE)

    def main(self):
        # self.map.debug_print_state()
        pass

    def start(self):
        while 1:
            self.clock.tick(C.TICKRATE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                #if event.type == pygame.KEYDOWN:

            self.update()
            self.draw()

    def update(self):
        for row in self.map.positions:
            for cell in row:
                cell.update(self.map.count_neighbours(cell.row, cell.col))

    def draw(self):
        self.screen.fill(C.LIGHT_GRAY)
        self.map.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    main = Main()

    main.main()
    main.start()
