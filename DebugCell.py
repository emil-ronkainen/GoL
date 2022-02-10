import pygame

from pygame import Rect
from Cell import Cell, State
from Consts import Consts as C

class DebugCell(Cell):

    def __init__(self, row, col, state):
        super().__init__(row, col, state)
        self.previous_state = state


    def draw(self, screen):
        rect = pygame.Rect(self.row * C.SQUARE_SIZE, self.col * C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)
        color = C.BLACK

        if self.state is State.ALIVE and self.previous_state == State.DEAD:
            color = C.RED
        elif self.state is State.DEAD and self.previous_state == State.ALIVE:
            color = C.DARK_GRAY
        elif self.state is State.ALIVE:
            color = C.GREEN

        self.previous_state = self.state
        pygame.draw.rect(screen, color, rect)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()
