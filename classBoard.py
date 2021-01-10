from classEmpty import Empty
from classFigure import Figure
from classPawn import Pawn
from random import choices


class Board:
    def __init__(self):
        # Make a board 5*5 with figures.
        self._board = [[Empty()] * 6 for i in range(6)]
        black = Figure.BLACK
        white = Figure.WHITE
        neutron = Figure.NEUTRON
        # Start position on the board.
        for j in range(1, 6):
            # self._board[1][j] = Pawn(black, j, 1)
            self._board[5][j] = Pawn(white, j, 5)
        for j in range(1, 6):
            self._board[0][j] = f"{j} "
            self._board[j][0] = f" {j}"
        self._board[3][3] = Pawn(neutron, 3, 3)
        self._board[5][2] = Empty()
        self._board[1][2] = Pawn(black, 3, 3)
        self._board[1][4] = Pawn(black, 3, 3)
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

    def move_pawns(self, xy_from, xy_to):
        self._board[xy_to[1]][xy_to[0]] = self._board[xy_from[1]][xy_from[0]]
        self._board[xy_from[1]][xy_from[0]] = Empty()

    def is_empty(self, x, y):
        return self.get_pawn(x, y).CODE == "empty"

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
            if coordinates[0] not in range(1, 6) or coordinates[1] not in range(1, 6):
                # Check: is input element 1,2,3,4,5?
                # print("Try again")
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
            coordinates = self.input_coordinates(from_to)
            if (
                (
                    from_to == 1
                    and self.check_given_coordinates(coordinates)
                    and self.check_choosen_figure_on_the_board(figure, coordinates[0], coordinates[1])
                )
                or (from_to == 0 and self.check_given_coordinates(coordinates))
            ):
                quit = False
                break
            else:
                print("Try again!")
                quit = True
        return coordinates

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
        self.move_pawns(fromXY, toXY)

    def random_fromXY(self, figure):
        possible = [1, 2, 3, 4, 5]
        quit = True
        while quit:
            from_xy = choices(possible, k=2)
            if self.check_choosen_figure_on_the_board(figure, from_xy[0], from_xy[1]):
                quit = False
                if len(self.get_pawn_moves(from_xy[0], from_xy[1])) != 0:
                    quit = False
                    break
                elif (
                    len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 0
                    and figure == Figure.NEUTRON
                ):
                    return False
                else:
                    quit = True
                    continue
            else:
                quit = True
                continue
        return from_xy

    def random_toXY(self, figure, from_xy):
        possible = [1, 2, 3, 4, 5]
        quit = True
        while quit:
            to_xy = choices(possible, k=2)
            if self.check_xyTo_in_possible_moves(from_xy, to_xy):
                return to_xy
            else:
                quit = True
                continue

    def random_opponent_coordinates(self, figure):
        """
        Computer chooses random coordinates for "From X Y" and "To X Y".
        """
        from_XY = self.random_fromXY(figure)
        if from_XY is False:
            return False
        to_XY = self.random_toXY(figure, from_XY)
        print(from_XY)
        print(self.get_pawn_moves(from_XY[0], from_XY[1]))
        self.move_pawns(from_XY, to_XY)

    def get_list_of_pawns(self, figure):
        pawns = []
        for x in range(1, 6):
            for y in range(1, 6):
                if self.check_choosen_figure_on_the_board(figure, x, y):
                    pawns.append([x, y])
        return pawns

    def hard_opponent_coordinates(self, figure):
        """
        Computer chooses best coordinates for "From X Y" and "To X Y".
        """
        possible = [1, 2, 3, 4, 5]
        correct_xy = True
        flag = True
        quit = True
        counter_from = 0
        while correct_xy and flag:
            from_xy = choices(possible, k=2)
            if self.check_choosen_figure_on_the_board(figure, from_xy[0], from_xy[1]):
                if figure == Figure.NEUTRON:
                    if len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 0:
                        # If neutron cannot move - game over
                        correct_xy = False
                        flag = True
                        quit = False
                        break
                    else:
                        flag = False
                    if flag is False:
                        for j in range(1, 6):
                            # If neutron can choose position on black row,
                            # choose it
                            vic = [j, 1]    # Victory position
                            if self.get_pawn_moves(from_xy[0], from_xy[1]).count(vic) == 1:
                                to_xy = vic
                                correct_xy = True
                                flag = False
                                break
                        else:
                            correct_xy = False
                            flag = True
                            quit = True
                            break
                else:
                    counter_from += 1
                    correct_xy = False
                    flag = True
                    quit = True
                    break
                    # if len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 0:
                    #     correct_xy = True
                    #     flag = True
                    #     continue
                    # elif len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 1:
                    #     flag = False
                    #     correct_xy = True
                    #     to_xy = self.get_pawn_moves(from_xy[0], from_xy[1])[0]
                    #     break
                    # else:
                    #     correct_xy = False
                    #     quit = True
                    #     flag = False
                    #     break
                    # flag = False

                    # if flag is False:
                    #     # for k in range(100):
                    #     if
                    #         # if black pawn can stand on the white row - move there
                    #         # to prevent empty places on white row (opponent)
                    #         if self.get_pawn_moves(from_xy[0], from_xy[1]).count(white_row) == 1:
                    #             to_xy = white_row
                    #             correct_xy = True
                    #             flag = False
                    #             break
                    #         elif (
                    #             self.get_pawn_moves(from_xy[0], from_xy[1]).count(white_row) != 1
                    #             and k != 99
                    #         ):
                    #             correct_xy = True
                    #             flag = True
                    #             continue
                    #         else:
                    #             correct_xy = False
                    #             flag = True
                    #             break
        counter_to = 0
        while correct_xy is False and quit is True:
            # If figure is Black Pawn

            to_xy = choices(possible, k=2)

            if self.get_pawn_moves(from_xy[0], from_xy[1]).count(to_xy) == 1:
                flag = False
                correct_xy = True
                counter_to += 1
                if figure == Figure.NEUTRON:
                    # Check looser position
                    # If Neutron has variants: choose looser position
                    # or another one, It should choose last one
                    if to_xy[1] == 5:
                        correct_xy = False
                        quit = True
                        continue
                    else:
                        break
                elif figure == Figure.BLACK:
                    if to_xy[1] == 5:
                        break
                    elif to_xy[1] != 5 and counter_to < 100:
                        correct_xy = False
                        quit = True
                        continue
                    elif to_xy[1] != 5 and counter_to == 100 and counter_from < 20:
                        correct_xy = True
                        flag = True
                        break
                    elif to_xy[1] != 5 and counter_to == 100 and counter_from == 20:
                        flag = False
                        correct_xy = True
                        break

        if flag is False and correct_xy is True and quit is True:
            print(from_xy)
            print(to_xy)
            print(self.get_pawn_moves(from_xy[0], from_xy[1]))
            self.move_pawns(from_xy, to_xy)
        if correct_xy is False and quit is False and flag is True:
            return False

    def game_over(self, ver):
        """
        Check.
        If the Neutron shows up on White back row, player1 have won the game.
        If the Neutron shows up on Black back row, player2 have won the game.
        """

        for j in range(1, 6):
            if self._board[1][j]._figure == Figure.NEUTRON:
                # ver - version of the game
                if ver == 23:
                    print("🟡 Player-1 🟡 is Looser")
                    print("🟣 Player-2 🟣 is Winner")
                    return True
                else:
                    print("🟡 Player-2 🟡 is Looser")
                    print("🟣 Player-1 🟣 is Winner")
                    return True
            elif self._board[5][j]._figure == Figure.NEUTRON:
                if ver == 23:
                    print("🟣 Player-2 🟣 is Looser", "\n🟡 Player-1 🟡 is WINNER")
                    return True
                else:
                    print("🟣 Player-1 🟣 is Looser")
                    print("🟡 Player-2 🟡 is Winner")
                    return True
