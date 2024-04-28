import copy
import random
import sys
import threading
import time
from F2L.F2L import F2L
from cross.resolve_cross import resolve_cross
from rubik_class import RubiksCube
from vizualize import RubixVisualiser, launch_vizualiser


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


if __name__ == "__main__":

    try:
        if len(sys.argv) != 2:
            raise AssertionError("Bad number of arguments")

        visualiser = RubixVisualiser()
        rubik = RubiksCube()

        # mix_rubiks(sys.argv[1], rubik, visualiser)
        random_scramble(rubik, visualiser)
        rubik.pretty_print()

        rubik_conf = copy.deepcopy(rubik.cube)

        cross_mouves = None
        for i in range(10):
            cross_mouves_tmp = resolve_cross(rubik, visualiser)
            if (cross_mouves == None or len(cross_mouves_tmp) < len(cross_mouves)):
                cross_mouves = copy.copy(cross_mouves_tmp)
            rubik.cube = copy.deepcopy(rubik_conf)

        print('final', len(cross_mouves))
        for elem in cross_mouves:
            rubik.soluce_mouves.append(elem)

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
