from classFigure import Figure


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
        self._row = row
        self._column = column

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

    def get_moves(self, board, x, y):

        """
        Horizontally left
        """
        moves = []
        temp_moves = []
        j = -1
        i = x + j
        while 1 <= i <= 5:
            figure = board.get_figure(i, y)
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([i, y])
            i += j
        if len(temp_moves) != 0:
            unique_step = []
            for i in range(len(temp_moves)):
                find = sum(temp_moves[i])
                unique_step.append(find)
            max_value = min(temp_moves)
            moves.append(max_value)

        """
        Horisontally wright
        """
        temp_moves = []
        j = 1
        i = x + j
        while 1 <= i <= 5:
            figure = board.get_figure(i, y)
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([i, y])
            i += j
        if len(temp_moves) != 0:
            unique_step = []
            for i in range(len(temp_moves)):
                find = sum(temp_moves[i])
                unique_step.append(find)
            max_value = max(temp_moves)
            moves.append(max_value)

        """
        Vertically up
        """
        temp_moves = []
        j = -1
        i = y + j
        while 1 <= i <= 5:
            figure = board.get_figure(x, i)
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([x, i])
            i += j
        if len(temp_moves) != 0:
            unique_step = []
            for i in range(len(temp_moves)):
                find = sum(temp_moves[i])
                unique_step.append(find)
            max_value = min(temp_moves)
            moves.append(max_value)
        """
        Vertically down
        """
        temp_moves = []
        j = 1
        i = y + j
        while 1 <= i <= 5:
            figure = board.get_figure(x, i)
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([x, i])
            i += j
        if len(temp_moves) != 0:
            unique_step = []
            for i in range(len(temp_moves)):
                find = sum(temp_moves[i])
                unique_step.append(find)
            max_value = max(temp_moves)
            moves.append(max_value)
        """
        Diagonally down left
        """
        temp_moves = []
        j = x - 1
        i = y + 1
        while 1 <= i <= 5 and 1 <= j <= 5:
            figure = board.get_figure(j, i)
            if j == x and i == y:
                break
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([j, i])
            j -= 1
            i += 1
        if len(temp_moves) != 0:
            new = []
            for i in range(len(temp_moves)):
                find = temp_moves[i][0]
                new.append(find)
            a = min(new)
            for i in temp_moves:
                if i[0] == a:
                    moves.append(i)

        """
        Diagonally down wright
        """
        temp_moves = []
        j = x + 1
        i = y + 1
        while 1 <= i <= 5 and 1 <= j <= 5:
            figure = board.get_figure(j, i)
            if j == x and i == y:
                break
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([j, i])
            j += 1
            i += 1
        if len(temp_moves) != 0:
            new = []
            for i in range(len(temp_moves)):
                find = temp_moves[i][0]
                new.append(find)
            a = max(new)
            for i in temp_moves:
                if i[0] == a:
                    moves.append(i)
        """
        Diagonally up left
        """
        temp_moves = []
        j = x - 1
        i = y - 1
        while 1 <= i <= 5 and 1 <= j <= 5:
            figure = board.get_figure(j, i)
            if j == x and i == y:
                break
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([j, i])
            j -= 1
            i -= 1
        if len(temp_moves) != 0:
            new = []
            for i in range(len(temp_moves)):
                find = temp_moves[i][0]
                new.append(find)
            a = min(new)
            for i in temp_moves:
                if i[0] == a:
                    moves.append(i)
        """
        Diagonally up wright
        """
        temp_moves = []
        j = x + 1
        i = y - 1
        while 1 <= i <= 5 and 1 <= j <= 5:
            figure = board.get_figure(j, i)
            if j == x and i == y:
                break
            if figure == self._figure:
                break
            if figure != Figure.EMPTY:
                break
            temp_moves.append([j, i])
            j += 1
            i -= 1
        if len(temp_moves) != 0:
            new = []
            for i in range(len(temp_moves)):
                find = temp_moves[i][0]
                new.append(find)
            a = max(new)
            for i in temp_moves:
                if i[0] == a:
                    moves.append(i)
        return moves
