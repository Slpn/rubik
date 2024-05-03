import copy
import random
import time
import F2L.F2L_algo as algo
from F2L.F2L_filters import *
from rubik_class import Opposite_mouves, RubiksCube
from face_class import Edge, Face, check_edge_color, dir_nodes, Corner
import numpy as np
from rubik_utils import apply_reversed_mouves
from rubik_utils import mouves_dir, inverse_mouves_dir
from vizualize import RubixVisualiser


def find_mouves(white_corner_bad_placed, rubik: RubiksCube) -> list[str] | None:
    best_mouve, mouves, algo_num, best_algo = None, None, None, None
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

            # if (mouves and (best_mouve == None or len(mouves) < len(best_mouve))):
            #     best_mouve = copy.copy(mouves)
            #     best_algo = algo_num
            if mouves:
                found_mouves.append((mouves, algo_num))
    # return best_mouve, best_algo
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

        # if (mouves and (best_mouve == None or len(mouves) < len(best_mouve))):
        #     best_mouve = copy.copy(mouves)
        #     best_algo = algo_num
        if mouves:
            found_mouves.append((mouves, algo_num))

    if len(found_mouves) == 0:
        for corner_wp in white_corner_well_placed:
            R_face = rubik.cube[get_R_corner_bottom(
                corner_wp['corner']['index'])]
            mid_edges = R_face.get_edge(
                (1, 0), rubik)
            if R_face[(1, 0)] == mid_edges["face"].color\
                    and mid_edges["color"] == R_face.color:
                mouves, algo_num = algo.thirty_eight(R_face)
                found_mouves.append((mouves, algo_num))

#    return best_mouve, best_algo
    return found_mouves


def F2L(rubik: RubiksCube, visualiser: RubixVisualiser | None):
    soluce_mouves = []
    if visualiser:
        visualiser.SPEED = 0.0
    corner_index = [(0, 0), (0, 2), (2, 0), (2, 2)]
    faces = [rubik.cube[face] for face in rubik.cube]

    all_corner = {face.dir: [face.get_corners(
        index, rubik) for index in corner_index] for face in faces}
    white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                      if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}
    replaced_edges = []
    edges_bad_placed = [1 for face in faces if face.dir != "Up" and face.dir != "Down" if not is_final_pos_edge(
        face, rubik.cube[face.dir].get_edge((1, 0), rubik))]
    while len(list(filter(lambda elem: len(white_corner_bad_placed[elem]) > 0, white_corner_bad_placed)))\
            or len(edges_bad_placed) > 0:
        if (len(soluce_mouves) > 60):
            return None
        best_mouve = {
            "mouves": None,
            "turn": None,
            "cost": None,
            "algo": None,
            "resolve_white": None
        }
        up_mouve = random.choice(["U", "U'", "U2"]) if len(
            replaced_edges) == 0 else random.choice(["U", "U'"])
        for i in range(4 if up_mouve != "U2" else 2):
            if len(list(filter(lambda elem: len(white_corner_bad_placed[elem]) > 0, white_corner_bad_placed))):
                found_mouves = find_mouves(
                    white_corner_bad_placed, rubik)
                if len(found_mouves):
                    chosen_mouve = random.choice(found_mouves)
                    mouves = chosen_mouve[0]
                    algo_num = chosen_mouve[1]
                    best_mouve["mouves"] = copy.copy(mouves)
                    best_mouve["turn"] = i
                    best_mouve["algo"] = algo_num
                    best_mouve["cost"] = len(mouves) + (1 if i > 0 else 0)
                    best_mouve["resolve_white"] = True
                    break
            if best_mouve["mouves"] == None:
                white_corner_well_placed = [corner for corner in all_corner['Up']
                                            if corner['corner']['color'] == 'W' and is_final_pos(corner)]
                found_mouves = find_mouves_bis(
                    white_corner_well_placed, rubik)
                if len(found_mouves):
                    chosen_mouve = random.choice(found_mouves)
                    mouves = chosen_mouve[0]
                    algo_num = chosen_mouve[1]
                    best_mouve["mouves"] = copy.copy(mouves)
                    best_mouve["turn"] = i
                    best_mouve["algo"] = algo_num
                    best_mouve["cost"] = len(mouves) + (1 if i > 0 else 0)
                    break

            apply_reversed_mouves([up_mouve], rubik, visualiser)
            soluce_mouves.append(inverse_mouves_dir[up_mouve])
            all_corner = {face.dir: [face.get_corners(
                index, rubik) for index in corner_index] for face in faces}
            white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                              if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}

        for i in range(len(soluce_mouves) - 1, len(soluce_mouves) - i - 1, -1):
            soluce_mouves.pop(i)

        if (best_mouve["mouves"]):
            replaced_edges = []
            # if (best_mouve["turn"] == 1):
            #     apply_reversed_mouves(['U'], rubik, visualiser)
            #     soluce_mouves.append(inverse_mouves_dir['U'])
            # elif (best_mouve["turn"] == 2):
            #     apply_reversed_mouves(['U2'], rubik, visualiser)
            #     soluce_mouves.append(inverse_mouves_dir['U2'])
            # elif (best_mouve["turn"] == 3):
            #     apply_reversed_mouves(["U'"], rubik, visualiser)
            #     soluce_mouves.append(inverse_mouves_dir["U'"])
            apply_reversed_mouves(best_mouve["mouves"], rubik, visualiser)
            for mouve_ in best_mouve["mouves"]:
                soluce_mouves.append(inverse_mouves_dir[mouve_])

        else:
            if len(replaced_edges):
                cancel_mouves(soluce_mouves, 3, rubik, visualiser)
            replaced_edges.append(replace_edge(
                soluce_mouves, replaced_edges, rubik, visualiser))
            if None in replaced_edges:
                return None

        all_corner = {face.dir: [face.get_corners(
            index, rubik) for index in corner_index] for face in faces}
        white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                          if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}
        edges_bad_placed = [1 for face in faces if face.dir != "Up" and face.dir != "Down" if not is_final_pos_edge(
            face, rubik.cube[face.dir].get_edge((1, 0), rubik))]

    # edges = {face.dir: face.get_edge((1, 0), rubik) for face in faces if face.dir !=
    #          "Up" and face.dir != "Down" if not is_final_pos_edge(face, face.get_edge((1, 0), rubik))}
    # turn = 0
    # replaced_edges = []
    # while len(edges):
    #     placed = place_edges(soluce_mouves, edges, rubik, visualiser)
    #     edges = {face.dir: face.get_edge((1, 0), rubik) for face in faces if face.dir !=
    #              "Up" and face.dir != "Down" if not is_final_pos_edge(face, face.get_edge((1, 0), rubik))}

    #     if not placed:
    #         turn += 1
    #         if turn == 4:
    #             if len(replaced_edges):
    #                 cancel_mouves(soluce_mouves, 7, rubik, visualiser)
    #             replaced_edges.append(replace_edge(
    #                 soluce_mouves, replaced_edges, rubik, visualiser))
    #             turn = 0
    #     else:
    #         turn = 0
    #         replaced_edges = []

    # print(soluce_mouves, len(soluce_mouves))

    return soluce_mouves


