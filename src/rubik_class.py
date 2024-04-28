
from utils import color_codes
from copy import copy
import numpy as np
from face_class import Face, Faces_Dir


class RubiksCube:

    def __init__(self):
        self.cube: dict[Faces_Dir, Face] = self.reset_cube()
        mouves = Mouves(self)
        self.mouves = mouves.mouves
        self.soluce_mouves = []

    def reset_cube(self):

        return {
            'Up': Face('Up'),
            'Down': Face('Down'),
            'Front': Face('Front'),
            'Bottom': Face('Bottom'),
            'Left': Face('Left'),
            'Right': Face('Right')
        }

    def get_edges_cpy(self, face: Face):
        top_edge, left_edge, down_edge, right_edge, front_edge, bottom_edge = None, None, None, None, None, None,
        dir = face.dir
        match dir:

            case 'Front' | 'Bottom':
                idx = 2 if dir == 'Front' else 0
                top_edge = copy(self.cube['Up'].array[idx])
                left_edge = copy([self.cube['Left'].array[i][idx]
                                  for i in range(3)])
                down_edge = copy(self.cube['Down'].array[2 - idx])
                right_edge = copy([self.cube['Right'].array[i][2 - idx]
                                   for i in range(3)])

            case 'Left' | 'Right':
                idx = 0 if dir == 'Left' else 2
                top_edge = copy([self.cube['Up'].array[i][idx]
                                 for i in range(3)])
                front_edge = copy([self.cube['Front'].array[i][idx]
                                   for i in range(3)])
                down_edge = copy([self.cube['Down'].array[i][idx]
                                  for i in range(3)])
                bottom_edge = copy([self.cube['Bottom'].array[i][2 - idx]
                                    for i in range(3)])

            case 'Up' | 'Down':
                idx = 0 if dir == 'Up' else 2
                left_edge = copy(self.cube["Left"].array[idx])
                front_edge = copy(self.cube["Front"].array[idx])
                right_edge = copy(self.cube["Right"].array[idx])
                bottom_edge = copy(self.cube["Bottom"].array[idx])

        return top_edge, left_edge, down_edge, right_edge, front_edge, bottom_edge

    def rotate_face_counterclockwise(self, face_dir: Faces_Dir):
        temp_top, temp_left, temp_down, temp_right, temp_front, temp_bottom = self.get_edges_cpy(
            self.cube[face_dir])
        self.cube[face_dir].array = np.rot90(self.cube[face_dir].array)

        match face_dir:

            case "Front":

                self.cube['Down'].array[0] = temp_left
                self.cube['Up'].array[2] = temp_right

                for i in range(3):
                    self.cube['Right'].array[i][0] = temp_down[2 - i]
                    self.cube['Left'].array[i][2] = temp_top[2 - i]

            case "Bottom":

                self.cube['Down'].array[2] = temp_right[::-1]
                self.cube['Up'].array[0] = temp_left[::-1]

                for i in range(3):
                    self.cube['Right'].array[i][2] = temp_top[i]
                    self.cube['Left'].array[i][0] = temp_down[i]

            case 'Left':
                for i in range(3):
                    self.cube['Down'].array[i][0] = temp_bottom[2 - i]
                    self.cube['Up'].array[i][0] = temp_front[i]
                    self.cube['Bottom'].array[i][2] = temp_top[2 - i]
                    self.cube['Front'].array[i][0] = temp_down[i]

            case 'Right':
                for i in range(3):
                    self.cube['Down'].array[i][2] = temp_front[i]
                    self.cube['Up'].array[i][2] = temp_bottom[2 - i]
                    self.cube['Bottom'].array[i][0] = temp_down[2 - i]
                    self.cube['Front'].array[i][2] = temp_top[i]

            case 'Up':
                self.cube['Left'].array[0] = temp_bottom
                self.cube['Right'].array[0] = temp_front
                self.cube['Bottom'].array[0] = temp_right
                self.cube['Front'].array[0] = temp_left

            case 'Down':
                self.cube['Left'].array[2] = temp_front
                self.cube['Right'].array[2] = temp_bottom
                self.cube['Bottom'].array[2] = temp_left
                self.cube['Front'].array[2] = temp_right

    def rotate_face_clockwise(self, face_dir: Faces_Dir):
        temp_top, temp_left, temp_down, temp_right, temp_front, temp_bottom = self.get_edges_cpy(
            self.cube[face_dir])

        self.cube[face_dir].array = np.rot90(self.cube[face_dir].array, k=-1)

        match face_dir:

            case 'Front':

                self.cube['Up'].array[2] = temp_left[::-1]
                self.cube['Down'].array[0] = temp_right[::-1]

                for i in range(3):
                    self.cube['Right'].array[i][0] = temp_top[i]
                    self.cube['Left'].array[i][2] = temp_down[i]

            case "Bottom":

                self.cube['Down'].array[2] = temp_left
                self.cube['Up'].array[0] = temp_right

                for i in range(3):
                    self.cube['Right'].array[i][2] = temp_down[2-i]
                    self.cube['Left'].array[i][0] = temp_top[2-i]

            case 'Left':
                for i in range(3):
                    self.cube['Down'].array[i][0] = temp_front[i]
                    self.cube['Up'].array[i][0] = temp_bottom[2 - i]
                    self.cube['Bottom'].array[i][2] = temp_down[2 - i]
                    self.cube['Front'].array[i][0] = temp_top[i]

            case 'Right':
                for i in range(3):
                    self.cube['Down'].array[i][2] = temp_bottom[2 - i]
                    self.cube['Up'].array[i][2] = temp_front[i]
                    self.cube['Bottom'].array[i][0] = temp_top[2 - i]
                    self.cube['Front'].array[i][2] = temp_down[i]

            case 'Up':

                self.cube['Left'].array[0] = temp_front
                self.cube['Right'].array[0] = temp_bottom
                self.cube['Bottom'].array[0] = temp_left
                self.cube['Front'].array[0] = temp_right

            case 'Down':
                self.cube['Left'].array[2] = temp_bottom
                self.cube['Right'].array[2] = temp_front
                self.cube['Bottom'].array[2] = temp_right
                self.cube['Front'].array[2] = temp_left

    def check_solved(self):
        for face in self.cube:
            for row in self.cube[face]:
                for color in row:
                    if color != row[0]:
                        return False
        return True

    def pretty_print(self):

        for i in range(3):
            print(' '*3)
            for j in range(3):
                print(color_codes[self.cube['Up'].array[i][j]],
                      self.cube['Up'].array[i][j],  color_codes['RESET'], end='',)
        print()
        print("F face surrounded by L, R, and B:")
        for i in range(3):
            for face in ['Left', 'Front', 'Right', 'Bottom']:

                for j in range(3):
                    print(color_codes[self.cube[face].array[i][j]],
                          self.cube[face].array[i][j],  color_codes['RESET'], end='')
                print(' ', end='')
            print()
        print("D face:")
        for i in range(3):
            print(' '*3, end='')
            for j in range(3):
                print(color_codes[self.cube['Down'].array[i][j]],
                      self.cube['Down'].array[i][j], color_codes['RESET'],  end='')
            print()
        print("\n")


