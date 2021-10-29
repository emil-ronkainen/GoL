import pygame, random
from Consts import Consts as C
from Cell import Cell, State
from DebugCell import DebugCell

class Map:

    def __init__(self, is_random, toggle_debug):
        self.generate_cells(is_random, toggle_debug)

    def count_neighbours(self, row, col):
        nbr = 0
        for r in range(max(0, row - 1), min(len(self.positions) - 1, row + 2)):
            for c in range(max(0, col - 1), min(len(self.positions[row]) - 1, col + 2)):
                if (r, c) == (row, col):
                    continue
                if self.positions[r][c].state is State.ALIVE or self.positions[r][c].state is State.DYING:
                    nbr += 1
        return nbr

    def draw(self, screen):
        for row in self.positions:
            for cell in row:
                cell.draw(screen)

        # Grid drawing
        for x in range(0, C.WIDTH, C.SQUARE_SIZE):
            for y in range(0, C.HEIGHT, C.SQUARE_SIZE):
                rect = pygame.Rect(x, y, C.SQUARE_SIZE, C.SQUARE_SIZE)
                pygame.draw.rect(screen, C.LIGHT_GRAY, rect, 1)

    def clear(self, is_debug):
        self.generate_cells(False, False)


    def generate_cells(self, is_random, is_debug):
        self.positions = []

        for r in range(int(C.WIDTH / C.SQUARE_SIZE)):
            row = []
            for c in range(int(C.HEIGHT / C.SQUARE_SIZE)):
                new_cell = Cell(r, c, State.DEAD)

                if random.randrange(0, C.SPAWN_MAX) > C.SPAWN_CUTOFF and is_random:
                    new_cell.state = State.ALIVE

                row.append(new_cell)
            self.positions.append(row)

        if is_debug:
            self.toggle_debug(is_debug)

    def toggle_debug(self, debug):
        for r in range(int(C.WIDTH / C.SQUARE_SIZE)):
            for c in range(int(C.HEIGHT / C.SQUARE_SIZE)):
                if debug:
                    new_cell = DebugCell(r, c, self.positions[r][c].state)
                else:
                    new_cell = Cell(r, c, self.positions[r][c].state)

                self.positions[r][c] = new_cell

    def debug_print(self):
        for r in range(len(self.positions)):
            for c in range(len(self.positions[r])):
                print(self.positions[r][c], end=" ")
            print("\n==============")

    def debug_print_state(self):
        for r in range(len(self.positions)):
            for c in range(len(self.positions[r])):
                print(self.positions[r][c].state, end=" ")
            print("\n==============")
