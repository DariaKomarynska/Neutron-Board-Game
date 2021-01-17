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