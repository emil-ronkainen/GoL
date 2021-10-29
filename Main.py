import pygame, sys, math
from Map import Map
from Consts import Consts as C

from DebugCell import DebugCell
from Cell import Cell

class Main:

    def __init__(self):
        self.map = Map(True, False)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(C.SIZE)
        self.toggled = True
        self.debug = False

    def main(self):
        # self.map.debug_print_state()
        pass

    def start(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.toggled = not self.toggled
                    elif event.key == pygame.K_r: # Reset state
                        self.map = Map(True, self.debug)
                        self.update()
                        self.draw()
                    elif event.key == pygame.K_c: # Clear board
                        self.map.clear(self.debug)
                        self.update()
                        self.draw()
                    elif event.key == pygame.K_v: # Toggle debug
                        self.debug = not self.debug
                        self.map.toggle_debug(self.debug)
                        self.draw()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = self.convert_to_coords(event.pos)
                    self.map.positions[pos[0]][pos[1]].toggle()
                    self.draw()

            if self.toggled:
                self.clock.tick(C.TICKRATE)

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

    def convert_to_coords(self, event_pos):
        x = math.floor(event_pos[0] / C.SQUARE_SIZE)
        y = math.floor(event_pos[1] / C.SQUARE_SIZE)
        return (x, y)

if __name__ == '__main__':
    main = Main()

    main.main()
    main.start()
