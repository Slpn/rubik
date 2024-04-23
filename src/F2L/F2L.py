import time
import F2L.F2L_algo as algo
from F2L.F2L_filters import *
from rubik_class import Opposite_mouves, RubiksCube
from face_class import Edge, Face, check_edge_color, dir_nodes, Corner
import numpy as np
from utils import CircularChainedList, get_face_to_mouve, mouves_dir, get_new_idx, inverse_mouves_dir, y_prime_mouve_dir
from vizualize import RubixVisualiser


def F2L(rubik: RubiksCube, visualiser: RubixVisualiser):
    visualiser.SPEED = 0.02
    corner_index = [(0, 0), (0, 2), (2, 0), (2, 2)]
    faces = [rubik.cube[face] for face in rubik.cube]
    all_corner = {face.dir: [face.get_corners(
        index, rubik) for index in corner_index] for face in faces}

    white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                      if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}

    # for corner in white_corner_bad_placed:
    #     for elem in white_corner_bad_placed[corner]:
    #         print(corner, ":", elem, is_adjacent_left_well_placed(elem))
    #     print()
    turn = 0
    replaced_edges = []
    while len(list(filter(lambda elem: len(white_corner_bad_placed[elem]) > 0, white_corner_bad_placed))):
        mouves = []

        print("en haut", white_corner_bad_placed)

        for corner in white_corner_bad_placed:
            print("ddd", corner, "\n")
            for cube in white_corner_bad_placed[corner]:
                print("WHITE CORNER", cube)
                if is_cube_well_placed(cube):

                    # print('well placed')
                    # print("ccc", corner, "\n")
                    # print(corner, cube)
                    if (is_cube_on_top(cube)):
                        # print("is_on top")

                        if (is_i_corner_equals_color(cube)):
                            # print("is_cube_well_placed_i_equal_corner")
                            if (adjacent := is_adjacent_well_placed(cube, rubik)):
                                # print("adjacent ok")
                                # print("case", adjacent["case"])
                                if (adjacent["case"] == 1):
                                    print("is_adjacent_well_placed_1")
                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.fourteen(cube)
                                        break
                                    if (cube["corner"]["index"][1] == 2):
                                        mouves = algo.thirteen(cube)
                                        break
                                if (adjacent["case"] == 2):
                                    # print("is_adjacent_well_placed_2")
                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.sixteen(cube)
                                        break
                                    if (cube["corner"]["index"][1] == 2):
                                        mouves = algo.fifteen(cube)
                                        break

                            if (adjacent := is_adjacent_j_well_placed(cube, rubik)):
                                if (adjacent["case"] == 1):
                                    # print("is_adjacent_well_placed_2")
                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.two(cube)
                                        break
                                    if (cube["corner"]["index"][1] == 2):
                                        mouves = algo.one(cube)
                                        break
                                if (adjacent["case"] == 2):
                                    # print("is_adjacent_well_placed_2")
                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.twelve(cube)
                                        break
                                    if (cube["corner"]["index"][1] == 2):
                                        mouves = algo.eleven(cube)
                                        break

                            if (opopsite_case := is_opposite_right_well_placed(cube, rubik)):
                                if opopsite_case == 1:
                                    if (cube["corner"]["index"][1] == 2):
                                        mouves = algo.five(cube)
                                        break

                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.eight(cube)
                                        break

                                if opopsite_case == 2:
                                    if (cube["corner"]["index"][1] == 2):
                                        mouves = algo.nine(cube)
                                        break

                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.four(cube)
                                        break
                            if (adjacent := is_adjacent_bottom_well_placed(cube, rubik)):
                                if (adjacent["case"] == 1):
                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.thirty_four(cube)
                                        break
                                    elif (cube["corner"]["index"][1] == 2):
                                        pass
                                        mouves = algo.thirty_three(cube)
                                        break
                                elif (adjacent["case"] == 2):
                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.thirty_six(cube)
                                        break
                                    elif (cube["corner"]["index"][1] == 2):
                                        pass
                                        mouves = algo.thirty_five(cube)
                                        break

                            if (opopsite_case := is_opposite_left_well_placed(cube, rubik)):
                                if opopsite_case == 1:
                                    if (cube["corner"]["index"][1] == 2):
                                        mouves = algo.seven(cube)
                                        break
                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.ten(cube)
                                        break
    
                                if opopsite_case == 2:
                                    if (cube["corner"]["index"][1] == 2):
                                        mouves = algo.three(cube)
                                        break

                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.six(cube)
                                        break


                    if (is_cube_up_face(cube)):
                        # print("is_on up face")

                        if (is_i_corner_equals_j_color(cube)):
                            # print("is_i_corner_equals_j_color")
                            time.sleep(0)
                            if (adjacent := is_adjacent_bottom_well_placed(cube, rubik)):
                                print("adjacent bottom ok")
                                if (adjacent["case"] == 1):
                                    mouves = algo.thirty_one(cube)
                                    break
                                elif (adjacent["case"] == 2):
                                    mouves = algo.thirty_two(cube)
                                    break
                            if (adjacent := is_adjacent_well_placed(cube, rubik)):
                                print("is_adjacent_well_placed")
                                if adjacent["case"] == 2:
                                    mouves = algo.twenty_four(cube)
                                    break
                                elif adjacent["case"] == 1:
                                    mouves = algo.seventeen(cube)
                                    break
                            if (adjacent := is_adjacent_j_well_placed(cube, rubik)):
                                if adjacent["case"] == 2:
                                    mouves = algo.eighteen(cube)
                                    break
                                elif adjacent["case"] == 1:
                                    mouves = algo.twenty_three(cube)
                                    break

                            if opposite := is_opposite_right_well_placed(cube, rubik, on_top=True):
                                # print(opposite)
                                # print(cube["corner"]["face"].dir)
                                # print(cube["corner_i"]["color"])
                                # print(cube["corner_j"]["color"])
                                if opposite == 1:
                                    mouves = algo.twenty_two(cube)
                                    break

                    if is_cube_on_bottom(cube):
                        print("cube on bottom")

                        if right_edge := right_edge_well_placed(cube, rubik):
                            print(right_edge)
                            if right_edge == 1:
                                mouves = algo.twenty_seven(cube)
                                break
                            elif right_edge == 2:
                                mouves = algo.thirty(cube)
                                break
                        

            if (len(mouves)):
                break

        if (len(mouves) == 0):
            turn += 1
            mouves = ["U"]
        else:
            turn = 0
            replaced_edges = []

        mouve_F2L(mouves, rubik, visualiser)

        all_corner = {face.dir: [face.get_corners(
            index, rubik) for index in corner_index] for face in faces}
        white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                          if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}

        if (turn >= 4):
            turn_not_found = 0
            if len(replaced_edges):
                cancel_mouves(7, rubik, visualiser)
            replaced_edges.append(replace_edge(
                replaced_edges, rubik, visualiser))
            # else:
            #     while (found := nothing_found_1(white_corner_bad_placed, rubik, visualiser)) == False\
            #             and turn_not_found < 3:
            #         turn_not_found += 1
            #         all_corner = {face.dir: [face.get_corners(
            #             index, rubik) for index in corner_index] for face in faces}
            #         white_corner_bad_placed = {face: [corner for corner in all_corner[face]
            #                                           if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}
            #     if (not found):
            #         print("replace edge")
            #         replaced_edges.append(replace_edge(
            #             replaced_edges, rubik, visualiser))
            #         turn = 0
            #         print("found", found)
            # if (not found):
            #     top_edges = {face.dir: [face.get_edge((2, 1), rubik)]
            #                  for face in faces if face.dir != "Down"}
            #     turn_not_found = 0
            #     while (found := nothing_found_2(top_edges, rubik, visualiser)) == False\
            #             and turn_not_found < 3:
            #         top_edges = {face.dir: [face.get_edge((2, 1), rubik)]
            #                      for face in faces if face.dir != "Down"}
            #         turn_not_found += 1

            all_corner = {face.dir: [face.get_corners(
                index, rubik) for index in corner_index] for face in faces}
            white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                              if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}
            turn = 0

        print()

    print("CORNERS OK")

    edges = [1 for face in faces if face.dir != "Up" and face.dir != "Down" if not is_final_pos_edge(
        face, rubik.cube[face.dir].get_edge((1, 0), rubik))]

    while len(edges):
        top_edges = {face.dir: [face.get_edge((2, 1), rubik)]
                     for face in faces if face.dir != "Down"}
        if last_algo := select_f2l_algorithm(cube, rubik):
            match last_algo:
                case 38:
                    mouves = algo.thirty_eight(cube)
                case 39:
                    mouves = algo.thirty_nine(cube)
                case 40:
                    mouves = algo.fourty(cube)
                case 41:
                    mouves = algo.fourty_one(cube)
                case 42:
                    mouves = algo.fourty_two(cube)
            break
        place_edges(top_edges, rubik, visualiser)
        edges = [1 for face in faces if face.dir != "Up" and face.dir != "Down" if not is_final_pos_edge(
            face, rubik.cube[face.dir].get_edge((1, 0), rubik))]

    print("EENND")


