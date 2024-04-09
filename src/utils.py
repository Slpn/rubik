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
        "+": "R",
        "-": "R'",
        "opposite": 'R2'
    },
    "Left": {
        "+": "L",
        "-": "L'",
        "opposite": 'L2'
    },
    "Front": {
        "+": "F",
        "-": "F'",
        "opposite": 'F2'
    },
    "Bottom": {
        "+": "B",
        "-": "B'",
        "opposite": 'B2'
    },
    "Up": {
        "+": "U",
        "-": "U'",
        "opposite": 'U2'
    },
    "Down": {
        "+": "D",
        "-": "D'",
        "opposite": 'D2'
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
