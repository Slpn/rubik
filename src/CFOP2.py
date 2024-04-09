

import time
from rubik_class import Opposite_mouves, RubiksCube
from faceClass import Edge, Face, check_edge_color, dir_nodes
import numpy as np
from utils import get_face_to_mouve, mouves_dir
from vizualize import RubixVisualiser

cross_idx = [(0, 1), (1, 0), (1, 2), (2, 1)]


def resolve_cross(rubix: RubiksCube, visualiser: RubixVisualiser):
    visualiser.SPEED = 0.5
    white_face = rubix.cube['Up']
    other_faces = [rubix.cube[other_face]
                   for other_face in rubix.cube if other_face != white_face.dir]
    well_placed = [
        idx for idx in cross_idx if white_face.array[idx[0]][idx[1]] == white_face.color and check_edge_color(white_face, idx, rubix)]
    while (len(well_placed) != 4):
        for face in other_faces:
            for idx in cross_idx:
                print('ffff', face.dir, face.array[idx[0]][idx[1]],  check_edge_color(
                    face, idx, rubix))
                if face.array[idx[0]][idx[1]] == white_face.color and check_edge_color(face, idx, rubix):
                    place_on_cross(white_face, face, idx, rubix, visualiser)
                time.sleep(2)

        # for face in other_faces:
        #     for idx in cross_idx:
        #         if face.array[idx[0]][idx[1]] == white_face.color:
        #             face, idx = place_on_good_edge()
        #             place_on_cross(white_face, face, idx, rubix, visualiser)


def rotate_cross(rubix: RubiksCube, cross_face: Face, to_mouve: str, idx: tuple, visualiser: RubixVisualiser):
    opposite_mouves = Opposite_mouves(rubix)
    dir = cross_face.dir
    i, j = None, None

    match dir:
        case 'Up' | 'Down':
            match to_mouve:
                case 'Front' | 'Bottom':
                    i, j = 2 if to_mouve == 'Front' else 0, 1
                case 'Left' | 'Right':
                    i, j = 1, 0 if to_mouve == 'Left' else 2
                case 'Up' | 'Down':
                    i, j = idx[0], idx[1]

        case 'Front' | 'Bottom':
            match to_mouve:
                case 'Left' | 'Right':
                    i, j = 1, 0 if to_mouve == 'Left' else 2
                case 'Up' | 'Down':
                    i, j = 0 if to_mouve == 'Up' else 2, 1
                case 'Front' | 'Bottom':
                    i, j = idx[0], idx[1]

        case 'Left' | 'Right':
            match to_mouve:
                case 'Front':
                    i, j = 1, 0 if to_mouve == 'Right' else 2
                case 'Bottom':
                    i, j = 1, 0 if to_mouve == 'Left' else 2
                case 'Up' | 'Down':
                    i, j = 0 if to_mouve == 'Up' else 2, 1
                case 'Left' | 'Right':
                    i, j = idx[0], 2 - idx[1]

    print(cross_face.array[i][j], cross_face.color)
    if cross_face.array[i][j] == cross_face.color:
        for mouve in mouves_dir[dir]:
            rubix.mouves[mouves_dir[dir][mouve]]()
            visualiser.visualizer_mouves[mouves_dir[dir][mouve]]()
            time.sleep(visualiser.SPEED)
            if (cross_face.array[i][j] == cross_face.color):
                opposite_mouves.mouves[mouves_dir[dir][mouve]]()
                visualiser.opposite_mouves[mouves_dir[dir][mouve]]()
                time.sleep(visualiser.SPEED)
            else:
                rubix.soluce_mouves.append(mouve)
                break


def place_on_cross(cross_face: Face, face: Face, idx: tuple, rubix: RubiksCube, visualiser: RubixVisualiser):
    opposite_mouves = Opposite_mouves(rubix)
    to_mouve = get_face_to_mouve(face.dir, idx)
    rotate_cross(rubix, cross_face, to_mouve, idx, visualiser)
    color = rubix.cube[to_mouve].color
    for mouve in mouves_dir[to_mouve]:
        print(mouves_dir[to_mouve][mouve])
        rubix.mouves[mouves_dir[to_mouve][mouve]]()
        visualiser.visualizer_mouves[mouves_dir[to_mouve][mouve]]()
        time.sleep(visualiser.SPEED)
        edges = [cross_face.get_edge(
            _idx, rubix) for _idx in cross_idx if cross_face.array[_idx[0]][_idx[1]] == cross_face.color]
        print('edges', edges)
        is_in_cross = list(
            filter(lambda edge: edge['face'].color == color, edges))
        print('i in cross', is_in_cross)
        if len(is_in_cross) == 0:
            opposite_mouves.mouves[mouves_dir[to_mouve][mouve]]()
            visualiser.opposite_mouves[mouves_dir[to_mouve][mouve]]()
            time.sleep(visualiser.SPEED)
        else:
            rubix.soluce_mouves.append(mouve)
            break
