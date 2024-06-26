

from rubik_class import RubiksCube
import numpy as np
from OLL.OLL_algos import algos
from rubik_utils import apply_mouves, make_algo_mouves, append_mouve, append_y2_prime_mouve, append_y_mouve, append_y_prime_mouve


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
    down_array = get_down_with_adjacent(rubik)
    found_oll = None
    for i in range(4):
        for algo in algos:
            if np.array_equal(down_array, algo['shema']):
                found_oll = algo
                break
        if found_oll:
            break
        down_array = np.rot90(down_array)

    return found_oll, i


def OLL(rubik: RubiksCube):
    found_oll, rotate = detect_OLL(rubik)
    soluce_mouves = []
    def append_func(): return None
    if (rotate == 0):
        append_func = append_mouve
    elif rotate == 3:
        append_func = append_y_mouve
    elif rotate == 1:
        append_func = append_y_prime_mouve
    elif rotate == 2:
        append_func = append_y2_prime_mouve

    make_algo_mouves(soluce_mouves, found_oll["mouves"], append_func)
    apply_mouves(soluce_mouves, rubik, None, False)
    return soluce_mouves