class Mouves:

    def __init__(self, rubik: RubiksCube):
        self.mouves = {
            "U": lambda: rubik.rotate_face_clockwise("Up"),
            "U'": lambda: rubik.rotate_face_counterclockwise("Up"),
            "U2": lambda: (
                rubik.rotate_face_clockwise("Up"),
                rubik.rotate_face_clockwise("Up"),
            ),

            "D": lambda: rubik.rotate_face_clockwise("Down"),
            "D'": lambda: rubik.rotate_face_counterclockwise("Down"),
            "D2": lambda: (
                rubik.rotate_face_clockwise("Down"),
                rubik.rotate_face_clockwise("Down"),
            ),

            "F": lambda: rubik.rotate_face_clockwise("Front"),
            "F'": lambda: rubik.rotate_face_counterclockwise("Front"),
            "F2": lambda: (
                rubik.rotate_face_clockwise("Front"),
                rubik.rotate_face_clockwise("Front"),
            ),

            "B": lambda: rubik.rotate_face_clockwise("Bottom"),
            "B'": lambda: rubik.rotate_face_counterclockwise("Bottom"),
            "B2": lambda: (
                rubik.rotate_face_clockwise("Bottom"),
                rubik.rotate_face_clockwise("Bottom"),
            ),

            "L": lambda: rubik.rotate_face_clockwise("Left"),
            "L'": lambda: rubik.rotate_face_counterclockwise("Left"),
            "L2": lambda: (
                rubik.rotate_face_clockwise("Left"),
                rubik.rotate_face_clockwise("Left"),
            ),

            "R": lambda: rubik.rotate_face_clockwise("Right"),
            "R'": lambda: rubik.rotate_face_counterclockwise("Right"),
            "R2": lambda: (
                rubik.rotate_face_clockwise("Right"),
                rubik.rotate_face_clockwise("Right"),
            ),
        }


class Opposite_mouves:

    def __init__(self, rubik: RubiksCube):
        self.mouves = {
            "U'": lambda: rubik.rotate_face_clockwise("Up"),
            "U": lambda: rubik.rotate_face_counterclockwise("Up"),
            "U2": lambda: (
                rubik.rotate_face_clockwise("Up"),
                rubik.rotate_face_clockwise("Up"),
            ),

            "D'": lambda: rubik.rotate_face_clockwise("Down"),
            "D": lambda: rubik.rotate_face_counterclockwise("Down"),
            "D2": lambda: (
                rubik.rotate_face_clockwise("Down"),
                rubik.rotate_face_clockwise("Down"),
            ),

            "F'": lambda: rubik.rotate_face_clockwise("Front"),
            "F": lambda: rubik.rotate_face_counterclockwise("Front"),
            "F2": lambda: (
                rubik.rotate_face_clockwise("Front"),
                rubik.rotate_face_clockwise("Front"),
            ),

            "B'": lambda: rubik.rotate_face_clockwise("Bottom"),
            "B": lambda: rubik.rotate_face_counterclockwise("Bottom"),
            "B2": lambda: (
                rubik.rotate_face_clockwise("Bottom"),
                rubik.rotate_face_clockwise("Bottom"),
            ),

            "L'": lambda: rubik.rotate_face_clockwise("Left"),
            "L": lambda: rubik.rotate_face_counterclockwise("Left"),
            "L2": lambda: (
                rubik.rotate_face_clockwise("Left"),
                rubik.rotate_face_clockwise("Left"),
            ),

            "R'": lambda: rubik.rotate_face_clockwise("Right"),
            "R": lambda: rubik.rotate_face_counterclockwise("Right"),
            "R2": lambda: (
                rubik.rotate_face_clockwise("Right"),
                rubik.rotate_face_clockwise("Right"),
            ),
        }

    # def __setattr__(self, other: RubiksCube) -> RubiksCube:
    #     other.cube = copy.copy(self.cube)
    #     return other
