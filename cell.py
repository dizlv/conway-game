from enum import Enum
from collections import namedtuple

RelativeCell = namedtuple('RelativeCell', ['delta_x', 'delta_y'])


class Offset(Enum):
    NORTH_WEST = RelativeCell(-1, -1)
    NORTH = RelativeCell(0, -1)
    NORTH_EAST = RelativeCell(1, -1)
    EAST = RelativeCell(1, 0)
    SOUTH_EAST = RelativeCell(1, 1)
    SOUTH = RelativeCell(0, 1)
    SOUTH_WEST = RelativeCell(-1, 1)
    WEST = RelativeCell(-1, 0)


class CellState(Enum):
    DEAD = 0
    LIVE = 1


class Cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y

        self.state = state

    def __repr__(self):
        return str(self.state.value)
