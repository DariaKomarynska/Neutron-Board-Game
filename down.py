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