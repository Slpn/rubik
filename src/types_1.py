from enum import Enum
from typing import ForwardRef


class Color(Enum):
    WHITE = 'white'
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'
    ORANGE = 'orange'


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    FRONT = 'front'
    BOTTOM = 'bottom'


Edge = list[Color]


Edges = dict[Direction, ForwardRef('Slice')]
