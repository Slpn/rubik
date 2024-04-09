import threading
import time


class WorkerThread(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self)
        self.app = app
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():

            time.sleep(2)

            self.app.U_prime()

            time.sleep(1)

            self.app.D_prime()

            time.sleep(1)

            self.app.U()

            time.sleep(1)

            self.app.B()

            time.sleep(1)

            self.app.R_prime()

            time.sleep(1)

            self.app.L()

            time.sleep(200)

    def stop(self):
        self.stop_event.set()