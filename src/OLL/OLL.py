

from rubik_class import RubiksCube
import numpy as np
from OLL.OLL_algos import algos


def get_down_with_adjacent(rubik: RubiksCube):
    face_array = rubik.cube["Down"].array
    _, left_edge, _, right_edge, front_edge, bottom_edge = rubik.get_edges_cpy(
        rubik.cube["Down"])

    down_w_adj = np.array([
        np.concatenate([['_'], bottom_edge[::-1], ['_']]),
        np.concatenate([[left_edge[0]], face_array[2], [right_edge[2]]]),
        np.concatenate([[left_edge[1]], face_array[1], [right_edge[1]]]),
        np.concatenate([[left_edge[2]], face_array[0], [right_edge[0]]]),
        np.concatenate([['_'], front_edge, ['_']])

    ])
    mask = (down_w_adj != 'Y')
    down_w_adj[mask] = '_'
    return down_w_adj


def detect_OLL(rubik: RubiksCube):
    array_w_adj = get_down_with_adjacent(rubik,)
    print(array_w_adj)
    for i in range(4):
        print(i)
        for algo in algos:
            if np.array_equal(array_w_adj, algo['shema']):
                print("found", algo)
                break

        array_w_adj = np.rot90(array_w_adj)


def OLL(rubik: RubiksCube):
    detect_OLL(rubik)
