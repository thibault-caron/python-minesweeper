from views.game_view import GameView
from controllers.game_controller import GameController
from constants.game_settings import Difficulty

def main() -> None:
    """
    Entry point for the Minesweeper application.
    """
    view = GameView()
    controller = GameController(view)
    controller.initialize_game(Difficulty.EASY)
    view.mainloop()

if __name__ == "__main__":
    main()