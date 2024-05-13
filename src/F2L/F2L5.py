import copy
import heapq
import random
import time
import F2L.F2L_algo as algo
from F2L.F2L_filters import *
from rubik_class import Opposite_mouves, RubiksCube
from face_class import Edge, Face, check_edge_color, dir_nodes, Corner
import numpy as np
from rubik_utils import apply_reversed_mouves, clear_mouves, get_face_to_mouve, mouves_dir, get_new_idx, inverse_mouves_dir, y_prime_mouve_dir, opposite_mouves
from vizualize import RubixVisualiser


def find_mouves(white_corner_bad_placed, rubik: RubiksCube) -> list[str]:
    mouves, algo_num = None, None
    found_mouves = []
    for corner in white_corner_bad_placed:
        for cube in white_corner_bad_placed[corner]:

            if is_cube_well_placed(cube):

                if (is_cube_on_top(cube)):
                    if (is_i_corner_equals_color(cube)):
                        if (adjacent := is_adjacent_well_placed(cube, rubik)):
                            if (adjacent["case"] == 1):
                                if (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.fourteen(cube)
                                elif (cube["corner"]["index"][1] == 2):
                                    mouves, algo_num = algo.thirteen(cube)
                            elif (adjacent["case"] == 2):
                                if (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.sixteen(cube)
                                elif (cube["corner"]["index"][1] == 2):
                                    mouves, algo_num = algo.fifteen(cube)

                        elif (adjacent := is_adjacent_j_well_placed(cube, rubik)):
                            if (adjacent["case"] == 1):
                                if (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.two(cube)
                                elif (cube["corner"]["index"][1] == 2):
                                    mouves, algo_num = algo.one(cube)
                            elif (adjacent["case"] == 2):
                                if (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.twelve(cube)
                                if (cube["corner"]["index"][1] == 2):
                                    mouves, algo_num = algo.eleven(cube)

                        elif (opopsite_case := is_opposite_right_well_placed(cube, rubik)):
                            if opopsite_case == 1:
                                if (cube["corner"]["index"][1] == 2):
                                    mouves, algo_num = algo.five(cube)

                                elif (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.eight(cube)

                            if opopsite_case == 2:
                                if (cube["corner"]["index"][1] == 2):
                                    mouves, algo_num = algo.nine(cube)

                                elif (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.four(cube)
                        elif (adjacent := is_adjacent_mid_well_placed(cube, rubik)):
                            if (adjacent["case"] == 1):
                                if (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.thirty_four(cube)
                                elif (cube["corner"]["index"][1] == 2):
                                    mouves, algo_num = algo.thirty_three(cube)
                            elif (adjacent["case"] == 2):
                                if (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.thirty_six(cube)
                                elif (cube["corner"]["index"][1] == 2):
                                    pass
                                    mouves, algo_num = algo.thirty_five(cube)

                        elif (opopsite_case := is_opposite_left_well_placed(cube, rubik)):
                            if opopsite_case == 1:
                                if (cube["corner"]["index"][1] == 2):
                                    mouves, algo_num = algo.seven(cube)
                                elif (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.six(cube)

                            elif opopsite_case == 2:
                                if (cube["corner"]["index"][1] == 2):
                                    mouves, algo_num = algo.three(cube)

                                elif (cube["corner"]["index"][1] == 0):
                                    mouves, algo_num = algo.ten(cube)

                elif (is_cube_up_face(cube)):

                    if (is_i_corner_equals_j_color(cube)):
                        time.sleep(0)
                        if (adjacent := is_adjacent_mid_well_placed(cube, rubik)):
                            if (adjacent["case"] == 1):
                                mouves, algo_num = algo.thirty_one(cube)
                            elif (adjacent["case"] == 2):
                                mouves, algo_num = algo.thirty_two(cube)
                        elif (adjacent := is_adjacent_well_placed(cube, rubik, on_top=True)):
                            if adjacent["case"] == 2:
                                mouves, algo_num = algo.seventeen(cube)
                            elif adjacent["case"] == 1:
                                mouves, algo_num = algo.twenty_four(cube)
                        elif (adjacent := is_adjacent_j_well_placed(cube, rubik, on_top=True)):
                            if adjacent["case"] == 2:
                                mouves, algo_num = algo.eighteen(cube)
                            elif adjacent["case"] == 1:
                                mouves, algo_num = algo.twenty_three(cube)

                        elif opposite := is_opposite_right_well_placed(cube, rubik, on_top=True):
                            if opposite == 1:
                                mouves, algo_num = algo.twenty_two(cube)
                            elif opposite == 2:
                                mouves, algo_num = algo.nineteen(cube)

                        elif opposite := is_opposite_left_well_placed(cube, rubik, on_top=True):
                            if opposite == 1:
                                mouves, algo_num = algo.twenty(cube)
                            elif opposite == 2:
                                mouves, algo_num = algo.twenty_one(cube)

                elif is_cube_on_bottom(cube):
                    if right_edge := right_up_edge_well_placed(cube, rubik):
                        if right_edge["case"] == 1:
                            mouves, algo_num = algo.twenty_seven(cube)
                        elif right_edge["case"] == 2:
                            mouves, algo_num = algo.thirty(cube)
                    elif left_edge := left_up_edge_well_placed(cube, rubik):
                        if left_edge["case"] == 1:
                            mouves, algo_num = algo.twenty_nine(cube)
                        elif left_edge["case"] == 2:
                            mouves, algo_num = algo.twenty_eight(cube)
                    elif (adjacent := is_adjacent_mid_well_placed(cube, rubik)):
                        if (adjacent["case"] == 1):
                            if (cube["corner"]["index"][1] == 0):
                                mouves, algo_num = algo.forty(cube)
                            elif (cube["corner"]["index"][1] == 2):
                                mouves, algo_num = algo.thirty_nine(cube)
                        elif (adjacent["case"] == 2):
                            if (cube["corner"]["index"][1] == 0):
                                mouves, algo_num = algo.forty_two(cube)
                            elif (cube["corner"]["index"][1] == 2):
                                mouves, algo_num = algo.forty_one(cube)

            if (mouves):
                found_mouves.append((mouves, algo_num))

    return found_mouves


def find_mouves_bis(white_corner_well_placed, rubik: RubiksCube) -> list[str] | None:
    mouves, algo_num, best_mouve, best_algo = None, None, None, None
    found_mouves = []

    for corner in white_corner_well_placed:
        if is_left_edge_well_placed(corner, rubik):
            mouves, algo_num = algo.twenty_six(
                corner)
        if is_right_edge_well_placed(corner, rubik):
            mouves, algo_num = algo.twenty_five(
                corner)

        if (mouves):
            found_mouves.append((mouves, algo_num))

    if best_mouve == None:
        for corner_wp in white_corner_well_placed:
            R_face = rubik.cube[get_R_corner_bottom(
                corner_wp['corner']['index'])]
            mid_edges = R_face.get_edge(
                (1, 0), rubik)
            if R_face[(1, 0)] == mid_edges["face"].color\
                    and mid_edges["color"] == R_face.color:
                best_mouve, best_algo = algo.thirty_eight(R_face)
                found_mouves.append((best_mouve, best_algo))

    # return best_mouve, best_algo
    return found_mouves


def get_hashed_conf(rubik: RubiksCube) -> str:
    hashed_conf = ""
    for face in rubik.cube:
        str_array = "".join(rubik.cube[face].array.flatten())
        hashed_conf += str(hash(str_array))
    return hashed_conf


def get_found_mouves(rubik: RubiksCube, current_cost: int):
    found_mouves = []
    corner_index = [(0, 0), (0, 2), (2, 0), (2, 2)]
    faces = [rubik.cube[face] for face in rubik.cube]
    rubik_copy = copy.deepcopy(rubik.cube)
    all_corner = {face.dir: [face.get_corners(
        index, rubik) for index in corner_index] for face in faces}
    white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                      if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}
    for i in range(4):
        if len(list(filter(lambda elem: len(white_corner_bad_placed[elem]) > 0, white_corner_bad_placed))):
            found_mouves_mouves = find_mouves(
                white_corner_bad_placed, rubik)

            if len(found_mouves_mouves):
                for mouve in found_mouves_mouves:
                    mouves = mouve[0]
                    turn = []
                    if (i == 1):
                        turn = ['U']
                    elif (i == 2):
                        turn = ['U2']
                    elif (i == 3):
                        turn = ["U'"]

                    to_append = {
                        "mouves": copy.copy(clear_mouves(turn + mouves)),
                        "cost": current_cost + len(turn) + len(mouves)
                    }
                    found_mouves.append(to_append)

        white_corner_well_placed = [corner for corner in all_corner['Up']
                                    if corner['corner']['color'] == 'W' and is_final_pos(corner)]
        found_mouves_mouves = find_mouves_bis(
            white_corner_well_placed, rubik)
        if len(found_mouves_mouves):
            for mouve in found_mouves_mouves:
                mouves = mouve[0]
                turn = []
                if (i == 1):
                    turn = ['U']
                elif (i == 2):
                    turn = ['U2']
                elif (i == 3):
                    turn = ["U'"]
                to_append = {
                    "mouves": copy.copy(clear_mouves(turn + mouves)),
                    "cost": current_cost + len(turn) + len(mouves)
                }
                found_mouves.append(to_append)
        apply_reversed_mouves(['U'], rubik, None)
        all_corner = {face.dir: [face.get_corners(
            index, rubik) for index in corner_index] for face in faces}
        white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                          if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}

    rubik.cube = copy.deepcopy(rubik_copy)
    return found_mouves


def found_soluce(current_node: dict, closed_set: set):
    closed_set.add(
        tuple((current_node["id"], current_node["parent_id"],
               ' '.join(current_node['mouves']))))
    soluce_mouves: list[str] = []

    for mouve in reversed(current_node["mouves"]):
        soluce_mouves.append(inverse_mouves_dir[mouve])
    iter_node = next(
        (element for element in closed_set if element[0] == current_node["parent_id"]), None)
    while (iter_node and iter_node[1] != None):
        mouves = iter_node[2].split()
        for mouve in reversed(mouves):
            soluce_mouves.append(inverse_mouves_dir[mouve])
        iter_node = next(
            (element for element in closed_set if element[0] == iter_node[1]), None)
    if iter_node:
        mouves = iter_node[2].split()
        for mouve in reversed(mouves):
            soluce_mouves.append(inverse_mouves_dir[mouve])
    return list(reversed(soluce_mouves))


def F2L(rubik: RubiksCube, open_set: set, closed_set: set, visualiser: RubixVisualiser | None):

    soluce_mouves = []
    if visualiser:
        visualiser.SPEED = 0.03

    replaced_edges = []
    current_node = {
        "mouves": [],
        "parent_id": None,
        "cost": 0,
        "id": get_hashed_conf(rubik)

    }

    while True:
        if rubik.check_F2L() and not (current_node["id"] in [elem[0] for elem in closed_set]):
            return found_soluce(current_node, closed_set)
        if (current_node["cost"] > 40):
            return None

        found_mouves = get_found_mouves(
            rubik, current_node["cost"])

        if len(found_mouves):
            rubik_copy = copy.deepcopy(rubik.cube)
            for mouves in found_mouves:
                replaced_edges = []
                apply_reversed_mouves(mouves["mouves"], rubik, visualiser)
                hashed_conf = get_hashed_conf(rubik)
                conf = ' '.join(np.array(rubik.get_cube_array()).flatten())
                str_mouves = " ".join(mouves["mouves"])
                if not (hashed_conf in [elem[0] for elem in closed_set]):
                    heapq.heappush(open_set,
                                   tuple((mouves["cost"], hashed_conf, current_node["id"], str_mouves, conf)))
                rubik.cube = copy.deepcopy(rubik_copy)

        else:
            replace_edge(
                replaced_edges, open_set, current_node, rubik, visualiser)

        closed_set.add(
            tuple((current_node["id"], current_node["parent_id"],
                   ' '.join(current_node['mouves']))))
        if len(open_set) == 0:
            return None
        explore = heapq.heappop(open_set)
        #  time.sleep(3)
        while (explore[1] in [elem[0] for elem in closed_set]):
            if len(open_set) == 0:
                return None
            explore = heapq.heappop(open_set)
        mouves = explore[2].split()
        current_node = {
            "mouves": explore[3].split(),
            "parent_id": explore[2],
            "cost": explore[0],
            "id": explore[1]
        }
        rubik.get_conf_from_str(explore[4])

    return soluce_mouves


def replace_edge(tried, open_set: heapq, current_node: dict, rubik: RubiksCube, visualiser: RubixVisualiser | None, is_not_found=False):
    sense1 = None
    sense2 = None
    faces = ["Front", "Left", "Bottom", "Right"]
    random.shuffle(faces)
    for face in faces:
        if (face + "+" + ('nf' if is_not_found else '') not in tried and not is_chunck_resolved(face, "+", rubik, is_not_found)):
            to_mouve = face
            sense1 = "+"
            sense2 = "-"
            break

        elif (face + "-" + ('nf' if is_not_found else '') not in tried and not is_chunck_resolved(face, "-", rubik, is_not_found)):
            to_mouve = face
            sense1 = "-"
            sense2 = "+"
            break

    if (is_not_found and not sense1):
        return None
    if not sense1:
        return replace_edge(tried, open_set, current_node, rubik, visualiser, is_not_found=True)

    apply_reversed_mouves([mouves_dir[to_mouve][sense1], "U'",
                           mouves_dir[to_mouve][sense2]], rubik, visualiser)

    hashed_conf = get_hashed_conf(rubik)
    conf = ' '.join(np.array(rubik.get_cube_array()).flatten())
    heapq.heappush(open_set, tuple((current_node["cost"] + 3, hashed_conf, current_node["id"], ' '.join([mouves_dir[to_mouve][sense1], "U'",
                                                                                                         mouves_dir[to_mouve][sense2]]), conf)))
    # currend_nodes["mouves"].append(mouves_dir[to_mouve][sense1])
    # currend_nodes["mouves"].append("U'")
    # currend_nodes["mouves"].append(mouves_dir[to_mouve][sense2])
    # currend_nodes["cost"] += 3

    return to_mouve + sense1 + ('nf' if is_not_found else '')


def cancel_mouves(current_node, count: int, rubik: RubiksCube, visualiser: RubixVisualiser | None):
    opposite_mouves = Opposite_mouves(rubik)
    for i in range(len(current_node["mouves"]) - 1, len(current_node["mouves"]) - count - 1, -1):
        user_continue = ""
        while (visualiser and user_continue != "y"):
            user_continue = input("Tapez y pour le prochain mouv: ")

        opposite_mouves.mouves[current_node["mouves"][i]]()
        if (visualiser):
            visualiser.opposite_mouves[current_node["mouves"][i]](
            )
            time.sleep(visualiser.SPEED)
        current_node["mouves"].pop(i)
        current_node["cost"] -= 1
