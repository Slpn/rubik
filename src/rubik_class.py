from rubix_types import Faces
from copy import copy
import numpy as np
from rubix_types import color_codes


class RubiksCube:

    def __init__(self):
        self.cube: dict[Faces, np.array] = self.reset_cube()
        self.mouves = {
            "U": lambda: self.rotate_face_clockwise("Up"),
            "U'": lambda: self.rotate_face_counterclockwise("Up"),

            "D": lambda: self.rotate_face_clockwise("Down"),
            "D'": lambda: self.rotate_face_counterclockwise("Down"),

            "F": lambda: self.rotate_face_clockwise("Front"),
            "F'": lambda: self.rotate_face_counterclockwise("Front"),

            "B": lambda: self.rotate_face_clockwise("Bottom"),
            "B'": lambda: self.rotate_face_counterclockwise("Bottom"),

            "L": lambda: self.rotate_face_clockwise("Left"),
            "L'": lambda: self.rotate_face_counterclockwise("Left"),

            "R": lambda: self.rotate_face_clockwise("Right"),
            "R'": lambda: self.rotate_face_counterclockwise("Right"),
        }

    def reset_cube(self):
        return {
            'Up': np.full((3, 3), 'W'),
            'Down': np.full((3, 3), 'Y'),
            'Front': np.full((3, 3), 'G'),
            'Bottom': np.full((3, 3), 'B'),
            'Left': np.full((3, 3), 'O'),
            'Right': np.full((3, 3), 'R')
        }

    def get_edges_cpy(self, face: Faces):
        top_edge, left_edge, down_edge, right_edge, front_edge, bottom_edge = None, None, None, None, None, None
        match face:

            case 'Front' | 'Bottom':
                idx = 2 if face == 'Front' else 0
                top_edge = copy(self.cube['Up'][idx])
                left_edge = copy([self.cube['Left'][i][idx]
                                  for i in range(3)])
                down_edge = copy(self.cube['Down'][2 - idx])
                right_edge = copy([self.cube['Right'][i][2 - idx]
                                   for i in range(3)])

            case 'Left' | 'Right':
                idx = 0 if face == 'Left' else 2
                top_edge = copy([self.cube['Up'][i][idx]
                                 for i in range(3)])
                front_edge = copy([self.cube['Front'][i][idx]
                                   for i in range(3)])
                down_edge = copy([self.cube['Down'][i][idx]
                                  for i in range(3)])
                bottom_edge = copy([self.cube['Bottom'][i][2 - idx]
                                    for i in range(3)])

            case 'Up' | 'Down':
                idx = 0 if face == 'Up' else 2
                left_edge = copy(self.cube["Left"][idx])
                front_edge = copy(self.cube["Front"][idx])
                right_edge = copy(self.cube["Right"][idx])
                bottom_edge = copy(self.cube["Bottom"][idx])

        return top_edge, left_edge, down_edge, right_edge, front_edge, bottom_edge

    def rotate_face_counterclockwise(self, face: Faces):
        temp_top, temp_left, temp_down, temp_right, temp_front, temp_bottom = self.get_edges_cpy(
            face)
        self.cube[face] = np.rot90(self.cube[face])

        match face:

            case "Front":

                self.cube['Down'][0] = temp_left
                self.cube['Up'][2] = temp_right

                for i in range(3):
                    self.cube['Right'][i][0] = temp_down[2 - i]
                    self.cube['Left'][i][2] = temp_top[2 - i]

            case "Bottom":

                self.cube['Down'][2] = temp_right[::-1]
                self.cube['Up'][0] = temp_left[::-1]

                for i in range(3):
                    self.cube['Right'][i][2] = temp_top[i]
                    self.cube['Left'][i][0] = temp_down[i]

            case 'Left':
                for i in range(3):
                    self.cube['Down'][i][0] = temp_bottom[2 - i]
                    self.cube['Up'][i][0] = temp_front[i]
                    self.cube['Bottom'][i][2] = temp_top[2 - i]
                    self.cube['Front'][i][0] = temp_down[i]

            case 'Right':
                for i in range(3):
                    self.cube['Down'][i][2] = temp_front[i]
                    self.cube['Up'][i][2] = temp_bottom[2 - i]
                    self.cube['Bottom'][i][0] = temp_down[2 - i]
                    self.cube['Front'][i][2] = temp_top[i]

            case 'Up':
                self.cube['Left'][0] = temp_bottom
                self.cube['Right'][0] = temp_front
                self.cube['Bottom'][0] = temp_right
                self.cube['Front'][0] = temp_left

            case 'Down':
                self.cube['Left'][2] = temp_front
                self.cube['Right'][2] = temp_bottom
                self.cube['Bottom'][2] = temp_left
                self.cube['Front'][2] = temp_right

    def rotate_face_clockwise(self, face):
        temp_top, temp_left, temp_down, temp_right, temp_front, temp_bottom = self.get_edges_cpy(
            face)

        self.cube[face] = np.rot90(self.cube[face], k=-1)

        match face:

            case 'Front':

                self.cube['Up'][2] = temp_left[::-1]
                self.cube['Down'][0] = temp_right[::-1]

                for i in range(3):
                    self.cube['Right'][i][0] = temp_top[i]
                    self.cube['Left'][i][2] = temp_down[i]

            case "Bottom":

                self.cube['Down'][2] = temp_left
                self.cube['Up'][0] = temp_right

                for i in range(3):
                    self.cube['Right'][i][2] = temp_down[2-i]
                    self.cube['Left'][i][0] = temp_top[2-i]

            case 'Left':
                for i in range(3):
                    self.cube['Down'][i][0] = temp_front[i]
                    self.cube['Up'][i][0] = temp_bottom[2 - i]
                    self.cube['Bottom'][i][2] = temp_down[2 - i]
                    self.cube['Front'][i][0] = temp_top[i]

            case 'Right':
                for i in range(3):
                    self.cube['Down'][i][2] = temp_bottom[2 - i]
                    self.cube['Up'][i][2] = temp_front[i]
                    self.cube['Bottom'][i][0] = temp_top[2 - i]
                    self.cube['Front'][i][2] = temp_down[i]

            case 'Up':
                self.cube['Left'][0] = temp_front
                self.cube['Right'][0] = temp_bottom
                self.cube['Bottom'][0] = temp_left
                self.cube['Front'][0] = temp_right

            case 'Down':
                self.cube['Left'][2] = temp_bottom
                self.cube['Right'][2] = temp_front
                self.cube['Bottom'][2] = temp_right
                self.cube['Front'][2] = temp_left

    def check_solved(self):
        for face in self.cube:
            for row in self.cube[face]:
                for color in row:
                    if color != row[0]:
                        return False
        return True

    def pretty_print(self):
        print("U face:")
        for i in range(3):
            print(' '*3, end='')
            for j in range(3):
                print(color_codes[self.cube['Up'][i][j]],
                      self.cube['Up'][i][j],  color_codes['RESET'], end='',)
            print()
        print("F face surrounded by L, R, and B:")
        for i in range(3):
            for face in ['Left', 'Front', 'Right', 'Bottom']:
                for j in range(3):
                    print(color_codes[self.cube[face][i][j]],
                          self.cube[face][i][j],  color_codes['RESET'], end='')
                print(' ', end='')
            print()
        print("D face:")
        for i in range(3):
            print(' '*3, end='')
            for j in range(3):
                print(color_codes[self.cube['Down'][i][j]],
                      self.cube['Down'][i][j], color_codes['RESET'],  end='')
            print()
        print("\n")

    # def solve_cross(self):
    #     target_color = 'W'
    #     for edge in find_edges(target_color):
    #         position_edge_correctly(edge)

    def solve_f2l(self):
        pass

    def solve_oll(self):
        pass

    def solve_pll(self):
        pass
