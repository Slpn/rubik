import random
import sys
import threading
import time
from WorkerThreadClass import WorkerThread
from rubik_class import RubiksCube
from rubix_types import Faces
from vizualize import RubixVisualiser, launch_vizualiser
from vispy import app
import numpy as np


def test_mouves(visualiser: RubixVisualiser,  stop_event: threading.Event):

    cube = RubiksCube()
    test_mouves = list(cube.mouves.keys())
    print(test_mouves)
    cube.pretty_print()
    time.sleep(1)

    mouves_sequence = []
    for _ in range(0, 10):
        if stop_event.is_set():
            return
        mouve = random.choice(test_mouves)
        print(mouve)
        cube.mouves[mouve]()
        cube.pretty_print()
        mouves_sequence.append(mouve)
        visualiser.visualizer_mouves[mouve]()

    print(mouves_sequence)


if __name__ == "__main__":

    try:

        visualizer = RubixVisualiser()
        stop_event = threading.Event()
        thread = threading.Thread(target=test_mouves, args=[
                                  visualizer, stop_event])
        thread.start()
        launch_vizualiser()
        thread.join()

    except KeyboardInterrupt:
        visualizer.close()
        stop_event.set()
        print("Canceled")
        sys.exit()
