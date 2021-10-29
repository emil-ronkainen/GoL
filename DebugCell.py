import pygame

from pygame import Rect
from Cell import Cell, State
from Consts import Consts as C

class DebugCell(Cell):

    def __init__(self, row, col, state):
        super().__init__(row, col, state)

    def update(self, neighbours):
        if self.state is State.ALIVE and not 2 <= neighbours <= 3:
            self.state = State.DYING
        elif self.state is State.DEAD and neighbours == 3:
            self.state = State.BIRTH
        elif self.state is State.DYING:
            self.state = State.DEAD
        elif self.state is State.BIRTH:
            self.state = State.ALIVE

    def draw(self, screen):
        rect = pygame.Rect(self.row * C.SQUARE_SIZE, self.col * C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)
        color = C.BLACK

        if self.state is State.ALIVE:
            color = C.GREEN
        elif self.state is State.DYING:
            color = C.DARK_GRAY
        elif self.state is State.BIRTH:
            color = C.RED

        pygame.draw.rect(screen, color, rect)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()
