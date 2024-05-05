import copy
from rubik_class import RubiksCube
from PLL.PLL_algo import algos
from rubik_utils import get_new_idx, inverse_mouves_dir, make_algo_mouves
from rubik_utils import inverse_mouves_dir, \
    x_mouves_dir, x_prime_mouves_dir, \
    y_mouves_dir, y_prime_mouve_dir, y2_mouve_dir, \
    z_mouves_dir, z_prime_mouves_dir, x2_mouves_dir, \
    append_mouve, append_y2_prime_mouve, append_y_mouve, append_y_prime_mouve


def detect_PLL(rubik: RubiksCube):
    face = rubik.cube["Down"]
    for rotate in range(4):
        print("rotate", rotate)
        for algo in algos:
            found = True
            corners = algo["shema"]["coins"]
            edges = algo["shema"]["edges"]
            for corner in corners:

                coor1, coor2 = None, None

                match rotate:
                    case 0:
                        coor1 = corner[0]
                        coor2 = corner[1]
                    case 1:
                        coor1 = get_new_idx(corner[0], '-')
                        coor2 = get_new_idx(corner[1], '-')
                    case 2:
                        coor1 = get_new_idx(corner[0], 'opposite')
                        coor2 = get_new_idx(corner[1], 'opposite')
                    case 3:
                        coor1 = get_new_idx(corner[0], '+')
                        coor2 = get_new_idx(corner[1], '+')

                corner1 = face.get_corners(coor1, rubik)
                corner2 = face.get_corners(coor2, rubik)
                if not ((corner1["corner_i"]["color"] == corner2["corner_i"]["face"].color
                        and corner1["corner_j"]["color"] == corner2["corner_j"]["face"].color)
                        or (corner1["corner_j"]["color"] == corner2["corner_i"]["face"].color
                        and corner1["corner_i"]["color"] == corner2["corner_j"]["face"].color)):
                    print("corner not ok")
                    found = False
                    break
            if found:
                for edge in edges:

                    coor1, coor2 = None, None
                    match rotate:
                        case 0:
                            coor1 = edge[0]
                            coor2 = edge[1]
                        case 1:
                            coor1 = get_new_idx(edge[0], '-')
                            coor2 = get_new_idx(edge[1], '-')
                        case 2:
                            coor1 = get_new_idx(edge[0], 'opposite')
                            coor2 = get_new_idx(edge[1], 'opposite')
                        case 3:
                            coor1 = get_new_idx(edge[0], '+')
                            coor2 = get_new_idx(edge[1], '+')

                    edge1 = face.get_edge(coor1, rubik)
                    edge2 = face.get_edge(coor2, rubik)
                    print("e2", edge2)
                    if edge1["color"] != edge2["face"].color:
                        print("egde not ok")
                        found = False
                        break

            if found:
                return algo, rotate

    return None, None


def PLL(rubik: RubiksCube):
    found_pll, rotate = None, None
    soluce_mouves = []
    i = 0
    while (found_pll == None):
        found_pll, rotate = detect_PLL(rubik)
        if (found_pll):
            break
        i += 1
        rubik.mouves['D']()

    if i == 1:
        soluce_mouves.append('D')
    elif i == 2:
        soluce_mouves.append('D2')
    elif i == 3:
        soluce_mouves.append("D'")

    def append_func(): return None
    if (rotate == 0):
        append_func = append_mouve
    elif rotate == 3:
        append_func = append_y_mouve
    elif rotate == 1:
        append_func = append_y_prime_mouve
    elif rotate == 2:
        append_func = append_y2_prime_mouve

    make_algo_mouves(soluce_mouves, found_pll["mouves"], append_func)

    return soluce_mouves
