import time
from rubik_class import Opposite_mouves, RubiksCube
from face_class import Edge, Face, check_edge_color, dir_nodes
import numpy as np
from utils import CircularChainedList, get_face_to_mouve, mouves_dir, get_new_idx
from vizualize import RubixVisualiser
import random


def resolve_cross(rubik: RubiksCube, visualiser: RubixVisualiser):
    cross_idx = [(0, 1), (1, 2), (2, 1), (1, 0)]
    visualiser.SPEED = 0.1
    opposite_mouves = Opposite_mouves(rubik)
    cross_face = rubik.cube['Up']
    other_faces = [rubik.cube[other_face]
                   for other_face in rubik.cube if other_face != cross_face.dir]

    cross_mouves = []

    def free_cross(face_dir: str):
        i, j = None, None
        match face_dir:
            case 'Right':
                i, j = 1, 2
            case 'Left':
                i, j = 1, 0
            case 'Bottom':
                i, j = 0, 1
            case 'Front':
                i, j = 2, 1
            case _:
                return
        if (cross_face[(i, j)] != cross_face.color):
            return
        for mouve in mouves_dir[cross_face.dir]:
            rubik.mouves[mouves_dir[cross_face.dir][mouve]]()
            # visualiser.visualizer_mouves[mouves_dir[cross_face.dir][mouve]]()
            # time.sleep(visualiser.SPEED)
            if (cross_face[(i, j)] == cross_face.color):
                opposite_mouves.mouves[mouves_dir[cross_face.dir][mouve]]()
                # visualiser.opposite_mouves[mouves_dir[cross_face.dir][mouve]]()
                # time.sleep(visualiser.SPEED)
            else:
                cross_mouves.append(mouves_dir[cross_face.dir][mouve])
                return

    def mouve_face(face: Face, index: tuple, disable_opposite=False):
        for mouve in mouves_dir[face.dir]:
            if (disable_opposite and mouve == "opposite"):
                continue
            rubik.mouves[mouves_dir[face.dir][mouve]]()
            # visualiser.visualizer_mouves[mouves_dir[face.dir][mouve]]()
            # time.sleep(visualiser.SPEED)
            new_index = get_new_idx(index, mouve)
            edge = face.get_edge(new_index, rubik)
            if (mouve != '-' and edge['face'].color != edge['color']):
                opposite_mouves.mouves[mouves_dir[face.dir][mouve]]()
                # visualiser.opposite_mouves[mouves_dir[face.dir][mouve]]()
                # time.sleep(visualiser.SPEED)
            else:
                cross_mouves.append(mouves_dir[face.dir][mouve])
                return new_index

    def shift_cross(face: Face, idx):
        colors_boucle = CircularChainedList(['B', 'R', 'G', 'O']).head_node
        edge = face.get_edge(idx, rubik)

        if (colors_boucle[edge['color']][1].value == edge['face'].color):
            colors_boucle = colors_boucle[-1]
            color_order = [colors_boucle[i].value for i in range(4)]

        elif (colors_boucle[edge['color']][-1].value == edge['face'].color):
            colors_boucle = colors_boucle[1]
            color_order = [colors_boucle[i].value for i in range(4)]
        else:
            colors_boucle = colors_boucle[2]
            color_order = [colors_boucle[i].value for i in range(4)]

        replace_cross(color_order)

    def place_on_cross(face: Face, idx: tuple, edge_ok=False):
        to_mouve = get_face_to_mouve(face.dir, idx)
        if edge_ok:
            replace_cross()
        else:
            if (to_mouve == 'Up' or to_mouve == 'Down'):
                free_cross(face.dir)
                idx = mouve_face(face, idx, True)
                edge_ok = check_edge_color(face, idx, rubik)
                to_mouve = get_face_to_mouve(face.dir, idx)
                if edge_ok:
                    replace_cross()
            if not edge_ok:
                shift_cross(rubik.cube[face.dir], idx)
                to_mouve = get_face_to_mouve(face.dir, idx)

        color = face.get_edge(idx, rubik)['color']
        for mouve in mouves_dir[to_mouve]:
            rubik.mouves[mouves_dir[to_mouve][mouve]]()
            # visualiser.visualizer_mouves[mouves_dir[to_mouve][mouve]]()
            # time.sleep(visualiser.SPEED)
            edges = [cross_face.get_edge(
                _idx, rubik) for _idx in cross_idx if cross_face[_idx] == cross_face.color]
            is_in_cross = list(
                filter(lambda edge: edge['color'] == color, edges))
            if len(is_in_cross) == 0:
                opposite_mouves.mouves[mouves_dir[to_mouve][mouve]]()
                # visualiser.opposite_mouves[mouves_dir[to_mouve][mouve]]()
                # time.sleep(visualiser.SPEED)
            else:
                cross_mouves.append(mouves_dir[to_mouve][mouve])
                break

    def is_cross_sorted() -> tuple | None:
        """
        Return true if the cross cube on the front are sorted
        """
        colors_boucle = CircularChainedList(['B', 'R', 'G', 'O']).head_node
        cross_cubes = [idx if cross_face[idx]
                       == cross_face.color else None for idx in cross_idx]
        if (len(list(filter(lambda elem: elem != None, cross_cubes))) < 2):
            return None
        counter = {index: 1 for index in cross_cubes if index != None}
        for idx in range(0, 4):
            if (cross_cubes[idx] != None):
                edge = cross_face.get_edge(cross_cubes[idx], rubik)
                colors_boucle = colors_boucle[edge["color"]]
                for i in range(1, 4):
                    j = idx + i if idx + i < 4 else abs(4 - (idx + i))
                    colors_boucle = colors_boucle.next
                    if (cross_cubes[j] != None):
                        edge = cross_face.get_edge(cross_cubes[j], rubik)
                        if (colors_boucle.value == edge["color"]):
                            counter[cross_cubes[idx]] += 1
                        else:
                            break

        for idx in counter:
            if (counter[idx] == 1):
                return idx
        return None

    def replace_cross(color_order=None):

        cross_cubes = [
            cross_face[index] for index in cross_idx]
        if color_order:
            bad_placed = [cross_cubes[i] for i in range(4) if cross_cubes[i] == cross_face.color and cross_face.get_edge(
                cross_idx[i], rubik)["color"] != color_order[i]]
        else:
            bad_placed = [cross_cubes[i] for i in range(
                4) if cross_cubes[i] == cross_face.color and not check_edge_color(cross_face, cross_idx[i], rubik)]

        if len(bad_placed) == 0:
            return

        for mouve in mouves_dir[cross_face.dir]:
            rubik.mouves[mouves_dir[cross_face.dir][mouve]]()
            # visualiser.visualizer_mouves[mouves_dir[cross_face.dir][mouve]]()
            # time.sleep(visualiser.SPEED)
            cross_cubes = [
                cross_face[index] for index in cross_idx]
            if color_order:
                bad_placed = [cross_cubes[i] for i in range(4) if cross_cubes[i] == cross_face.color and cross_face.get_edge(
                    cross_idx[i], rubik)["color"] != color_order[i]]
            else:
                bad_placed = [cross_cubes[i] for i in range(
                    4) if cross_cubes[i] == cross_face.color and not check_edge_color(cross_face, cross_idx[i], rubik)]
            if len(bad_placed) > 0:
                opposite_mouves.mouves[mouves_dir[cross_face.dir][mouve]]()
                # visualiser.opposite_mouves[mouves_dir[cross_face.dir][mouve]]()
                # time.sleep(visualiser.SPEED)
            else:
                cross_mouves.append(mouves_dir[cross_face.dir][mouve])
                return

    well_placed = [
        idx for idx in cross_idx if cross_face.array[idx[0]][idx[1]] == cross_face.color and check_edge_color(cross_face, idx, rubik)]

    while (len(well_placed) != 4):
        random.shuffle(other_faces)
        for face in other_faces:
            do_break = False
            not_placed = is_cross_sorted()
            while (not_placed):
                to_mouve = get_face_to_mouve(cross_face.dir, not_placed)
                mouve_face(rubik.cube[to_mouve], not_placed)
                not_placed = is_cross_sorted()
            for idx in cross_idx:
                if face.array[idx[0]][idx[1]] == cross_face.color and check_edge_color(face, idx, rubik):
                    # time.sleep(5)
                    place_on_cross(face, idx, True)
                    do_break = True
                    break
            if do_break:
                break
            for face in other_faces:
                do_break = False
                not_placed = is_cross_sorted()
                while (not_placed):
                    to_mouve = get_face_to_mouve(cross_face.dir, not_placed)
                    mouve_face(rubik.cube[to_mouve], not_placed)
                    not_placed = is_cross_sorted()
                for idx in cross_idx:
                    if face.array[idx[0]][idx[1]] == cross_face.color:
                        place_on_cross(
                            face, idx, check_edge_color(face, idx, rubik))
                        do_break = True
                        break
                if do_break:
                    break
            if do_break:
                break

        cross_cubes = [
            idx for idx in cross_idx if cross_face.array[idx[0]][idx[1]] == cross_face.color]
        if (len(cross_cubes) == 4):
            replace_cross()
        well_placed = [
            idx for idx in cross_idx if cross_face.array[idx[0]][idx[1]] == cross_face.color and check_edge_color(cross_face, idx, rubik)]

    print('Cross OK', len(cross_mouves))
    return cross_mouves
