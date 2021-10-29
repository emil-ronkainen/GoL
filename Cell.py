import random, pygame
from enum import Enum, auto
from Consts import Consts as C

class State(Enum):
    DEAD = auto()
    ALIVE = auto()
    BIRTH = auto()
    DYING = auto()

class Cell(object):

    def __init__(self, row, col, state):
        self.state = state
        self.row = row
        self.col = col

    def __str__(self):
        return str((self.row, self.col))

    def __repr__(self):
        return self.__str__()

    def update(self, neighbours):
        if self.state is State.ALIVE and not 2 <= neighbours <= 3:
            self.state = State.DEAD
        elif self.state is State.DEAD and neighbours == 3:
            self.state = State.ALIVE

    def draw(self, screen):
        rect = pygame.Rect(self.row * C.SQUARE_SIZE, self.col * C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)
        color = C.BLACK
        if self.state is State.ALIVE:
            color = C.GREEN
        pygame.draw.rect(screen, color, rect)

    def toggle(self):
        if self.state is State.ALIVE:
            self.state = State.DEAD
        else: # Only if State is State.DEAD
            self.state = State.ALIVE
