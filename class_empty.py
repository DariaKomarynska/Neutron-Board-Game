from class_figure import Figure
from errors import MoveEmptyError


class Empty:
    """
    Empty figure in the board - "o".
    """

    def __init__(self):
        self._figure = Figure.EMPTY

    def figure(self):
        return self._figure

    def get_moves(self, board, x, y):
        """
        Empty cannot move
        """
        raise MoveEmptyError("INCORRECT CHOICE")

    def __str__(self):
        """Presents empty place on the gameboard"""
        return " o"
