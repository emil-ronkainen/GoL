import pygame
from Consts import Consts as C
from Cell import Cell, State

class Map:

    def __init__(self):
        self.positions = []

        for r in range(int(C.WIDTH / C.SQUARE_SIZE)):
            row = []
            for c in range(int(C.HEIGHT / C.SQUARE_SIZE)):
                row.append(Cell(r, c))
            self.positions.append(row)

    def count_neighbours(self, row, col):
        nbr = 0
        for r in range(max(0, row - 1), min(len(self.positions) - 1, row + 2)):
            for c in range(max(0, col - 1), min(len(self.positions[row]) - 1, col + 2)):
                if self.positions[r][c].state is State.ALIVE:
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