def place_edges(soluce_mouves: list[str], mid_edges: dict[str, Edge], rubik: RubiksCube, visualiser: RubixVisualiser | None):
    for face in mid_edges:
        if rubik.cube[face][(1, 0)] == mid_edges[face]["face"].color\
                and mid_edges[face]["color"] == rubik.cube[face].color:
            mouves = algo.thirty_eight(face)
            apply_reversed_mouves(mouves, rubik, visualiser)
            for _mouve in mouves:
                soluce_mouves.append(inverse_mouves_dir[_mouve])
            return True

    mouves = []
    top_edges = {face: [rubik.cube[face].get_edge((2, 1), rubik)]
                 for face in ["Front", "Left", "Bottom", "Right"]}

    for face_dir in top_edges:
        for edge in top_edges[face_dir]:
            if corner := is_left_edge_well_placed(face_dir, edge, rubik):
                mouves, algo_num = algo.twenty_six(corner)
                break
            if corner := is_right_edge_well_placed(face_dir, edge, rubik):
                mouves, algo_num = algo.twenty_five(corner)
                break

    if (len(mouves) == 0):
        apply_reversed_mouves(["U"], rubik, visualiser)
        soluce_mouves.append(inverse_mouves_dir["U"])
        return False
    apply_reversed_mouves(mouves, rubik, visualiser)
    for _mouve in mouves:
        soluce_mouves.append(inverse_mouves_dir[_mouve])
    return True


def replace_edge(soluce_mouves: list[str], tried, rubik: RubiksCube, visualiser: RubixVisualiser | None, is_not_found=False):
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
        return replace_edge(soluce_mouves, tried, rubik, visualiser, is_not_found=True)

    mouves = [mouves_dir[to_mouve][sense1], "U'",
              mouves_dir[to_mouve][sense2]]
    apply_reversed_mouves(mouves, rubik, visualiser)
    for _mouve in mouves:
        soluce_mouves.append(inverse_mouves_dir[_mouve])

    return to_mouve + sense1 + ('nf' if is_not_found else '')


def cancel_mouves(soluce_mouves: list[str], count: int, rubik: RubiksCube, visualiser: RubixVisualiser | None, visualise=False):
    opposite_mouves = Opposite_mouves(rubik)
    for i in range(len(soluce_mouves) - 1, len(soluce_mouves) - count - 1, -1):
        user_continue = ""
        while (visualise and visualiser and user_continue != "y"):
            user_continue = input("Tapez y pour le prochain mouv: ")

        opposite_mouves.mouves[soluce_mouves[i]]()
        if visualiser:
            visualiser.opposite_mouves[soluce_mouves[i]](
            )
        if (visualise and visualiser):
            time.sleep(visualiser.SPEED)
        soluce_mouves.pop(i)
