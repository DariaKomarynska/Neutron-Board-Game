        temp_moves = []
        i = x + direction if hor_ver == 1 else y + direction
        j = y + updown
        while 1 <= i <= 5 and 1 <= j <= 5:
            figure = board.get_figure(j, i)
            if figure != Figure.EMPTY:
                break
            temp_moves.append([j, i])
            j += direction
            i += updown
        if len(temp_moves) != 0:
            move = min(temp_moves) if direction == -1 else max(temp_moves)
            return move