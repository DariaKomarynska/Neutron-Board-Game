from classFigure import Figure
from errors import NotIntegerError, IncorrectNumberError


class Pawn:
    """
    Class Pawn. General class for all figures on the board.
    Contains attributes:
    :param figure: kind of pawn
    :type figure: int

    :param row: pawn's row on the board
    :type power: int

    :param column: pawn's column on the board
    :type power: int
    """

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
        """
        Present figure: black pawn, white pawn or neutron
        """
        return (
            self.WHITE_IMG
            if self._figure == Figure.WHITE
            else self.BLACK_IMG
            if self._figure == Figure.BLACK
            else self.NEUTRON_IMG
        )

    def get_horizontally_vertically_move(
        self, board, x, y, hor_ver, direction
    ):
        """
        Gets coordinates for moving as far as possible:
        horizontally left or right / vertically up or down

        Param:
        -----
        board   : gameboard with all pawns
        x, y    : coordinates of pawn on the board
        hor_ver : choosen horizontal - 1 or vertical - 0 direction
        direction :
            horizontally : left (-1) or right (1)
            vertically   : up (-1)   or down (1)
        """
        temp_moves = []
        i = x + direction if hor_ver == 1 else y + direction
        while 1 <= i <= 5:
            figure = board.get_figure(i, y) if hor_ver == 1 \
                else board.get_figure(x, i)
            if figure != Figure.EMPTY:
                break
            temp_moves.append([i, y]) if hor_ver == 1 \
                else temp_moves.append([x, i])
            i += direction
        if len(temp_moves) != 0:
            move = min(temp_moves) if direction == -1 else max(temp_moves)
            return move

    def get_horizontally_left(self, board, x, y):
        """Gets horizontally left move"""
        return self.get_horizontally_vertically_move(board, x, y, 1, -1)

    def get_horizontally_right(self, board, x, y):
        """Gets horizontally right move"""
        return self.get_horizontally_vertically_move(board, x, y, 1, 1)

    def get_vertically_up(self, board, x, y):
        """Gets vertically up move"""
        return self.get_horizontally_vertically_move(board, x, y, 0, -1)

    def get_vertically_down(self, board, x, y):
        """Gets vertically down move"""
        return self.get_horizontally_vertically_move(board, x, y, 0, 1)

    def get_diagonally_up_down_left_right(
        self, board, x, y, up_down, left_right
    ):
        """
        Gets coordinates for moving as far as possible diagonally:
        down / up - left or right

        Param:
        -----
        board     : gameboard with all pawns
        x, y      : coordinates of pawn on the board
        up_down    : choosen down (1) or up (-1)
        left_right : left (-1) or right (1)
        """
        temp_moves = []
        j = x + left_right
        i = y + up_down
        while 1 <= i <= 5 and 1 <= j <= 5:
            figure = board.get_figure(j, i)
            if figure != Figure.EMPTY:
                break
            temp_moves.append([j, i])
            j += left_right
            i += up_down
        if len(temp_moves) != 0:
            move = min(temp_moves) if left_right == -1 else max(temp_moves)
            return move

    def get_diagonally_down_left(self, board, x, y):
        """Gets diagonally down left move"""
        return self.get_diagonally_up_down_left_right(board, x, y, 1, -1)

    def get_diagonally_down_right(self, board, x, y):
        """Gets diagonally down right move"""
        return self.get_diagonally_up_down_left_right(board, x, y, 1, 1)

    def get_diagonally_up_left(self, board, x, y):
        """Gets diagonally up left move"""
        return self.get_diagonally_up_down_left_right(board, x, y, -1, -1)

    def get_diagonally_up_right(self, board, x, y):
        """Gets diagonally up right move"""
        return self.get_diagonally_up_down_left_right(board, x, y, -1, 1)

    def get_moves(self, board, x, y):
        temp_moves = [
            self.get_horizontally_left(board, x, y),
            self.get_horizontally_right(board, x, y),
            self.get_vertically_up(board, x, y),
            self.get_vertically_down(board, x, y),
            self.get_diagonally_down_left(board, x, y),
            self.get_diagonally_down_right(board, x, y),
            self.get_diagonally_up_left(board, x, y),
            self.get_diagonally_up_right(board, x, y),
        ]
        final_moves = []
        for i in temp_moves:
            if i is not None:
                final_moves.append(i)
        return final_moves
