import random
import threading
import time
from WorkerThreadClass import WorkerThread
from rubik_class import RubiksCube
from rubix_types import Faces
from vizualize import RubixVisualiser, launch_vizualiser
from vispy import app
import numpy as np


def test_mouves(visualiser: RubixVisualiser):
    test_mouves = ["F", "F'", "B", "B'", 'L']

    cube = RubiksCube()
    cube.pretty_print()
    time.sleep(1)
    seq = ["B'", 'F', "B'", 'B', 'L', "B'", "B'", 'F', "F'"]
    mouves_sequence = []
    for i in range(0, 9):
        mouve = random.choice(test_mouves)
        print(seq[i])
        # cube.mouves[mouve]()
        cube.mouves[seq[i]]()
        cube.pretty_print()
        mouves_sequence.append(mouve)
        # visualiser.visualizer_mouves[mouve]()

    print(seq)


if __name__ == "__main__":

    visualizer = RubixVisualiser()
    thread = threading.Thread(target=test_mouves, args=[visualizer])
    thread.start()
  #  launch_vizualiser()

    # visualizer_thread = WorkerThread(visualizer)
    # visualizer_thread.start()
