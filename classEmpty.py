from classFigure import Figure
from errors import MoveEmptyError


class Empty:
    """
    Empty figure in the board - "o".
    """

    CODE = "empty"

    def __init__(self):
        self._figure = Figure.EMPTY

    def figure(self):
        return self._figure

    def get_moves(self, board, x, y):
        raise MoveEmptyError("INCORRECT CHOICE")

    def __str__(self):
        return " o"
