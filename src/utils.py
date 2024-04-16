from enum import Enum


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

mouves_dir = {
    "Right": {
        "opposite": 'R2',
        "+": "R",
        "-": "R'",
    },
    "Left": {
        "opposite": 'L2',
        "+": "L",
        "-": "L'",
    },
    "Front": {
        "opposite": 'F2',
        "+": "F",
        "-": "F'",
    },
    "Bottom": {
        "opposite": 'B2',
        "+": "B",
        "-": "B'",
    },
    "Up": {
        "opposite": 'U2',
        "+": "U",
        "-": "U'",
    },
    "Down": {
        "opposite": 'D2',
        "+": "D",
        "-": "D'",
    },


}


def get_face_to_mouve(from_face: str, index: tuple):
    i, j = index[0], index[1]
    match from_face:
        case 'Up' | 'Down':
            if i == 2:
                to_mouve = 'Front' if from_face == 'Up' else 'Bottom'
            elif i == 0:
                to_mouve = 'Bottom' if from_face == 'Up' else 'Front'
            else:
                to_mouve = "Left" if j == 0 else 'Right'

        case 'Bottom' | 'Front':
            if i == 2:
                to_mouve = 'Down'
            elif i == 0:
                to_mouve = 'Up'
            else:
                if from_face == 'Front':
                    to_mouve = "Left" if j == 0 else 'Right'
                else:
                    to_mouve = "Left" if j == 2 else 'Right'

        case 'Left' | 'Right':
            if i == 2:
                to_mouve = 'Down'
            elif i == 0:
                to_mouve = 'Up'
            else:
                if from_face == 'Right':
                    to_mouve = 'Front' if j == 0 else 'Bottom'
                else:
                    to_mouve = 'Front' if j == 2 else 'Bottom'
    return to_mouve

# def get_9_cubes(color, first_edge, seconde_edge, third_edge, fourth_edge):
#     return np.array([
#         np.array([
#             Cube('corner', main=color,
#                     edge=fourth_edge, corner=first_edge),
#             Cube('edge', main=color,  edge=first_edge),
#             Cube('corner', main=color,
#                     edge=first_edge, corner=seconde_edge)
#         ]),
#         np.array([
#             Cube('edge', main=color, edge=fourth_edge),
#             Cube('center', main=color),
#             Cube('edge', main=color, edge=seconde_edge)
#         ]),
#         np.array([
#             Cube('corner', main=color,
#                     edge=third_edge, corner=fourth_edge),
#             Cube('edge', main=color, edge=third_edge),
#             Cube('corner', main=color,
#                     edge=seconde_edge, corner=third_edge)
#         ]),

#     ])


#  return {
#             'Up': get_9_cubes('W', first_edge='B', seconde_edge='R', third_edge='G', fourth_edge='O'),
#             'Down': get_9_cubes('Y', first_edge='G', seconde_edge='R', third_edge='B', fourth_edge='O'),
#             'Front': get_9_cubes('G', first_edge='W', seconde_edge='R', third_edge='Y', fourth_edge='O'),
#             'Bottom': get_9_cubes('B', first_edge='W', seconde_edge='R', third_edge='Y', fourth_edge='O'),
#             'Left': get_9_cubes('O', first_edge='W', seconde_edge='G', third_edge='Y', fourth_edge='B'),
#             'Right': get_9_cubes('R', first_edge='W', seconde_edge='B', third_edge='Y', fourth_edge='G'),
#         }


class Node:
    def __init__(self, value):
        self.value: any = value
        self.next: Node = None

    def __getitem_index__(self, key: int):
        iter_node = self
        if (key >= 0):
            for _ in range(key):
                iter_node = iter_node.next
            return iter_node
        else:
            for _ in range(4):
                if iter_node.__getitem_index__(-key) == self:
                    return iter_node
                iter_node = iter_node.next

    def __getitem__(self, key: str):
        if (type(key) == int):
            return self.__getitem_index__(key)
        iter_node = self
        while iter_node.next != self:
            if iter_node.value == key:
                break
            iter_node = iter_node.next
        return iter_node


class CircularChainedList:
    def __init__(self):
        self.head_node: Node = None

    def __init__(self, elem_lst: list):
        self.head_node: Node = None
        for elem in elem_lst:
            self.add_elem(elem)

    def add_elem(self, value):
        new_node = Node(value)
        if self.head_node is None:
            self.head_node = new_node
            new_node.next = self.head_node
        else:
            iter_node = self.head_node
            while iter_node.next != self.head_node:
                iter_node = iter_node.next
            new_node.next = self.head_node
            iter_node.next = new_node


def get_new_idx(idx: tuple, sense: str):
    i, j = None, None
    match sense:
        case '+':
            i = idx[1]
            j = 2 - idx[0]

        case '-':
            i = 2 - idx[1]
            j = idx[0]

        case 'opposite':
            i = 2 - idx[0]
            j = 2 - idx[1]
    return (i, j)