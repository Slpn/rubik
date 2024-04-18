from enum import Enum
import sys
import time
from typing import Union
from vispy import app, scene, gloo, visuals
import numpy as np
from vispy.color import ColorArray


CUBE_SIZE = 1


colors_exemple = [
    ['RED', 'GREEN', 'BLUE'],
    ['YELLOW', 'ORANGE', 'BLACK'],
    ['PURPLE', 'BEIGE', 'WHITE']
]
colors = {
    'RED': (1.0, 0.0, 0.0),
    'GREEN': (0.0, 1, 0.0),
    'BLUE': (0.0, 0.0, 1),
    'YELLOW': (1, 1, 0.0),
    'ORANGE': (1.0, 0.5, 0.0),
    'BLACK': (0.0, 0.0, 0.0),
    'PURPLE': (0.5, 0, 0.5),
    'BEIGE': (0.5, 0.2, 0.5),
    'WHITE':  (1.0, 1.0, 1.0)

}


faceIndex = {
    "FRONT": [0, 2],
    "BOTTOM": [2, 4],
    "DOWN": [4, 6],
    "UP": [6, 8],
    "RIGHT": [8, 10],
    "LEFT": [10, 12],
}

face_colors = [
    colors['YELLOW'], colors['BLACK'],
    colors['BLUE'], colors['BLUE'],
    colors['RED'], colors['RED'],
    colors['GREEN'], colors['BLACK'],
    colors['WHITE'], colors['BLACK'],
    colors['ORANGE'], colors['BLACK']
]


