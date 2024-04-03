import threading
import time


class WorkerThread(threading.Thread):

    def __init__(self, app):

        threading.Thread.__init__(self)
        self.visualizer = app
        self.stop_event = threading.Event()

        self.visualizer_mouves = {
            "U": self.visualizer.U,
            "U'": self.visualizer.U_prime,

            "D": self.visualizer.D,
            "D'": self.visualizer.D_prime,

            "F": self.visualizer.F,
            "F'": self.visualizer.F_prime,

            "B": self.visualizer.B,
            "B'": self.visualizer.B_prime,

            "L": self.visualizer.L,
            "L'": self.visualizer.L_prime,

            "R": self.visualizer.R,
            "R'": self.visualizer.R_prime,
        }

    def stop(self):
        self.stop_event.set()

    def start(self) -> None:
        self.visualizer.app.run()
