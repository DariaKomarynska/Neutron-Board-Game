from classFigure import Figure


class Empty:
    """
    Empty figure in the board - "o".
    """

    CODE = "empty"
    # figure = Figure.EMPTY

    def __init__(self):
        self._figure = Figure.EMPTY

    def figure(self):
        return self._figure

    def get_moves(self, board, x, y):
        raise Exception("INCORRECT CHOICE")

    def __str__(self):
        return " o"
