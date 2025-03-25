import threading
import time

class Menu:
    def __init__(self, mines, difficulty="easy"):
        self.flags_left = mines
        self.difficulty = difficulty
        self.timer = 0
        self.timer_thread = None
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_thread = threading.Thread(target=self._increment_timer)
            self.timer_thread.start()

    def _increment_timer(self):
        while self.timer_running:
            self.timer += 1
            time.sleep(1)

    def stop_timer(self):
        self.timer_running = False
        if self.timer_thread:
            self.timer_thread.join()

    def reset(self):
        self.flags_left = 0
        self.timer = 0
        self.timer_running = False
        if self.timer_thread:
            self.timer_thread.join()
        self.timer_thread = None
