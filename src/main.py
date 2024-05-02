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


def mouve_visualiser(mouves: list[str], visualiser: RubixVisualiser):
    time.sleep(1)
    visualiser.SPEED = 0.01
    print(mouves)
    for mouve in mouves:
        visualiser.visualizer_mouves[mouve]()
        time.sleep(visualiser.SPEED)


def mix_rubiks(mouves: str, rubik: RubiksCube, visualiser: RubixVisualiser):
    array_mouves = mouves.split()

    if len(list(filter(lambda mouve: mouve not in list(rubik.mouves.keys()), array_mouves))):
        raise AssertionError('Bad mouve provided')

    for mouve in array_mouves:
        rubik.mouves[mouve]()
        visualiser.SPEED = 0
        visualiser.visualizer_mouves[mouve]()


def random_scramble(rubik: RubiksCube, visualiser: RubixVisualiser):
    test_mouves = list(rubik.mouves.keys())

    visualiser.SPEED = 0
    mouves_sequence = []
    for _ in range(0, 20):
        mouve = random.choice(test_mouves)
        rubik.mouves[mouve]()
        mouves_sequence.append(mouve)
        visualiser.visualizer_mouves[mouve]()

    print(' '.join(mouves_sequence))


def test_mouves(visualiser: RubixVisualiser, rubik: RubiksCube,  stop_event: threading.Event):

    test_mouves = ["B2", "F'"]
    rubik.pretty_print()
    time.sleep(1)
    print(test_mouves)
    mouves_sequence = []
    for i in range(0, 2):
        if stop_event.is_set():
            return
        mouve = test_mouves[i]
        print(mouve)
        rubik.mouves[mouve]()
        rubik.pretty_print()
        mouves_sequence.append(mouve)
        visualiser.visualizer_mouves[mouve]()

    print(mouves_sequence)


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


def resolve_rubik(rubik: RubiksCube, visualiser: RubixVisualiser):

    rubik_conf = copy.deepcopy(rubik.cube)
    visualiser.SPEED = 0.0
    mouves: list | None = None
    for i in range(200):
        cross_mouves_tmp = resolve_cross(rubik, None)
        F2L_mouves_tmp = F2L(rubik, None)
        if (mouves == None or (F2L_mouves_tmp != None and cross_mouves_tmp != None and len(cross_mouves_tmp) + len(F2L_mouves_tmp) < len(mouves))):
            mouves = copy.copy(cross_mouves_tmp)+copy.copy(F2L_mouves_tmp)
        if F2L_mouves_tmp:
            print(len(cross_mouves_tmp) + len(F2L_mouves_tmp),
                  len(cross_mouves_tmp), len(F2L_mouves_tmp))
        rubik.cube = copy.deepcopy(rubik_conf)

    print("end", len(mouves))
    rubik.soluce_mouves = mouves
    apply_mouves(rubik.soluce_mouves, rubik, visualiser, False)
    time.sleep(3)

    oll_mouves = OLL(rubik)
    print("oll mouves", oll_mouves)

    for mouve in oll_mouves:
        rubik.soluce_mouves.append(mouve)

    clear_mouves(rubik)

    print('Final', len(rubik.soluce_mouves))

    visualiser.SPEED = 0.02
    apply_mouves(oll_mouves, rubik, visualiser, True)
    rubik.pretty_print()


if __name__ == "__main__":

    try:
        if len(sys.argv) != 2:
            raise AssertionError("Bad number of arguments")

        visualiser = RubixVisualiser()
        rubik = RubiksCube()

        # mix_rubiks(sys.argv[1], rubik, visualiser)
        # random_scramble(rubik, visualiser)
        test_OLL(rubik)

        # resolve_rubik_thread = threading.Thread(
        #     target=resolve_rubik, args=[rubik, visualiser])
        # resolve_rubik_thread.start()

        # launch_vizualiser()
        sys.exit()

      #  thread_test.start()
     #   thread_test.join()

  #      mouve_visualiser(cross_mouves, visualiser)
        # F2L_thread = threading.Thread(target=F2L, args=[rubik, visualiser])
        # time.sleep(5)
        # F2L_thread.start()

        # F2L(rubik, None)

        thread_visualiser = threading.Thread(
            target=mouve_visualiser, args=[rubik.soluce_mouves, visualiser])
        thread_visualiser.start()
        launch_vizualiser()

      #  resolve_cross(rubik, visualiser)

        # thread.join()

    except Exception as e:
        print("Error:", e)
        raise (e)

    except KeyboardInterrupt:
        visualiser.close()
        print("Canceled")
        sys.exit()
