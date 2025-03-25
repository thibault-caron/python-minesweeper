from views.game_view import GameView
from controllers.game_controller import GameController

def main():
    view = GameView()
    controller = GameController(view)
    controller.start_game()

    view.mainloop()

if __name__ == "__main__":
    main()
