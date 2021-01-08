from classFigure import Figure
from errors import NotIntegerError, IncorrectNumberError


class Pawn:
    """
    General class for figures in the board.
    """

    CODE = "pawn"
    WHITE_IMG = "🟡"
    BLACK_IMG = "🟣"
    NEUTRON_IMG = "🐹"

    def __init__(self, figure, row, column):
        self._figure = figure
        self._row = int(row)
        self._column = int(column)
        if (
            (type(row) is not int)
            or (type(column) is not int)
            or (type(figure) is not int)
        ):
            raise NotIntegerError("Write integer")
        if not 1 <= row <= 5 or not 1 <= column <= 5:
            raise IncorrectNumberError("It has to be from 1 to 5")

    def figure(self):
        return self._figure

    def row(self):
        return self._row

    def column(self):
        return self._column

    def __str__(self):
        # Present our figures: black pawn, white pawn, neutron in tuple
        return (
            self.WHITE_IMG
            if self._figure == Figure.WHITE
            else self.BLACK_IMG
            if self._figure == Figure.BLACK
            else self.NEUTRON_IMG
        )

    def check_horizontally_vertically(self, board, x, y, hor_ver, direction):
        """
        Horizontally - 1: left (-1) or right (1)
        Vertically   - 0: up (-1)   or down (1)
        """
        temp_moves = []
        j = direction
        i = x + j if hor_ver == 1 else y + j
        while 1 <= i <= 5:
            figure = board.get_figure(i, y) if hor_ver == 1 else board.get_figure(x, i)
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([i, y]) if hor_ver == 1 else temp_moves.append([x, i])
            i += j
        if len(temp_moves) != 0:
            unique_step = []
            for i in range(len(temp_moves)):
                find = sum(temp_moves[i])
                unique_step.append(find)
            result = min(temp_moves) if direction == -1 else max(temp_moves)
            return result

    def check_horizontally_left(self, board, x, y):
        return self.check_horizontally_vertically(board, x, y, 1, -1)

    def check_horizontally_right(self, board, x, y):
        return self.check_horizontally_vertically(board, x, y, 1, 1)

    def check_vertically_up(self, board, x, y):
        return self.check_horizontally_vertically(board, x, y, 0, -1)

    def check_vertically_down(self, board, x, y):
        return self.check_horizontally_vertically(board, x, y, 0, 1)

    def check_diagonally_up_down_left_right(self, board, x, y, updown, direction):
        """
        Diagonally down (y + 1):  left (-1) or right (1)
        Diagonally up   (y - 1):  left (-1) or right (1)
        """
        temp_moves = []
        j = x + direction
        i = y + updown
        while 1 <= i <= 5 and 1 <= j <= 5:
            figure = board.get_figure(j, i)
            if j == x and i == y:
                break
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([j, i])
            j += direction
            i += updown
        if len(temp_moves) != 0:
            new = []
            for i in range(len(temp_moves)):
                find = temp_moves[i][0]
                new.append(find)
            a = min(new) if direction == -1 else max(new)
            for move in temp_moves:
                if move[0] == a:
                    return move

    def check_diagonally_down_left(self, board, x, y):
        return self.check_diagonally_up_down_left_right(board, x, y, 1, -1)

    def check_diagonally_down_right(self, board, x, y):
        return self.check_diagonally_up_down_left_right(board, x, y, 1, 1)

    def check_diagonally_up_left(self, board, x, y):
        return self.check_diagonally_up_down_left_right(board, x, y, -1, -1)

    def check_diagonally_up_right(self, board, x, y):
        return self.check_diagonally_up_down_left_right(board, x, y, -1, 1)

    def get_moves(self, board, x, y):
        temp_moves = [
            self.check_horizontally_left(board, x, y),
            self.check_horizontally_right(board, x, y),
            self.check_vertically_up(board, x, y),
            self.check_vertically_down(board, x, y),
            self.check_diagonally_down_left(board, x, y),
            self.check_diagonally_down_right(board, x, y),
            self.check_diagonally_up_left(board, x, y),
            self.check_diagonally_up_right(board, x, y)
        ]
        final_moves = []
        for i in temp_moves:
            if i is not None:
                final_moves.append(i)
        return final_moves