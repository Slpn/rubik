import copy
from enum import Enum
from typing import ForwardRef, NamedTuple
import numpy as np


class Faces_Dir(Enum):
    UP = 'Up'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'
    FRONT = 'Front'
    BOTTOM = 'Bottom'


Face = ForwardRef('Face')


class Edge(NamedTuple):
    face: Face
    index: tuple
    color: str


class Corner(NamedTuple):
    corner: Edge
    corner_i: Edge
    corner_j: Edge


dir_nodes = {
    'Bottom': {
        'Down': 'up',
        'Up': 'down',
        'Left': 'left',
        'Right': 'right'
    },
    'Down': {
        'Front': 'up',
        'Bottom': 'down',
        'Left': 'left',
        'Right': 'right'
    },
    'Front': {
        'Up': 'up',
        'Down': 'down',
        'Left': 'left',
        'Right': 'right'
    },
    'Left': {
        'Up': 'up',
        'Down': 'down',
        'Bottom': 'left',
        'Front': 'right'
    },
    'Right': {
        'Up': 'up',
        'Down': 'down',
        'Front': 'left',
        'Bottom': 'right'
    },
    'Up': {
        'Bottom': 'up',
        'Front': 'down',
        'Left': 'left',
        'Right': 'right'
    }
}


class Face():

    def __init__(self, dir:  Faces_Dir) -> None:
        self.dir = dir
        match dir:
            case 'Up':
                self.array = np.full((3, 3), 'W')
                self.color = 'W'
            case 'Down':
                self.array = np.full((3, 3), 'Y')
                self.color = 'Y'
            case 'Front':
                self.array = np.full((3, 3), 'G')
                self.color = 'G'
            case 'Bottom':
                self.array = np.full((3, 3), 'B')
                self.color = 'B'
            case 'Left':
                self.array = np.full((3, 3), 'O')
                self.color = 'O'
            case 'Right':
                self.array = np.full((3, 3), 'R')
                self.color = 'R'

    def __getitem__(self, key: tuple):
        return self.array[key[0]][key[1]]

    def get_edge(self, index: tuple, rubix) -> Edge:
        res_i, res_j = None, None
        i, j = index[0], index[1]
        face = None
        dir = self.dir
        match dir:
            case 'Down' | "Up":
                res_i, res_j = 2 if dir == "Down" else 0, 1
                if (i == 0 and j == 1):
                    face = rubix.cube["Front"] if dir == "Down" else rubix.cube["Bottom"]
                elif (i == 1 and j == 0):
                    face = rubix.cube["Left"]
                elif (i == 1 and j == 2):
                    face = rubix.cube["Right"]
                elif (i == 2 and j == 1):
                    face = rubix.cube["Bottom"] if dir == "Down" else rubix.cube["Front"]
                else:
                    raise Exception(
                        f"Face {dir} at index {(i, j)} is not an edge")
            case 'Front' | "Bottom":
                if (i == 0 and j == 1):
                    face = rubix.cube["Up"]
                    res_i, res_j = 2 if dir == "Front" else 0, 1
                elif (i == 1 and j == 0):
                    face = rubix.cube["Left"] if dir == "Front" else rubix.cube["Right"]
                    res_i, res_j = 1, 2
                elif (i == 1 and j == 2):
                    face = rubix.cube["Left"] if dir == "Bottom" else rubix.cube["Right"]
                    res_i, res_j = 1, 0
                elif (i == 2 and j == 1):
                    face = rubix.cube["Down"]
                    res_i, res_j = 0 if dir == "Front" else 2, 1
                else:
                    raise Exception(
                        f"Face {dir} at index {(i, j)} is not an edge")

            case 'Left' | "Right":
                if (i == 0 and j == 1):
                    face = rubix.cube["Up"]
                    res_i, res_j = 1, 0 if dir == "Left" else 2
                elif (i == 1 and j == 0):
                    face = rubix.cube["Bottom"] if dir == "Left" else rubix.cube["Front"]
                    res_i, res_j = 1, 2
                elif (i == 1 and j == 2):
                    face = rubix.cube["Bottom"] if dir == "Right" else rubix.cube["Front"]
                    res_i, res_j = 1, 0
                elif (i == 2 and j == 1):
                    face = rubix.cube["Down"]
                    res_i, res_j = 1, 0 if dir == "Left" else 2
                else:
                    raise Exception(
                        f"Face {dir} at index {(i, j)} is not an edge")

        return {"face": face, "index": (res_i, res_j), "color": face.array[res_i][res_j]}

    def get_4_edges_color(self, dir: Faces_Dir):
        match dir:
            case 'Down' | "Up":
                return ["O", "R", "B", "G"]
            case 'Front' | "Bottom":
                return ["O", "R", "Y", "W"]
            case 'Left' | "Right":
                return ["Y", "W", "B", "G"]
            case _:
                raise Exception('Bad face direction')

    def get_first_corner(self, index: tuple, rubix) -> Edge:
        res_i, res_j = None, None
        i, j = index[0], index[1]
        face = None
        dir = self.dir
        match dir:
            case "Up":
                face = rubix.cube["Bottom"] if i == 0 else rubix.cube["Front"]
                if i == 0 and j == 0:
                    res_i, res_j = 0, 2
                elif i == 0 and j == 2:
                    res_i, res_j = 0, 0
                elif i == 2 and j == 0:
                    res_i, res_j = 0, 0
                elif i == 2 and j == 2:
                    res_i, res_j = 0, 2
            case "Down":
                face = rubix.cube["Front"] if i == 0 else rubix.cube["Bottom"]
                if i == 0 and j == 0:
                    res_i, res_j = 2, 0
                elif i == 0 and j == 2:
                    res_i, res_j = 2, 2
                elif i == 2 and j == 0:
                    res_i, res_j = 2, 2
                elif i == 2 and j == 2:
                    res_i, res_j = 2, 0
            case "Front":
                face = rubix.cube["Up"] if i == 0 else rubix.cube["Down"]
                if i == 0 and j == 0:
                    res_i, res_j = 2, 0
                elif i == 0 and j == 2:
                    res_i, res_j = 2, 2
                elif i == 2 and j == 0:
                    res_i, res_j = 0, 0
                elif i == 2 and j == 2:
                    res_i, res_j = 0, 2
            case "Bottom":
                face = rubix.cube["Up"] if i == 0 else rubix.cube["Down"]
                if i == 0 and j == 0:
                    res_i, res_j = 0, 2
                elif i == 0 and j == 2:
                    res_i, res_j = 0, 0
                elif i == 2 and j == 0:
                    res_i, res_j = 2, 2
                elif i == 2 and j == 2:
                    res_i, res_j = 2, 0
            case "Left":
                face = rubix.cube["Up"] if i == 0 else rubix.cube["Down"]
                if i == 0 and j == 0:
                    res_i, res_j = 0, 0
                elif i == 0 and j == 2:
                    res_i, res_j = 2, 0
                elif i == 2 and j == 0:
                    res_i, res_j = 2, 0
                elif i == 2 and j == 2:
                    res_i, res_j = 0, 0
            case "Right":
                face = rubix.cube["Up"] if i == 0 else rubix.cube["Down"]
                if i == 0 and j == 0:
                    res_i, res_j = 2, 2
                elif i == 0 and j == 2:
                    res_i, res_j = 0, 2
                elif i == 2 and j == 0:
                    res_i, res_j = 0, 2
                elif i == 2 and j == 2:
                    res_i, res_j = 2, 2
        if res_i == None or res_j == None:
            raise Exception(
                f"Face {dir} at index {(i, j)} is not a corner")

        return {"face": face, "index": (res_i, res_j), "color": face[(res_i, res_j)]}

    def get_second_corner(self, index: tuple, rubix) -> Edge:
        res_i, res_j = None, None
        i, j = index[0], index[1]
        face = None
        dir = self.dir
        match dir:
            case "Up":
                face = rubix.cube["Left"] if j == 0 else rubix.cube["Right"]
                if i == 0 and j == 0:
                    res_i, res_j = 0, 0
                elif i == 0 and j == 2:
                    res_i, res_j = 0, 2
                elif i == 2 and j == 0:
                    res_i, res_j = 0, 2
                elif i == 2 and j == 2:
                    res_i, res_j = 0, 0
            case "Down":
                face = rubix.cube["Left"] if j == 0 else rubix.cube["Right"]
                if i == 0 and j == 0:
                    res_i, res_j = 2, 2
                elif i == 0 and j == 2:
                    res_i, res_j = 2, 0
                elif i == 2 and j == 0:
                    res_i, res_j = 2, 0
                elif i == 2 and j == 2:
                    res_i, res_j = 2, 2
            case "Front":
                face = rubix.cube["Left"] if j == 0 else rubix.cube["Right"]
                if i == 0 and j == 0:
                    res_i, res_j = 0, 2
                elif i == 0 and j == 2:
                    res_i, res_j = 0, 0
                elif i == 2 and j == 0:
                    res_i, res_j = 2, 2
                elif i == 2 and j == 2:
                    res_i, res_j = 2, 0
            case "Bottom":
                face = rubix.cube["Left"] if j == 2 else rubix.cube["Right"]
                if i == 0 and j == 0:
                    res_i, res_j = 0, 2
                elif i == 0 and j == 2:
                    res_i, res_j = 0, 0
                elif i == 2 and j == 0:
                    res_i, res_j = 2, 2
                elif i == 2 and j == 2:
                    res_i, res_j = 2, 0
            case "Left":
                face = rubix.cube["Bottom"] if j == 0 else rubix.cube["Front"]
                if i == 0 and j == 0:
                    res_i, res_j = 0, 2
                elif i == 0 and j == 2:
                    res_i, res_j = 0, 0
                elif i == 2 and j == 0:
                    res_i, res_j = 2, 2
                elif i == 2 and j == 2:
                    res_i, res_j = 2, 0
            case "Right":
                face = rubix.cube["Front"] if j == 0 else rubix.cube["Bottom"]
                if i == 0 and j == 0:
                    res_i, res_j = 0, 2
                elif i == 0 and j == 2:
                    res_i, res_j = 0, 0
                elif i == 2 and j == 0:
                    res_i, res_j = 2, 2
                elif i == 2 and j == 2:
                    res_i, res_j = 2, 0
        if i == None or j == None:
            raise Exception(
                f"Face {dir} at index {(i, j)} is not a corner")

        return {"face": face, "index": (res_i, res_j), "color": face[(res_i, res_j)]}

    def get_corners(self, index: tuple, rubix) -> Corner:
        first_corner = self.get_first_corner(index, rubix)
        second_corner = self.get_second_corner(index, rubix)
        return {
            "corner": {
                "face": self,
                "index": index,
                "color": self[index]
            },
            "corner_i": first_corner,
            "corner_j": second_corner
        }

    # def __setattr__(self, other: Face) -> Face:
    #     other.array = copy.copy(self.array)
    #     other.color = self.color
    #     other.dir = self.dir
    #     return other

    def __deepcopy__(self, other):
        other = Face(self.dir)
        other.array = copy.deepcopy(self.array)
        other.color = self.color
        return other


def check_edge_color(face: Face, idx: tuple, rubix) -> bool:
    edge = face.get_edge(idx, rubix)
    if (edge['face'].color != edge["color"]):
        return False
    return True
