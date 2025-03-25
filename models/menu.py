import time

class Menu:
    def __init__(self, mines, difficulty="easy"):
        self.flags_left = mines
        self.difficulty = difficulty
        self.timer = 0

    def start_timer(self):
        pass

    def _increment_timer(self):
            self.timer += 1
            time.sleep(1)

    def reset(self):
        self.flags_left = 0
        self.timer = 0