# def nothing_found_1(corners: dict[str, list[Corner]], rubik: RubiksCube, visualiser: RubixVisualiser):
#     print("nothing_found_1")
#     mouves = []
#     for face_dir in corners:
#         for cube in corners[face_dir]:
#             if is_cube_well_placed(cube):
#                 print('well placed')
#                 print(cube, cube)
#                 if (is_cube_on_top(cube)):
#                     print("is_on top")
#                     if (is_i_corner_equals_color(cube)):
#                         if (cube["corner"]["index"][1] == 0):
#                             mouves = algo.four(cube)
#                             break
#                         if (cube["corner"]["index"][1] == 2):
#                             mouves = algo.three(cube)
#                             break
#                         if len(mouves):
#                             break

#     if (len(mouves) == 0):
#         mouve_F2L(["U"], rubik, visualiser)
#         return False
#     mouve_F2L(mouves, rubik, visualiser)
#     return True


def place_edges(top_edges: dict[str, list[Edge]], rubik: RubiksCube, visualiser: RubixVisualiser):
    print("nothing_found_2")
    mouves = []
    for face_dir in top_edges:
        print(face_dir)
        for edge in top_edges[face_dir]:
            if adjacent_face := is_left_edge_well_placed(face_dir, edge, rubik):
                print("ho", edge["index"])
                mouves = algo.twenty_six(face_dir, adjacent_face.dir)
                break
            if adjacent_face := is_right_edge_well_placed(face_dir, edge, rubik):
                print("hi", edge["index"])
                mouves = algo.twenty_seven(adjacent_face.dir)
                break
        if len(mouves):
            break

    if (len(mouves) == 0):
        mouve_F2L(["U"], rubik, visualiser)
        return False
    mouve_F2L(mouves, rubik, visualiser)
    return True


