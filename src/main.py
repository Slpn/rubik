import copy
import random
import sys
import threading
import time
from F2L.F2L import F2L
from OLL.OLL import OLL
from cross.resolve_cross import resolve_cross
from rubik_class import RubiksCube
from rubik_utils import apply_mouves, clear_mouves
from vizualize import RubixVisualiser, launch_vizualiser
import numpy as np
from OLL.OLL_algos import algos as OLL_algo


def mouve_visualiser(mouves: list[str], visualiser: RubixVisualiser, speed: float):
    time.sleep(1)
    visualiser.SPEED = speed
    print(mouves)
    for mouve in mouves:
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


def random_scramble(rubik: RubiksCube, visualiser: RubixVisualiser | None = None):
    test_mouves = list(rubik.mouves.keys())

    if visualiser:
        visualiser.SPEED = 0.02
    mouves_sequence = []
    for _ in range(0, 20):
        mouve = random.choice(test_mouves)
        rubik.mouves[mouve]()
        mouves_sequence.append(mouve)
        if visualiser:
            visualiser.visualizer_mouves[mouve]()
            time.sleep(visualiser.SPEED)

    mix = ' '.join(mouves_sequence)
    print(mix)
    return mouves_sequence


def test_OLL(rubik: RubiksCube):
    for rotate in [None,  "y'", "y", "y2"]:
        for i in range(1, 57):
            print("algooo", i)
            config_OLL(i, rubik, rotate)
            mouves = OLL(rubik)
            apply_mouves(mouves, rubik, None)
            rubik.pretty_print()
            if not all(all(item == 'Y' for item in row) for row in rubik.cube['Down'].array):
                print("algo", i, "not ok")
                print(mouves)
                return


def config_OLL(num: int, rubik: RubiksCube, rotate: None | str = None):
    algo = list(filter(lambda elem: elem["num"] == num, OLL_algo))[0]
    shema = algo["shema"]

    match rotate:
        case None:
            bottom = "Bottom"
            front = "Front"
            left = "Left"
            right = "Right"
        case "y'":
            bottom = "Right"
            front = "Left"
            left = "Bottom"
            right = "Front"
        case "y":
            bottom = "Left"
            front = "Right"
            left = "Front"
            right = "Bottom"
        case "y2":
            bottom = "Front"
            front = "Bottom"
            left = "Right"
            right = "Left"

    rubik.cube[bottom].array[2] = shema[0][1:4][::-1]
    rubik.cube[front].array[2] = shema[4][1:4]
    j = 0
    for i in range(1, 4):
        rubik.cube[left].array[2][j] = shema[i][0]
        rubik.cube[right].array[2][j] = shema[4 - i][4]
        j += 1

    rubik.cube["Down"].array[2] = shema[1][1:4]
    rubik.cube["Down"].array[1] = shema[2][1:4]
    rubik.cube["Down"].array[0] = shema[3][1:4]

    if rotate == "y'":
        rubik.cube["Down"].array = np.rot90(rubik.cube["Down"].array)
    elif rotate == "y":
        rubik.cube["Down"].array = np.rot90(rubik.cube["Down"].array, k=-1)
    elif rotate == "y2":
        rubik.cube["Down"].array = np.rot90(rubik.cube["Down"].array, k=-1)
        rubik.cube["Down"].array = np.rot90(rubik.cube["Down"].array, k=-1)


def resolve_rubik(rubik: RubiksCube, visualiser: RubixVisualiser | None = None):

    rubik_conf = copy.deepcopy(rubik.cube)
    mouves: list | None = None
    for _ in range(100):
        cross_mouves = resolve_cross(rubik, None)

        rubik_white_ok_cpy = copy.deepcopy(rubik.cube)

        F2L_mouves = None
        mouves2 = None
        for _ in range(10):
            F2L_mouves_tmp = F2L(rubik, None)
            OLL_mouves = OLL(rubik)
            clear_concat = clear_mouves(F2L_mouves_tmp + OLL_mouves)
            if (F2L_mouves_tmp and (mouves2 == None or len(clear_concat) < len(mouves2))):
                mouves2 = clear_concat
            rubik.cube = copy.deepcopy(rubik_white_ok_cpy)

        apply_mouves(mouves2, rubik, None, False)
        clear_concat = clear_mouves(cross_mouves + mouves2)
        if (mouves == None or (mouves2 != None and cross_mouves != None and len(clear_concat) < len(mouves))):
            mouves = clear_concat

        rubik.cube = copy.deepcopy(rubik_conf)

    print("end", len(mouves))
    rubik.soluce_mouves = clear_mouves(mouves)
    apply_mouves(rubik.soluce_mouves, rubik, None, False)

    print('Final', len(rubik.soluce_mouves))
    rubik.pretty_print()


if __name__ == "__main__":

    try:
        if len(sys.argv) != 2:
            raise AssertionError("Bad number of arguments")

        rubik = RubiksCube()

        # mix = mix_rubiks(sys.argv[1], rubik)
        mix = random_scramble(rubik)

        resolve_rubik(rubik)
       # sys.exit()

        visualiser = RubixVisualiser()
        mouve_visualiser(mix, visualiser, 0.0)

        thread_visualiser = threading.Thread(
            target=mouve_visualiser, args=[rubik.soluce_mouves, visualiser, 0.04])
        thread_visualiser.start()
        launch_vizualiser()

    except Exception as e:
        print("Error:", e)
        raise (e)

    except KeyboardInterrupt:
        visualiser.close()
        print("Canceled")
        sys.exit()
