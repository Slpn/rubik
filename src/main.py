import copy
import curses
import heapq
import random
import sys
import threading
import time
from F2L.F2L5 import F2L
from OLL.OLL import OLL
from PLL.PLL import PLL
from cross.resolve_cross import resolve_cross
from rubik_class import RubiksCube
from rubik_utils import apply_mouves, clear_mouves
from utils import get_options
from vizualize import RubixVisualiser, launch_vizualiser
import numpy as np
from OLL.OLL_algos import algos as OLL_algo


def mouve_visualiser(mouves: list[str], visualiser: RubixVisualiser, speed: float, auto_visualise=True):
    time.sleep(2)
    print(ord('y'))
    visualiser.SPEED = speed
    for mouve in mouves:
        print(mouve)
        user_continue = " "
        while (not auto_visualise and ord(user_continue) != 97):
            user_continue = input("Tapez y pour le prochain mouv: ")
        visualiser.visualizer_mouves[mouve]()
        time.sleep(visualiser.SPEED)


def mix_rubiks(mouves: str, rubik: RubiksCube, visualiser: RubixVisualiser | None = None):
    array_mouves = mouves.split()

    if len(list(filter(lambda mouve: mouve not in list(rubik.mouves.keys()), array_mouves))):
        raise AssertionError('Bad mouve provided')
    if visualiser:
        visualiser.SPEED = 0.02
    for mouve in array_mouves:
        rubik.mouves[mouve]()
        if visualiser:
            visualiser.visualizer_mouves[mouve]()
    return array_mouves


def random_scramble(rubik: RubiksCube, visualiser: RubixVisualiser | None = None, mouves=20):
    test_mouves = list(rubik.mouves.keys())

    if visualiser:
        visualiser.SPEED = 0.02
    mouves_sequence = []
    for _ in range(0, mouves):
        mouve = random.choice(test_mouves)
        rubik.mouves[mouve]()
        mouves_sequence.append(mouve)
        if visualiser:
            visualiser.visualizer_mouves[mouve]()
            time.sleep(visualiser.SPEED)

    return mouves_sequence


def resolve_rubik(rubik: RubiksCube, visualiser: RubixVisualiser | None = None, explored_cross: set = None, max_iter=400, stop_50=False):

    rubik_conf = copy.deepcopy(rubik.cube)
    mouves: list | None = None
    i = 0

    mouves = None

    if (explored_cross == None):
        explored_cross = set()

    i = 0

    cross_mouves = None
    cross_conf = None

    while (mouves == None or i < max_iter):
        if stop_50 and mouves and len(mouves) < 50:
            break

        cross_mouves_tmp = clear_mouves(
            resolve_cross(rubik, None))
        if (cross_mouves_tmp == None):
            rubik.cube = copy.deepcopy(rubik_conf)
            i += 1
            continue

        conf = " ".join((np.array(rubik.get_cube_array())).flatten())
        if conf == cross_conf and len(cross_mouves_tmp) < len(cross_mouves):
            cross_mouves = cross_mouves_tmp

        explored = next(
            (element for element in explored_cross if element[1] == conf), None)
        if explored:
            rubik.cube = copy.deepcopy(rubik_conf)
            i += 1
            continue
        else:
            explored_cross.add(tuple((" ".join(cross_mouves_tmp), conf)))

        cross_ok = copy.deepcopy(rubik.cube)
        closed_set_F2L = set()
        open_set_F2L:  heapq = []
        for _ in range(25):

            F2L_mouves = F2L(rubik, open_set_F2L, closed_set_F2L, None)
            if (F2L_mouves == None):
                rubik.cube = copy.deepcopy(cross_ok)
                i += 1
                continue
            if not rubik.check_F2L():
                raise Exception("F2L not OK")

            OLL_mouves = OLL(rubik)
            if not rubik.check_OLL():
                raise Exception("OLL not OK")

            PLL_mouves = PLL(rubik)
            if not rubik.check_solved():
                rubik.pretty_print()
                raise Exception("PLL not OK")

            clear_concat = clear_mouves(
                F2L_mouves + OLL_mouves + PLL_mouves)
            mouves_tmp = copy.copy(clear_mouves(
                cross_mouves_tmp + clear_concat))
            if mouves == None or len(mouves_tmp) < len(mouves):
                cross_mouves = cross_mouves_tmp
                cross_conf = conf
                mouves = mouves_tmp
            if stop_50 and mouves and len(mouves) < 50:
                break

            rubik.cube = copy.deepcopy(cross_ok)
            i += 1

        rubik.cube = copy.deepcopy(rubik_conf)

        i += 1

   # rubik.pretty_print()
    if stop_50:
        return mouves
    rubik.soluce_mouves = mouves
    j = 0
    explored_rand = set()
    while len(rubik.soluce_mouves) > 50 and j < 15:
        rand_mouves = random_scramble(rubik, None, 2)
        if ' '.join(rand_mouves) in explored_rand:
            rubik.cube = copy.deepcopy(rubik_conf)
            j += 1
            continue
        explored_rand.add(' '.join(rand_mouves))

        new_mouves = rand_mouves + \
            resolve_rubik(rubik, visualiser, None, 20, stop_50=True)
        if len(new_mouves) < len(rubik.soluce_mouves):
            rubik.soluce_mouves = new_mouves
        rubik.cube = copy.deepcopy(rubik_conf)
        j += 1

    apply_mouves(rubik.soluce_mouves, rubik, None, False)

    return rubik.soluce_mouves


if __name__ == "__main__":
    global mix
    try:

        rubik = RubiksCube()

        generate, generated_lenght, visualise, visualise_mix, auto_visualise, count = get_options(
            sys.argv)

        if generate:
            mix = random_scramble(rubik, None, generated_lenght)
        else:
            mix = mix_rubiks(sys.argv[count + 1], rubik, None)

        resolve_rubik(rubik, None)

        if (not rubik.check_solved()):
            raise Exception('The rubik is not solved')
        print(' '.join(rubik.soluce_mouves))

        if visualise:
            visualiser = RubixVisualiser()
            mouve_visualiser(
                mix, visualiser,  0.0 if not visualise_mix else 0.04, auto_visualise)

            thread_visualiser = threading.Thread(
                target=mouve_visualiser, args=[rubik.soluce_mouves, visualiser, 0.04, auto_visualise])
            thread_visualiser.start()
            launch_vizualiser()

        sys.exit(0)

    except Exception as e:
        print("Error:", e)
    #    sys.exit(-2)
        raise (e)

    except KeyboardInterrupt:
        visualiser.close()
        print("Canceled")
sys.exit()
