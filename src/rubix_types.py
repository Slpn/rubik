from enum import Enum


class Faces(Enum):
    UP = 'Up'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'
    FRONT = 'Front'
    BOTTOM = 'Bottom'


moves = ['U', 'D', 'F', 'B', 'L', 'R', ]


color_codes = {
    'R': '\033[41m',
    'G': '\033[42m',
    'Y':  '\33[43m',
    'B': "\033[44m",
    'O': '\033[48;2;255;165;0m',
    'W': '\33[47m',
    'RESET': "\033[0m"


}