def replace_edge(tried, rubik: RubiksCube, visualiser: RubixVisualiser):
    sense1 = None
    sense2 = None
    faces = ["Front", "Left", "Bottom", "Right"]
    for face in faces:
        if (face + "+" not in tried and not is_chunck_resolved(face, "+", rubik)):
            to_mouve = face
            sense1 = "+"
            sense2 = "-"
            break

        elif (face + "-" not in tried and not is_chunck_resolved(face, "-", rubik)):
            to_mouve = face
            sense1 = "-"
            sense2 = "+"
            break

    mouve_F2L([mouves_dir[to_mouve][sense1], "U'",
              mouves_dir[to_mouve][sense2]], rubik, visualiser)
    return to_mouve + sense1


def mouve_F2L(mouves: list[str], rubik: RubiksCube, visualiser: RubixVisualiser):
    print(mouves)
    for mouve in mouves:
        user_continue = ""
        while (user_continue != "y"):
            user_continue = input("Tapez y pour le prochain mouv: ")

        rubik.mouves[inverse_mouves_dir[mouve]]()
        visualiser.visualizer_mouves[inverse_mouves_dir[mouve]]()
        time.sleep(visualiser.SPEED)
        rubik.soluce_mouves.append(inverse_mouves_dir[mouve])


def cancel_mouves(count: int, rubik: RubiksCube, visualiser: RubixVisualiser):
    opposite_mouves = Opposite_mouves(rubik)
    print(rubik.soluce_mouves[len(
        rubik.soluce_mouves) - count:len(rubik.soluce_mouves)])
    for i in range(len(rubik.soluce_mouves) - 1, len(rubik.soluce_mouves) - count - 1, -1):
        print('cancel mouves', rubik.soluce_mouves[i])
        user_continue = ""
        while (user_continue != "y"):
            user_continue = input("Tapez y pour le prochain mouv: ")

        opposite_mouves.mouves[rubik.soluce_mouves[i]]()
        visualiser.opposite_mouves[rubik.soluce_mouves[i]](
        )
        time.sleep(visualiser.SPEED)
        rubik.soluce_mouves.pop(i)
