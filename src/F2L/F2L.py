import time
import F2L.F2L_algo as algo
from F2L.F2L_filters import *
from rubik_class import Opposite_mouves, RubiksCube
from face_class import Edge, Face, check_edge_color, dir_nodes, Corner
import numpy as np
from utils import CircularChainedList, get_face_to_mouve, mouves_dir, get_new_idx, inverse_mouves_dir, y_prime_mouve_dir
from vizualize import RubixVisualiser


def F2L(rubik: RubiksCube, visualiser: RubixVisualiser):
    visualiser.SPEED = 0.08
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

    while (len(white_corner_bad_placed)):
        mouves = []

        print("en haut")

        for corner in white_corner_bad_placed:
            print("ddd", corner, "\n")
            for cube in white_corner_bad_placed[corner]:

                if is_cube_well_placed(cube):

                    print('well placed')
                    print("ccc", corner, "\n")
                    print(corner, cube)
                    if (is_cube_on_top(cube)):
                        print("is_on top")

                        if (is_i_corner_equals_color(cube)):
                            print("is_cube_well_placed_i_equal_corner")
                            time.sleep(0)
                            if (adjacent := is_adjacent_j_well_placed(cube, rubik)):
                                print("adjacent ok")
                                if (is_adjacent_well_placed_1(cube, adjacent['edge'], adjacent['idx'])):
                                    print("is_adjacent_well_placed_1")
                                    if (cube["corner"]["index"][1] == 0):
                                        mouves = algo.fourteen(cube)
                                        break
                                    if (cube["corner"]["index"][1] == 2):
                                        mouves = algo.thirteen(cube)
                                        break

                            if (is_opposite_right_well_placed(cube, rubik)):
                                print("is_opposite_right_well_placed_bis")
                                if (cube["corner"]["index"][1] == 2):
                                    mouves = algo.five(cube)
                                    break

                                if (cube["corner"]["index"][1] == 0):
                                    mouves = algo.eight(cube)
                                    break

                            if (is_opposite_right_well_placed_bis(cube, rubik)):
                                print("is_opposite_right_well_placed_bis")
                                if (cube["corner"]["index"][1] == 2):
                                    mouves = algo.nine(cube)
                                    break

                                if (cube["corner"]["index"][1] == 0):
                                    mouves = algo.four(cube)
                                    break

                            # if (is_opposite_left_well_placed_bis(cube, rubik)):
                            #     # mouve = (R U R')
                            #     mouves = ["L", "D", "L'"]
                            #     print("is_opposite_left_well_placed_bis")
                            #     break

                    if (is_cube_up_face(cube)):
                        print("is_on up face")

                        if (is_i_corner_equals_j_color(cube)):
                            print("is_i_corner_equals_j_color")
                            time.sleep(0)
                            if (adjacent := is_adjacent_bottom_well_placed(cube, rubik)):
                                print("adjacent bottom ok")
                                if (is_adjacent_bottom_well_placed_1(cube, adjacent['edge'], adjacent['idx'])):
                                    mouves = algo.thirty_one(cube)
                                    break
                            if (adjacent := is_adjacent_j_well_placed(cube, rubik)):
                                print("is_adjacent_j_well_placed")
                                if is_adjacent_well_placed_2(cube, adjacent['edge'], adjacent['idx']):
                                    mouves = algo.twenty_four
                                    break
                                if is_adjacent_well_placed_1(cube, adjacent['edge'], adjacent['idx']):
                                    if (adjacent["idx"] == (2, 1)):
                                        mouves = algo.seventeen(cube)
                                        break
                                    if (adjacent["idx"] == (0, 1)):
                                        mouves = algo.eighteen(cube)
                                        break
            if (len(mouves)):
                break

        if (len(mouves) == 0):
            turn += 1
            mouves = ["U"]
        else:
            turn = 0

        mouve_F2L(mouves, rubik, visualiser)

        all_corner = {face.dir: [face.get_corners(
            index, rubik) for index in corner_index] for face in faces}
        white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                          if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}

        if (turn >= 4):
            turn_not_found = 0
            while (found := nothing_found_1(white_corner_bad_placed, rubik, visualiser)) == False\
                    and turn_not_found < 3:
                turn_not_found += 1
                all_corner = {face.dir: [face.get_corners(
                    index, rubik) for index in corner_index] for face in faces}
                white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                                  if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}
            if (not found):
                top_edges = {face.dir: [face.get_edge((2, 1), rubik)]
                             for face in faces}
                turn_not_found = 0
                while (found := nothing_found_2(top_edges, rubik, visualiser)) == False\
                        and turn_not_found < 3:
                    top_edges = {face.dir: [face.get_edge((2, 1), rubik)]
                                 for face in faces}
                    turn_not_found += 1

            all_corner = {face.dir: [face.get_corners(
                index, rubik) for index in corner_index] for face in faces}
            white_corner_bad_placed = {face: [corner for corner in all_corner[face]
                                              if corner['corner']['color'] == 'W' and not is_final_pos(corner)]for face in all_corner}
            turn = 0

        print()


def nothing_found_1(corners: dict[str, list[Corner]], rubik: RubiksCube, visualiser: RubixVisualiser):
    print("nothing_found_1")
    mouves = []
    for face_dir in corners:
        for cube in corners[face_dir]:
            if is_cube_well_placed(cube):
                print('well placed')
                print(cube, cube)
                if (is_cube_on_top(cube)):
                    print("is_on top")
                    if (is_i_corner_equals_color(cube)):
                        if (cube["corner"]["index"][1] == 0):
                            mouves = algo.four(cube)
                            break
                        if (cube["corner"]["index"][1] == 2):
                            mouves = algo.three(cube)
                            break
                        if len(mouves):
                            break

    if (len(mouves) == 0):
        mouve_F2L(["U"], rubik, visualiser)
        return False
    mouve_F2L(mouves, rubik, visualiser)
    return True


def nothing_found_2(top_edges: dict[str, list[Edge]], rubik: RubiksCube, visualiser: RubixVisualiser):
    print("nothing_found_2")
    mouves = []
    for face_dir in top_edges:
        print(face_dir)
        for edge in top_edges[face_dir]:
            if adjacent_face := is_edge_well_placed(face_dir, edge, rubik):
                print("ho", edge["index"])
                if (edge["index"] == (2, 1)):
                    mouves = algo.twenty_six(face_dir, adjacent_face.dir)
                    break
                if (edge["index"] == (1, 2)):
                    mouves = algo.twenty_seven(adjacent_face.dir)
                    break

    if (len(mouves) == 0):
        mouve_F2L(["U"], rubik, visualiser)
        return False
    mouve_F2L(mouves, rubik, visualiser)
    return True


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
