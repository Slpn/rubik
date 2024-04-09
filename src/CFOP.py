

import time
from rubik_class import Opposite_mouves, RubiksCube
from faceClass import Edge, Face, dir_nodes
import numpy as np
from utils import get_face_to_mouve, mouves_dir
from vizualize import RubixVisualiser


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


def resolve_cross(rubix: RubiksCube, visualiser: RubixVisualiser):

    def place_almost(cross_face: Face, almost_face: str, idx:  tuple):
        opposite_mouves = Opposite_mouves(rubix)
        to_mouve = get_face_to_mouve(almost_face, idx)
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

    def get_new_idx(idx: tuple, sense: str):
        i, j = idx[0], idx[1]
        print('ij', i, j, 'sense', sense)
        match sense:
            case '+':
                i += 1 if i < 2 else -1
                j -= 1 if j > 0 else -1

            case '-':
                i -= 1 if i > 0 else -1
                j += 1 if j < 2 else -1

            case 'opposite':
                if i == 0:
                    i = 2
                elif i == 2:
                    i = 0
                if j == 0:
                    j = 2
                elif j == 2:
                    j = 0
        return (i, j)

    def find_good_mouve(bad_placed: str, indexes: list[tuple]):
        print('bad placed', bad_placed)
        print(mouves_dir[bad_placed])

        current_face = rubix.cube[bad_placed]
        for index in indexes:
            for sense in mouves_dir[bad_placed]:
                rubix.mouves[mouves_dir[bad_placed][sense]]()
                visualiser.visualizer_mouves[mouves_dir[bad_placed][sense]]()
                time.sleep(visualiser.SPEED)
                new_idx = get_new_idx(index, sense)
                new_edge = current_face.get_edge(new_idx, rubix)
                if (new_edge['face'].color == current_face.color):
                    rubix.soluce_mouves.append[mouves_dir[face.dir][sense]]()
                    place_almost(cross_face, bad_placed, index)

                else:
                    opposite_mouves.mouves[mouves_dir[bad_placed][sense]]()
                    visualiser.opposite_mouves[mouves_dir[bad_placed][sense]]()
                    time.sleep(visualiser.SPEED)

        print(rubix.soluce_mouves)

    def get_to_place(face: Face):
        other_faces = [rubix.cube[other_face]
                       for other_face in rubix.cube if other_face != face.dir]
        almost_well_placed = {other_face.dir: [idx for idx in cross_idx if other_face.array[idx[0]][idx[1]] == face.color]
                              for other_face in other_faces}
        almost_bad_placed = {other_face.dir: [] for other_face in other_faces}

        for face_dir in almost_well_placed:
            to_remove = []
            colors_edges = face.get_4_edges_color(face_dir)

           # print(face_dir)
          #  print(colors_edges)
            for idx in almost_well_placed[face_dir]:
                edge: Edge = rubix.cube[face_dir].get_edge(idx, rubix)
                edge_color = edge["face"].array[edge["index"]
                                                [0]][edge["index"][1]]

                print('face dir ', face_dir, 'edge',
                      edge_color, edge["face"].color)
               # print(idx, edge_color)
                if edge_color != edge["face"].color:
                    almost_bad_placed[face_dir].append(idx)
                    to_remove.append(idx)
            for i in to_remove:
                almost_well_placed[face_dir].remove(i)

            return almost_well_placed, almost_bad_placed

    def get_face_cost(face: Face):

        well_placed = [
            idx for idx in cross_idx if face.array[idx[0]][idx[1]] == face.color]
        to_remove = []
        for well in well_placed:
            edge = face.get_edge(well, rubix)
            if (edge['face'].array[edge["index"][0]][edge["index"][1]] != edge['face'].color):
                to_remove.append(well)
        for elem in to_remove:
            well_placed.remove(elem)

        other_faces = [rubix.cube[other_face]
                       for other_face in rubix.cube if other_face != face.dir]
        almost_well_placed, almost_bad_placed = get_to_place(face)

        len_almost_well = sum([len(array)
                              for array in list(almost_well_placed.values())])
        len_almost_bad = sum([len(array)
                              for array in list(almost_bad_placed.values())])

        estimated_cost = len(well_placed) * 2 + \
            len_almost_well * 3
        return {"face": face.dir, "point": estimated_cost, "well": well_placed, "almost": almost_well_placed, "almost_bad": almost_bad_placed}

    print("res cross")
    # Index witch compose the cross
    cross_idx = [(0, 1), (1, 0), (1, 2), (2, 1)]
    best_face = None

    # Check witch face we'll put the cross on (default 'Up'), regarding the number of mouve required by face
    for face in rubix.cube:
        find_best_cross = get_face_cost(rubix.cube[face])
        if (best_face == None or find_best_cross["point"] > best_face["point"]):
            best_face = find_best_cross
        print(face)
        # print(best_face)
        # print()

    print(best_face)
    cross_face = rubix.cube[best_face['face']]
    visualiser.SPEED = 0.2

    for dir in best_face['almost']:
        for idx in best_face['almost'][dir]:
            print("plaaace", dir)
            time.sleep(15)
            place_almost(cross_face, dir, idx)

    print("all baf")
    # time.sleep(15)
    # for bad_placed in best_face["almost_bad"]:
    #     find_good_mouve(rubix.cube[best_face['face']],
    #                     bad_placed, best_face['almost_bad'][bad_placed])
