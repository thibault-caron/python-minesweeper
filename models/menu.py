import threading
import time

class Menu:
    """
    Represents the game menu, including flags, difficulty, and timer.

    :param mines: int - Number of mines in the game.
    :param difficulty: str - Difficulty level ("easy", "medium", or "hard").
    """
    def __init__(self, mines, difficulty="easy"):
        self.flags_left = mines
        self.difficulty = difficulty
        self.timer = 0
        self.timer_thread = None
        self.timer_running = False

    def start_timer(self) -> None:
        """
        Start the game timer.
        """
        if not self.timer_running:
            self.timer_running = True
            self.timer_thread = threading.Thread(target=self._increment_timer)
            self.timer_thread.start()

    def _increment_timer(self) -> None:
        """
        Increment the timer by 1 every second while the timer is running.
        """
        while self.timer_running:
            self.timer += 1
            time.sleep(1)

    def stop_timer(self) -> None:
        """
        Stop the game timer.
        """
        self.timer_running = False
        if self.timer_thread:
            self.timer_thread.join()

    def reset(self) -> None:
        """
        Reset the menu attributes to their initial state.
        """
        self.flags_left = 0
        self.timer = 0
        self.timer_running = False
        if self.timer_thread:
            self.timer_thread.join()
        self.timer_thread = None
