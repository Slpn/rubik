import time
from F2L_algo_class import F2L_algo
from rubik_class import Opposite_mouves, RubiksCube
from face_class import Edge, Face, check_edge_color, dir_nodes
import numpy as np
from utils import CircularChainedList, get_face_to_mouve, mouves_dir, get_new_idx
from vizualize import RubixVisualiser


def F2L(rubik: RubiksCube, visualiser: RubixVisualiser):
    corner_index = [(0, 0), (0, 2), (2, 0), (2, 2)]
    faces = [rubik.cube[face] for face in rubik.cube]

    all_corner = {face.dir: [face.get_corners(
        index, rubik) for index in corner_index] for face in faces}

    white_corner = {face: [corner for corner in all_corner[face]
                           if corner['corner']['color'] == 'W'] for face in all_corner}

    algo = F2L_algo()
    for corner in white_corner:
        for elem in white_corner[corner]:
            print(corner, ":", elem)
            print('is well placed :', algo.is_cube_well_placed(elem))
        print()
