import copy
import time
from rubik_class import RubiksCube
from vizualize import RubixVisualiser


def apply_reversed_mouves(mouves: list[str], rubik: RubiksCube, visualiser: RubixVisualiser | None, visualise=False):
    for mouve in mouves:
        user_continue = ""
        while (visualise and visualiser and user_continue != "y"):
            user_continue = input("Tapez y pour le prochain mouv: ")
        rubik.mouves[inverse_mouves_dir[mouve]]()
        if visualiser:
            visualiser.visualizer_mouves[inverse_mouves_dir[mouve]]()
        if visualise and visualiser:
            time.sleep(visualiser.SPEED)


def apply_mouves(mouves: list[str], rubik: RubiksCube, visualiser: RubixVisualiser | None, visualise=False):
    for mouve in mouves:
        user_continue = ""
        while (visualise and visualiser and user_continue != "y"):
            user_continue = input("Tapez y pour le prochain mouv: ")
        rubik.mouves[mouve]()
        if (visualiser):
            visualiser.visualizer_mouves[mouve]()
            time.sleep(visualiser.SPEED)


def clear_mouves(rubik: RubiksCube):
    soluce_mouves = copy.copy(rubik.soluce_mouves)
    rubik.soluce_mouves = []
    i = 0
    while i <= len(soluce_mouves) - 1:
        equal = 1
        j = i
        while (j + 1 < len(soluce_mouves) and soluce_mouves[j + 1] == soluce_mouves[j]):
            equal += 1
            j += 1

        inverse = 1
        j = i
        while (j + 1 < len(soluce_mouves) and soluce_mouves[j + 1] == opposite_mouves[soluce_mouves[j]]):
            inverse += 1
            j += 1

        if (equal > 1):

            if equal % 2 == 0:
                if soluce_mouves[i][-1] == '2':
                    i += equal
                    pass
                else:
                    if equal % 4 == 0:
                        pass
                    else:
                        rubik.soluce_mouves.append(soluce_mouves[i][0] + '2')
                    i += equal
            elif equal % 2 == 1:
                if soluce_mouves[i][-1] == '2':
                    rubik.soluce_mouves.append(soluce_mouves[i])
                    i += equal
                else:
                    rubik.soluce_mouves.append(
                        opposite_mouves[soluce_mouves[i]])
                    i += equal

        elif inverse > 1:
            if inverse % 2 == 0:
                pass
                i += inverse
            elif inverse % 2 == 1:
                rubik.soluce_mouves.append(soluce_mouves[i])
                i += inverse

        else:
            rubik.soluce_mouves.append(soluce_mouves[i])
            i += 1


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


opposite_mouves = {
    "U": "U'",
    "U'": "U",
    "U2": "U2",

    "D": "D'",
    "D'": "D",
    "D2": "D2",

    "F": "F'",
    "F'": "F",
    "F2": "F2",

    "B": "B'",
    "B'": "B",
    "B2": "B2",

    "L": "L'",
    "L'": "L",
    "L2": "L2",

    "R": "R'",
    "R'": "R",
    "R2": "R2",

}


inverse_mouves_dir = {
    "U": "D'",
    "U'": "D",
    "U2": "D2",

    "D": "U'",
    "D'": "U",
    "D2": "U2",

    "F": "F'",
    "F'": "F",
    "F2": "F2",

    "B": "B'",
    "B'": "B",
    "B2": "B2",

    "L": "L'",
    "L'": "L",
    "L2": "L2",

    "R": "R'",
    "R'": "R",
    "R2": "R2",

}


y2_mouve_dir = {
    "U": "U",
    "U'": "U'",
    "U2": "U2",

    "D": "D",
    "D'": "D'",
    "D2": "D2",

    "F": "B",
    "F'": "B'",
    "F2": "B2",

    "B": "F",
    "B'": "F'",
    "B2": "F2",

    "L": "R",
    "L'": "R'",
    "L2": "R2",

    "R": "L",
    "R'": "L'",
    "R2": "L2",

}

y_mouves_dir = {
    "U": "U",
    "U'": "U'",
    "U2": "U2",

    "D": "D",
    "D'": "D'",
    "D2": "D2",

    "F": "R",
    "F'": "R'",
    "F2": "R2",

    "B": "L",
    "B'": "L'",
    "B2": "L2",

    "L": "F",
    "L'": "F'",
    "L2": "F2",

    "R": "B",
    "R'": "B'",
    "R2": "B2",

}


x_mouves_dir = {
    "U": "B",
    "U'": "B'",
    "U2": "B2",

    "D": "F",
    "D'": "F'",
    "D2": "F2",

    "F": "U",
    "F'": "U'",
    "F2": "U2",

    "B": "D",
    "B'": "D'",
    "B2": "D2",

    "L": "L",
    "L'": "L'",
    "L2": "L2",

    "R": "R",
    "R'": "R'",
    "R2": "R2",

}

x_prime_mouves_dir = {
    "U": "F",
    "U'": "F'",
    "U2": "F2",

    "D": "B",
    "D'": "B'",
    "D2": "B2",

    "F": "D",
    "F'": "D'",
    "F2": "D2",

    "B": "U",
    "B'": "U'",
    "B2": "U2",

    "L": "L",
    "L'": "L'",
    "L2": "L2",

    "R": "R",
    "R'": "R'",
    "R2": "R2",

}


y_prime_mouve_dir = {
    "U": "U",
    "U'": "U'",
    "U2": "U2",

    "D": "D",
    "D'": "D'",
    "D2": "D2",

    "F": "L",
    "F'": "L'",
    "F2": "L2",

    "B": "R",
    "B'": "R'",
    "B2": "R2",

    "L": "B",
    "L'": "B'",
    "L2": "B2",

    "R": "F",
    "R'": "F'",
    "R2": "F2",

}


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


def get_R_corner_top(idx: tuple):
    match idx:
        case (0, 0):
            return 'Front'
        case (0, 2):
            return 'Right'
        case (2, 0):
            return 'Left'
        case (2, 2):
            return 'Bottom'


def get_R_corner_Bottom(idx: tuple):
    match idx:
        case (0, 0):
            return 'Left'
        case (0, 2):
            return 'Front'
        case (2, 0):
            return 'Bottom'
        case (2, 2):
            return 'Right'


def get_R_corner_bottom(idx: tuple):
    match idx:
        case (0, 0):
            return 'Left'
        case (0, 2):
            return 'Bottom'
        case (2, 0):
            return 'Front'
        case (2, 2):
            return 'Right'


def get_F_corner_bottom(idx: tuple):
    match idx:
        case (0, 0):
            return 'Bottom'
        case (0, 2):
            return 'Right'
        case (2, 0):
            return 'Left'
        case (2, 2):
            return 'Front'


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