class RubixVisualiser(app.Canvas):

    def __init__(self):
        app.Canvas.__init__(self, keys='interactive',
                            show=False)

        self.SPEED = 0.06

        self.view = scene.SceneCanvas(keys='interactive', show=True)
        self.view.size = (800, 600)
        self.view.create_native()

        self.view_widget = self.view.central_widget.add_view()
        self.view_widget.bgcolor = (1, 1, 1, 1)

        self.cam = scene.cameras.TurntableCamera(parent=self.view_widget.scene,
                                                 up='y', azimuth=-45, elevation=30, distance=10, center=(0, 0, 0), roll=360)

        self.cam.flip = (False, True, False)
        self.view_widget.camera = self.cam

        self.cam.set_range()

        self.node_cube = scene.node.Node(parent=self.view_widget.scene, name='rubix',
                                         transforms=None)
        self.node_face = scene.node.Node(parent=self.node_cube, name="up_face",
                                         transforms=None)

        self.all_cubes_nodes: list[scene.node.Node] = self.create_cube()

        self.visualizer_mouves = {
            "U": self.U,
            "U'": self.U_prime,
            "U2": lambda: (
                self.U(),
                self.U(),
            ),

            "D": self.D,
            "D'": self.D_prime,
            "D2": lambda: (
                self.D(),
                self.D(),
            ),

            "F": self.F,
            "F'": self.F_prime,
            "F2": lambda: (
                self.F(),
                self.F(),
            ),

            "B": self.B,
            "B'": self.B_prime,
            "B2": lambda: (
                self.B(),
                self.B(),
            ),

            "L": self.L,
            "L'": self.L_prime,
            "L2": lambda: (
                self.L(),
                self.L(),
            ),

            "R": self.R,
            "R'": self.R_prime,
            "R2": lambda: (
                self.R(),
                self.R(),
            ),
        }

        self.opposite_mouves = {
            "U'": self.U,
            "U": self.U_prime,
            "U2": lambda: (
                self.U(),
                self.U(),
            ),

            "D'": self.D,
            "D": self.D_prime,
            "D2": lambda: (
                self.D(),
                self.D(),
            ),

            "F'": self.F,
            "F": self.F_prime,
            "F2": lambda: (
                self.F(),
                self.F(),
            ),

            "B'": self.B,
            "B": self.B_prime,
            "B2": lambda: (
                self.B(),
                self.B(),
            ),

            "L'": self.L,
            "L": self.L_prime,
            "L2": lambda: (
                self.L(),
                self.L(),
            ),

            "R'": self.R,
            "R": self.R_prime,
            "R2": lambda: (
                self.R(),
                self.R(),
            ),
        }

        # self.worker_thread = WorkerThread(self)
        # self.worker_thread.start()

    def close(self):
        app.quit()
        raise KeyboardInterrupt('Visualiser have quit')

    def on_timer(self, event):
        self.update()

    def add_child(self, group: str):
        """Add the good cubes to the slice we are about to mouve
        For exemple, if we are about to rotate the up face of the rubik,
        we have to find the cube located on this face, whith are the ones white the biggest
        value of their position on Y axe.
          """
        match group:

            case 'DOWN' | 'UP':
                sorted_cubes = sorted(
                    self.all_cubes_nodes, key=lambda node: node.node_transform(self.node_cube).map((0, 0, 0))[1])
                # if we want to rotate the down face, we take the 9 first cube witg the lowest Y, else we take the last ones (biggest)
                cubes_face = sorted_cubes[0:9] if group == 'DOWN' else sorted_cubes[-9:]

            case 'FRONT' | "BOTTOM":
                sorted_cubes = sorted(
                    self.all_cubes_nodes, key=lambda node: node.node_transform(self.node_cube).map((0, 0, 0))[2])
                cubes_face = sorted_cubes[0:9] if group == 'FRONT' else sorted_cubes[-9:]

            case 'LEFT' | "RIGHT":
                sorted_cubes = sorted(
                    self.all_cubes_nodes, key=lambda node: node.node_transform(self.node_cube).map((0, 0, 0))[0])
                cubes_face = sorted_cubes[0:9] if group == 'RIGHT' else sorted_cubes[-9:]

        for cube in cubes_face:
            cube.parent = self.node_face

    def rotate(self, axis: tuple, angle):
        test = scene.transforms.MatrixTransform()
        rotate = angle / 10
        for _ in range(10):

            test.rotate(rotate, axis)
            self.node_face.transform = test
            time.sleep(self.SPEED)

        for node in self.node_face.children:
            node.transform = test * node.transform
            node.parent = self.node_cube

        self.node_face.transform.reset()

    def F(self):
        self.add_child('FRONT')
        self.rotate((0, 0, 1), 90)

    def F_prime(self):
        self.add_child('FRONT')
        self.rotate((0, 0, 1), -90)

    def B(self):
        self.add_child('BOTTOM')
        self.rotate((0, 0, 1), -90)

    def B_prime(self):
        self.add_child('BOTTOM')
        self.rotate((0, 0, 1), 90)

    def U(self):
        self.add_child('UP')
        self.rotate((0, 1, 0), -90)

    def U_prime(self):
        self.add_child('UP')
        self.rotate((0, 1, 0), 90)

    def D(self):
        self.add_child('DOWN')
        self.rotate((0, 1, 0), 90)

    def D_prime(self):
        self.add_child('DOWN')
        self.rotate((0, 1, 0), -90)

    def L(self):
        self.add_child('LEFT')
        self.rotate((1, 0, 0), -90)

    def L_prime(self):
        self.add_child('LEFT')
        self.rotate((1, 0, 0), 90)

    def R(self):
        self.add_child('RIGHT')
        self.rotate((1, 0, 0), 90)

    def R_prime(self):
        self.add_child('RIGHT')
        self.rotate((1, 0, 0), -90)

    def create_cube(self) -> list[scene.node.Node]:
        """
            Create an ordered 3x3 rubik.
            Each cube is store in a node.
        """
        center_pos = (0, 0, 0)
        # Pos of the up slice of the rubik
        positions = [
            [center_pos[0] - (1 * CUBE_SIZE),
             CUBE_SIZE * 2,
             center_pos[2] - (1 * CUBE_SIZE)],

            [center_pos[0] - (0 * CUBE_SIZE),
             CUBE_SIZE * 2,
             center_pos[2] - (1 * CUBE_SIZE)],

            [center_pos[0] + (1 * CUBE_SIZE),
             CUBE_SIZE * 2,
             center_pos[2] - (1 * CUBE_SIZE)],

            [center_pos[0] - (1 * CUBE_SIZE),
             CUBE_SIZE * 2,
             center_pos[2] - (0 * CUBE_SIZE)],

            [center_pos[0] - (0 * CUBE_SIZE),
             CUBE_SIZE * 2,
             center_pos[2] - (0 * CUBE_SIZE)],

            [center_pos[0] + (1 * CUBE_SIZE),
             CUBE_SIZE * 2,
             center_pos[2] - (0 * CUBE_SIZE)],

            [center_pos[0] - (1 * CUBE_SIZE),
             CUBE_SIZE * 2,
             center_pos[2] + (1 * CUBE_SIZE)],

            [center_pos[0] - (0 * CUBE_SIZE),
             CUBE_SIZE * 2,
             center_pos[2] + (1 * CUBE_SIZE)],

            [center_pos[0] + (1 * CUBE_SIZE),
             CUBE_SIZE * 2,
             center_pos[2] + (1 * CUBE_SIZE)],
        ]

        cubes = []
        # In each iteration, the initial position is translated on the y axe,
        # Of the 3 iteration result the rubik (3 slice combinated)
        for i in range(1, 4):
            for j in range(len(positions)):
                # uptate the position on the y axe for each cube
                positions[j][1] -= 1
            for idx, pos in enumerate(positions):
                face_colors = np.full((12, 3), colors['BLACK'])
                # face color object store the position of the color on the cubes which are composed of 12 color (2 per face)
                # exemple: to color the up face of a cube in red and the rest in black the face color should looks like:
                # [black, black, black, black, black, black, red, red, black, black, black, black]
                # the position index of up face is 6 and 7
                if (i == 1):
                    face_colors[faceIndex['UP'][0]                                :faceIndex['UP'][1]] = colors['WHITE']
                if (i == 3):
                    face_colors[faceIndex['DOWN'][0]                                :faceIndex['DOWN'][1]] = colors['YELLOW']
                if (idx >= 6):
                    face_colors[faceIndex['BOTTOM'][0]                                :faceIndex['BOTTOM'][1]] = colors['BLUE']
                if (idx % 3 == 0):
                    face_colors[faceIndex['RIGHT'][0]                                :faceIndex['RIGHT'][1]] = colors['RED']
                if (idx < 3):
                    face_colors[faceIndex['FRONT'][0]                                :faceIndex['FRONT'][1]] = colors['GREEN']
                if ((idx - 2) % 3 == 0):
                    face_colors[faceIndex['LEFT'][0]
                        :faceIndex['LEFT'][1]] = colors["ORANGE"]

                # Crete the node at the ggod position
                transform = scene.STTransform(translate=pos)
                cube_node = scene.node.Node(parent=self.node_cube, name=None)
                cube_node.transform = transform

                # Create the cube, children of the cube node
                scene.visuals.Cube(
                    size=CUBE_SIZE, face_colors=face_colors, edge_color='black', parent=cube_node)

                cubes.append(cube_node)

        return cubes


def launch_vizualiser():
    app.run()
