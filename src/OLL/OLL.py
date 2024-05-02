

from rubik_class import RubiksCube
import numpy as np
from OLL.OLL_algos import algos
from rubik_utils import inverse_mouves_dir, \
    x_mouves_dir, x_prime_mouves_dir, \
    y_mouves_dir, y_prime_mouve_dir, y2_mouve_dir, \
    z_mouves_dir, z_prime_mouves_dir, x2_mouves_dir


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
    print(down_array)
    for i in range(4):
        print(i)
        for algo in algos:
            if np.array_equal(down_array, algo['shema']):
                print("found", algo)
                found_oll = algo
                break
        if found_oll:
            print("fouuudnd")
            break
        down_array = np.rot90(down_array)

    return found_oll, i


def append_mouve(soluce_mouves: list[str], mouve: str):
    soluce_mouves.append(inverse_mouves_dir[mouve])


def append_y_mouve(soluce_mouves: list[str], mouve: str):
    soluce_mouves.append(inverse_mouves_dir[y_mouves_dir[mouve]])


def append_y_prime_mouve(soluce_mouves: list[str], mouve: str):
    soluce_mouves.append(inverse_mouves_dir[y_prime_mouve_dir[mouve]])


def append_y2_prime_mouve(soluce_mouves: list[str], mouve: str):
    soluce_mouves.append(inverse_mouves_dir[y2_mouve_dir[mouve]])


def make_mouve(soluce_mouves: list[str], found_oll: dict, append_func: callable):
    x, x_prime, z, z_prime, y, y_prime, x2 = False, False, False, False, False, False, False

    print('in make mouves', found_oll)
    for mouve in found_oll['mouves']:
        to_append = mouve
        match to_append:
            case "x" | "r" | "l'" | "M'" | "M2":
                if x_prime:
                    x_prime = False
                else:
                    x = True

                if to_append == "r":
                    to_append = "L"
                elif to_append == "l'":
                    to_append = "R'"
                elif to_append == "M'":
                    append_func(soluce_mouves, "L")
                    to_append = "R'"
                elif to_append == 'M2':
                    append_func(soluce_mouves, "L2")
                    to_append = "R2"
                    print("M2")
                    x = True
                    x_prime = False

                else:
                    continue

            case "x'" | "r'" | "l" | 'M':
                if x:
                    x = False
                else:
                    x_prime = True

                if to_append == "r'":
                    to_append = "L'"
                elif to_append == "l":
                    to_append = "R"
                elif to_append == 'M':
                    append_func(soluce_mouves, "L'")
                    to_append = 'R'
                else:
                    continue

            case "z" | "f" | "b'":
                if z:
                    z_prime = False
                else:
                    z = True

                if to_append == "f":
                    to_append = "B"
                elif to_append == "b'":
                    to_append = "F'"
                else:
                    continue

            case "z'" | "f'" | "b":
                if z:
                    z = False
                else:
                    z_prime = True

                if to_append == "f'":
                    to_append = "B'"
                elif to_append == "b":
                    to_append = "F"
                else:
                    continue

            case 'y':
                if y_prime:
                    y_prime = False
                else:
                    y = True

                continue

            case "y'":
                if y:
                    y = False
                else:
                    y_prime = True

                continue

        print("zzzzz", z)
        if z:
            append_func(soluce_mouves, z_mouves_dir[to_append])
        elif z_prime:
            append_func(soluce_mouves, z_prime_mouves_dir[to_append])
        elif x:
            append_func(soluce_mouves, x_mouves_dir[to_append])
        elif x_prime:
            append_func(soluce_mouves, x_prime_mouves_dir[to_append])
        elif x2:
            append_func(soluce_mouves, x2_mouves_dir[to_append])
        else:
            append_func(soluce_mouves, to_append)


def OLL(rubik: RubiksCube):
    found_oll, rotate = detect_OLL(rubik)
    print("rotate", rotate)
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

    make_mouve(soluce_mouves, found_oll, append_func)

    return soluce_mouves
