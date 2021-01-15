from classEmpty import Empty
from classFigure import Figure
from classPawn import Pawn
from random import choice


class Board:
    def __init__(self):
        # Make a board 5*5 with figures.
        self._board = [[Empty()] * 6 for i in range(6)]
        black = Figure.BLACK
        white = Figure.WHITE
        neutron = Figure.NEUTRON
        # Start position on the board.
        for j in range(1, 6):
            self._board[1][j] = Pawn(black, j, 1)
            self._board[5][j] = Pawn(white, j, 5)
        for j in range(1, 6):
            self._board[0][j] = f"{j} "
            self._board[j][0] = f" {j}"
        self._board[3][3] = Pawn(neutron, 3, 3)
        self._board[0][0] = "Y|X"

    def board(self):
        return self._board

    def create_board(self):
        # Present the board with indentation units and string elements
        matrix = ""
        for i in range(6):
            matrix += "   ".join(map(str, self._board[i])) + "\n"
        return matrix

    def __str__(self):
        # Print created board
        return self.create_board()

    def get_pawn(self, x, y):
        return self._board[y][x]

    def get_figure(self, x, y):
        return self.get_pawn(x, y)._figure

    def get_pawn_moves(self, x, y):
        return self.get_pawn(x, y).get_moves(self, x, y)

    def move_pawns(self, xy_from, xy_to, player):
        a = self._board[xy_from[1]][xy_from[0]]
        b = self._board[xy_to[1]][xy_to[0]]
        self._board[xy_to[1]][xy_to[0]] = self._board[xy_from[1]][xy_from[0]]
        self._board[xy_from[1]][xy_from[0]] = Empty()
        # new = self._board[xy_to[1]][xy_to[0]]
        # print(new)
        if self._board[xy_to[1]][xy_to[0]]._figure == 3 and player == 1:
            # player = 1 - hard computer neutron
            if self.check_neutron_next_step(xy_to):
                return True
            else:
                self._board[xy_from[1]][xy_from[0]] = a
                self._board[xy_to[1]][xy_to[0]] = b
                return False

    def input_coordinates(self, from_to):
        # Enter list of two numbers for x and y with space.
        your_xy = "From X Y: " if from_to == 1 else "To X Y: "
        XY = list((input(your_xy)).split())
        return XY

    def start_xy_for_neutron(self, figure):
        # If figure is Neutron: don't ask fromXY, take from the board
        figure = Figure.NEUTRON
        for j in range(1, 6):
            for i in range(1, 6):
                if self._board[j][i]._figure == figure:
                    fromXY = [i, j]
                    return fromXY

    def give_possible_moves(self, start_XY):
        possible_moves = self.get_pawn_moves(start_XY[0], start_XY[1])
        print("HINTS")
        # Here is a list of possible moves for certain figure.
        return(f"Your possible moves: {possible_moves}")

    def check_given_coordinates(self, coordinates):
        if (
            (len(coordinates) == 2)
            and (coordinates[0].isdigit() and coordinates[1].isdigit())
        ):
            # Check number of input elements
            # Check: is input element digit?
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            if (
                coordinates[0] not in range(1, 6)
                or coordinates[1] not in range(1, 6)
            ):
                # Check: is input element 1,2,3,4,5?
                return False
            return True
        else:
            # print("Try again")
            return False

    def check_xyTo_in_possible_moves(self, xyFrom, xyTo):
        # Do chooosen elements belong to list of possible moves?
        if self.get_pawn_moves(xyFrom[0], xyFrom[1]).count(xyTo) == 1:
            return True
        return False

    def check_pawn_not_zero_moves(self, figure, xyFrom):
        if len(self.get_pawn_moves(xyFrom[0], xyFrom[1])) == 0:
            if figure != Figure.NEUTRON:
                print("Choose another pawn")
            return False
        return True

    def check_choosen_figure_on_the_board(self, figure, x, y):
        """
        Check input coordinates for certain figure.
        """
        choosen_figure = self.get_figure(x, y)
        if choosen_figure == figure:
            return True
        return False

    def input_and_check_coordinates(self, figure, from_to):
        quit = True
        while quit:
            coord = self.input_coordinates(from_to)
            if (
                (
                    from_to == 1
                    and self.check_given_coordinates(coord)
                    and self.check_choosen_figure_on_the_board(figure, coord[0], coord[1])
                )
                or (from_to == 0 and self.check_given_coordinates(coord))
            ):
                quit = False
                break
            else:
                print("Try again!")
                quit = True
        return coord

    def choose_correct_fromXY(self, figure):
        quit = True
        while quit:
            if figure != Figure.NEUTRON:
                fromXY = self.input_and_check_coordinates(figure, 1)
                if self.check_pawn_not_zero_moves(figure, fromXY) is False:
                    continue
                else:
                    quit = False
                    break
            else:
                fromXY = self.start_xy_for_neutron(figure)
                if not self.check_pawn_not_zero_moves(figure, fromXY):
                    return False
                else:
                    quit = False
                    break
        return fromXY

    def choose_correct_toXY(self, figure, fromXY):
        quit = True
        while quit:
            toXY = self.input_and_check_coordinates(figure, 0)
            if self.check_xyTo_in_possible_moves(fromXY, toXY):
                quit = False
                break
            else:
                quit = True
        return toXY

    def enter_coordinates(self, figure):
        fromXY = self.choose_correct_fromXY(figure)
        if fromXY is False:
            return False
        print(self.give_possible_moves(fromXY))
        toXY = self.choose_correct_toXY(figure, fromXY)
        self.move_pawns(fromXY, toXY, 0)

    def random_fromXY(self, figure, pawns):
        possible_pawns = pawns
        quit = True
        while quit:
            from_xy = choice(possible_pawns)
            if len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 0:
                if figure == Figure.NEUTRON:
                    return False
                else:
                    continue
            else:
                return from_xy

    def random_toXY(self, figure, from_xy, player, possible_moves):
        possible = self.get_pawn_moves(from_xy[0], from_xy[1])
        if player == 1:
            possible = possible_moves
        to_xy = choice(possible)
        return to_xy

    def random_opponent_coordinates(self, figure):
        """
        Computer chooses random coordinates for "From X Y" and "To X Y".
        """
        pawns = self.get_list_of_pawns(figure)
        from_XY = self.random_fromXY(figure, pawns)
        if from_XY is False:
            return False
        to_XY = self.random_toXY(figure, from_XY, 0, 0)
        self.move_pawns(from_XY, to_XY, 0)

    def get_list_of_pawns(self, figure):
        pawns = []
        for x in range(1, 6):
            for y in range(1, 6):
                if self.check_choosen_figure_on_the_board(figure, x, y):
                    pawns.append([x, y])
        return pawns

    def hard_victory_toXY_neutron(self, fromXY, possible_moves):
        quit = True
        possible = possible_moves.copy()
        while quit:
            for j in range(1, 6):
                vic = [j, 1]    # victory position
                if possible.count(vic) == 1:
                    toXY = vic
                    quit = False
                    return toXY
                    break
            else:
                return False
                break

    def check_neutron_try_without_white_moves(self, figure, fromXY, possible_moves):
        result = []
        for move in possible_moves:
            if move[1] != 5:
                result.append(move)
            elif move[1] == 5 and len(possible_moves) == 1:
                result.append(move)
        return result

    def hard_check_black_goes_on_white(self, from_xy):
        for j in range(1, 6):
            on_white = [j, 5]
            if self.get_pawn_moves(from_xy[0], from_xy[1]).count(on_white) == 1:
                toXY = on_white
                return toXY
        else:
            return False

    def hard_opponent_coordinates_toXY_black(self, figure, fromXY):
        quit = True
        temp_fromXY = fromXY
        pawns = self.get_list_of_pawns(figure)
        while quit:
            toXY = self.hard_check_black_goes_on_white(temp_fromXY)
            if toXY is not False:
                quit = False
                break
            if len(pawns) != 1:
                used_fromXY = temp_fromXY
                pawns.remove(used_fromXY)
                temp_fromXY = self.random_fromXY(figure, pawns)
                quit = True
                continue
            else:
                toXY = self.random_toXY(figure, fromXY, 0, 0)
                temp_fromXY = fromXY
                quit = False
                break
        return [temp_fromXY, toXY]

    def choose_move_black_hard(self, figure, from_XY):
        coordinates_moving = self.hard_opponent_coordinates_toXY_black(figure, from_XY)
        from_XY = coordinates_moving[0]
        to_XY = coordinates_moving[1]
        print(from_XY)
        print(to_XY)
        print(self.get_pawn_moves(from_XY[0], from_XY[1]))
        self.move_pawns(from_XY, to_XY, 0)

    def choose_move_neutron_hard(self, figure, from_XY):
        quit = True
        possible_moves = self.get_pawn_moves(from_XY[0], from_XY[1])
        if self.hard_victory_toXY_neutron(from_XY, possible_moves) is not False:
            to_XY = self.hard_victory_toXY_neutron(from_XY, possible_moves)
            self.move_pawns(from_XY, to_XY, 0)
            return
        else:
            temp_to_XY_moves = self.check_neutron_try_without_white_moves(figure, from_XY, possible_moves)
            new_possible = temp_to_XY_moves.copy()
            if len(temp_to_XY_moves) == 1:
                to_XY = temp_to_XY_moves[0]
            else:
                while quit is True:
                    to_XY = self.random_toXY(figure, from_XY, 1, new_possible)

                    to = self.move_pawns(from_XY, to_XY, 1)
                    if to is False and len(new_possible) != 1:
                        used = to_XY
                        new_possible.remove(used)
                        continue

                    elif to is False and len(new_possible) == 1:
                        to_XY = new_possible[0]
                        quit = False
                        break
                    else:
                        quit = False
                        return

    def hard_opponent_coordinates(self, figure):
        """
        Computer chooses best coordinates for "From X Y" and "To X Y".
        """
        pawns = self.get_list_of_pawns(figure)
        from_XY = self.random_fromXY(figure, pawns)
        if from_XY is False:
            return False

        if figure == Figure.BLACK:
            self.choose_move_black_hard(figure, from_XY)

        else:
            self.choose_move_neutron_hard(figure, from_XY)

    def check_neutron_next_step(self, new_from_XY):
        next_moves = self.get_pawn_moves(new_from_XY[0], new_from_XY[1])
        bad_moves = []
        for move in next_moves:
            if move[1] == 5:
                bad_moves.append(move)
        for i in bad_moves:
            if i[1] == 5:
                return False
        return True

    def game_over(self, version):
        """
        Check.
        If the Neutron shows up on White back row, player1 have won the game.
        If the Neutron shows up on Black back row, player2 have won the game.
        """
        for j in range(1, 6):
            if self._board[1][j]._figure == Figure.NEUTRON:
                # ver - version of the game
                if version == 23:
                    print("🟡 Player-1 🟡 is Looser")
                    print("🟣 Player-2 🟣 is WINNER")
                    return True
                else:
                    print("🟡 Player-2 🟡 is Looser")
                    print("🟣 Player-1 🟣 is WINNER")
                    return True
            elif self._board[5][j]._figure == Figure.NEUTRON:
                if version == 23:
                    print("🟣 Player-2 🟣 is Looser", "\n🟡 Player-1 🟡 is WINNER")
                    return True
                else:
                    print("🟣 Player-1 🟣 is Looser")
                    print("🟡 Player-2 🟡 is WINNER")
                    return True
