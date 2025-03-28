from views.game_view import GameView
from controllers.game_controller import GameController
from constants import Difficulty

def main() -> None:
    """
    Entry point for the Minesweeper application.
    """
    view = GameView()
    controller = GameController(view)
    controller.initialize_game(Difficulty.HARD)
    view.mainloop()

if __name__ == "__main__":
    main()