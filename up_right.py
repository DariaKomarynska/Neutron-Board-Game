"""
        Diagonally up right
        """
        moves = []
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
            for move in temp_moves:
                if move[0] == a:
                    return move