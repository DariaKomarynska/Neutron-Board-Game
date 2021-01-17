from classEmpty import Empty
from classFigure import Figure
from classPawn import Pawn
from random import choice


class Board:
    def __init__(self):
        """
        Makes a gameboard 5*5 with figures
        but in fact 6*6 array with auxiliary symbols
        """
        self._board = [[Empty()] * 6 for i in range(6)]
        black = Figure.BLACK
        white = Figure.WHITE
        neutron = Figure.NEUTRON
        # Start position on the board
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
        """Create the board with indentation units and string elements"""
        matrix = ""
        for i in range(6):
            matrix += "   ".join(map(str, self._board[i])) + "\n"
        return matrix

    def __str__(self):
        """Present created board"""
        return self.create_board()

    def get_pawn(self, x, y):
        """Get certain pawn on the board according to given coordinates"""
        return self._board[y][x]

    def get_figure(self, x, y):
        """Get pawn's kind according to given coordinates"""
        return self.get_pawn(x, y)._figure

    def get_pawn_moves(self, x, y):
        """Get pawn's possible moves on the board according to given x, y"""
        return self.get_pawn(x, y).get_moves(self, x, y)

    def move_pawns(self, xy_from, xy_to, player):
        """
        Moves pawn on the board from start point to end point
        Returns false and doesn't move neutron for hard computer
        if next step will be losing for it

        Param:
        ----
        xy_from : start point
        xy_to   : end point
        player  : 1 if it is hard computer | 0 if another one

        """
        a = self._board[xy_from[1]][xy_from[0]]
        b = self._board[xy_to[1]][xy_to[0]]
        self._board[xy_to[1]][xy_to[0]] = self._board[xy_from[1]][xy_from[0]]
        self._board[xy_from[1]][xy_from[0]] = Empty()
        if self._board[xy_to[1]][xy_to[0]]._figure == 3 and player == 1:
            if self.check_neutron_next_step(xy_to):
                return True
            else:
                self._board[xy_from[1]][xy_from[0]] = a
                self._board[xy_to[1]][xy_to[0]] = b
                return False

    def input_coordinates(self, from_or_to):
        """
        Asks coordinates of start or end point, with space
        ----
        from_or_to : choose from_xy (1) or to_xy (0)
        """
        your_xy = "From X Y: " if from_or_to == 1 else "To X Y: "
        coord = list((input(your_xy)).split())
        return coord

    def start_xy_for_neutron(self):
        """Gets start coordinates from the board for neutron"""
        figure = Figure.NEUTRON
        for j in range(1, 6):
            for i in range(1, 6):
                if self._board[j][i]._figure == figure:
                    from_xy = [i, j]
                    return from_xy

    def give_possible_moves(self, start_xy):
        """Present a list of pawn's possible moves"""
        possible_moves = self.get_pawn_moves(start_xy[0], start_xy[1])
        print("HINTS")
        return f"Your possible moves: {possible_moves}"

    def check_given_coordinates(self, coordinates):
        """
        Checks input coordinates:
        -Is number of input elements two?
        -Is input element digit?
        -Is an element 1-5?
        """
        if (len(coordinates) == 2) and (
            coordinates[0].isdigit() and coordinates[1].isdigit()
        ):
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            if (
                coordinates[0] not in range(1, 6)
                or coordinates[1] not in range(1, 6)
            ):
                return False
            return True
        else:
            return False

    def check_xy_to_in_possible_moves(self, xy_from, xy_to):
        """
        Do chooosen end coordinates belong to list of possible moves?
        """
        if self.get_pawn_moves(xy_from[0], xy_from[1]).count(xy_to) == 1:
            return True
        return False

    def check_not_zero_moves(self, figure, xy_from):
        """
        Check : pawn has not zero possible moves
        """
        if len(self.get_pawn_moves(xy_from[0], xy_from[1])) == 0:
            if figure != Figure.NEUTRON:
                print("Choose another pawn")
            return False
        return True

    def check_choosen_figure_on_the_board(self, figure, x, y):
        """
        Check : do input coordinates belong to certain figure on the board?
        """
        choosen_figure = self.get_figure(x, y)
        if choosen_figure == figure:
            return True
        return False

    def get_list_of_pawns(self, figure):
        """
        Gets list with coordinates of pawns for moving on the board
        """
        pawns = []
        for x in range(1, 6):
            for y in range(1, 6):
                if self.check_choosen_figure_on_the_board(figure, x, y):
                    pawns.append([x, y])
        return pawns

    def input_and_check_coordinates(self, figure, from_or_to):
        """
        Input coordinates until they are correct
        ----
        from_or_to : choose from_xy (1) or to_xy (0)
        """
        quit = True
        while quit:
            coord = self.input_coordinates(from_or_to)
            if (
                from_or_to == 1
                and self.check_given_coordinates(coord)
                and self.check_choosen_figure_on_the_board(
                    figure, coord[0], coord[1])
            ) or (from_or_to == 0 and self.check_given_coordinates(coord)):
                quit = False
                break
            else:
                print("Try again!")
                quit = True
        return coord

    def choose_correct_from_xy(self, figure):
        """
        Gets from human correct from_xy coordinates
        with checking availability of possible moves
        """
        quit = True
        while quit:
            if figure != Figure.NEUTRON:
                from_xy = self.input_and_check_coordinates(figure, 1)
                if self.check_not_zero_moves(figure, from_xy) is False:
                    continue
                else:
                    quit = False
                    break
            else:
                from_xy = self.start_xy_for_neutron()
                if not self.check_not_zero_moves(figure, from_xy):
                    return False
                else:
                    quit = False
                    break
        return from_xy

    def choose_correct_to_xy(self, figure, from_xy):
        """
        Gets from human correct to_xy coordinates
        untill they are in possible moves
        """
        quit = True
        while quit:
            to_xy = self.input_and_check_coordinates(figure, 0)
            if self.check_xy_to_in_possible_moves(from_xy, to_xy):
                quit = False
                break
            else:
                quit = True
        return to_xy

    def human_makes_move(self, figure):
        """
        Human enters start coordinates for moving,
        gets possible moves, enters end coordinates and pawn moves.
        Returns False if neutron doesn't have moves.
        """
        from_xy = self.choose_correct_from_xy(figure)
        if from_xy is False:
            return False
        print(self.give_possible_moves(from_xy))
        to_xy = self.choose_correct_to_xy(figure, from_xy)
        self.move_pawns(from_xy, to_xy, 0)

    def random_from_xy(self, figure, pawns):
        """
        Gets randomly correct from_xy coordinates
        with checking availability of possible moves
        """
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

    def random_to_xy(self, figure, from_xy, player, possible_moves):
        """
        Gets randomly correct to_xy coordinates from list of possible moves
        """
        possible = self.get_pawn_moves(from_xy[0], from_xy[1])
        if player == 1:
            possible = possible_moves
        to_xy = choice(possible)
        return to_xy

    def randomly_makes_move(self, figure):
        """
        Computer chooses random coordinates for moving and pawn moves
        Returns False if neutron doesn't have moves.
        """
        pawns = self.get_list_of_pawns(figure)
        from_XY = self.random_from_xy(figure, pawns)
        if from_XY is False:
            return False
        to_XY = self.random_to_xy(figure, from_XY, 0, 0)
        self.move_pawns(from_XY, to_XY, 0)

    def hard_victory_to_xy_neutron(self, possible_moves):
        """
        Gets victory position for hard computer's neutron :
        on the black row
        """
        quit = True
        possible = possible_moves.copy()
        while quit:
            for j in range(1, 6):
                vic = [j, 1]  # victory position
                if possible.count(vic) == 1:
                    to_xy = vic
                    quit = False
                    return to_xy
                    break
            else:
                return False
                break

    def neutron_looks_moves_not_on_white(self, possible_moves):
        """
        Gets list of moves without moves on white row as possible
        """
        result = []
        for move in possible_moves:
            if move[1] != 5:
                result.append(move)
            elif move[1] == 5 and len(possible_moves) == 1:
                result.append(move)
        return result

    def hard_check_black_goes_on_white(self, from_xy):
        """
        Gets move on white row for black pawn as possible
        To prevent moving neutron by white player onto its row
        """
        for j in range(1, 6):
            on_white = [j, 5]
            if (self.get_pawn_moves(
                from_xy[0], from_xy[1]
            ).count(on_white) == 1):
                to_xy = on_white
                return to_xy
        else:
            return False

    def hard_coordinates_start_end_black(self, figure, from_xy):
        """
        Chooses start and end coordinates for black pawn for hard computer
        with all checks untill they are correct
        """
        quit = True
        temp_from_xy = from_xy
        pawns = self.get_list_of_pawns(figure)
        while quit:
            to_xy = self.hard_check_black_goes_on_white(temp_from_xy)
            if to_xy is not False:
                quit = False
                break
            if len(pawns) != 1:
                used_from_xy = temp_from_xy
                pawns.remove(used_from_xy)
                temp_from_xy = self.random_from_xy(figure, pawns)
                quit = True
                continue
            else:
                to_xy = self.random_to_xy(figure, from_xy, 0, 0)
                temp_from_xy = from_xy
                quit = False
                break
        return [temp_from_xy, to_xy]

    def hard_make_move_black(self, figure, from_xy):
        """
        Hard computer makes move of black pawn
        """
        coordinates_moving = self.hard_coordinates_start_end_black(
            figure, from_xy)
        from_xy = coordinates_moving[0]
        to_xy = coordinates_moving[1]
        self.move_pawns(from_xy, to_xy, 0)

    def hard_make_move_neutron(self, figure, from_xy):
        """
        Hard computer makes move of neutron with checking this move
        Choose move to prevent loosing in this and also in the next step
        """
        quit = True
        possible = self.get_pawn_moves(from_xy[0], from_xy[1])
        if self.hard_victory_to_xy_neutron(possible) is not False:
            to_xy = self.hard_victory_to_xy_neutron(possible)
            self.move_pawns(from_xy, to_xy, 0)
            return
        else:
            temp_to_xy_moves = self.neutron_looks_moves_not_on_white(possible)
            new_possible = temp_to_xy_moves.copy()
            if len(temp_to_xy_moves) == 1:
                to_xy = temp_to_xy_moves[0]
            else:
                while quit is True:
                    to_xy = self.random_to_xy(figure, from_xy, 1, new_possible)

                    to = self.move_pawns(from_xy, to_xy, 1)
                    if to is False and len(new_possible) != 1:
                        used = to_xy
                        new_possible.remove(used)
                        continue

                    elif to is False and len(new_possible) == 1:
                        to_xy = new_possible[0]
                        quit = False
                        break
                    else:
                        quit = False
                        return

    def hard_computer_makes_move(self, figure):
        """
        Computer chooses best coordinates for black pawn or neutron
        """
        pawns = self.get_list_of_pawns(figure)
        from_xy = self.random_from_xy(figure, pawns)
        if from_xy is False:
            return False

        if figure == Figure.BLACK:
            self.hard_make_move_black(figure, from_xy)

        else:
            self.hard_make_move_neutron(figure, from_xy)

    def check_neutron_next_step(self, new_from_xy):
        """
        Check : neutron can have loosing move next step
        """
        next_moves = self.get_pawn_moves(new_from_xy[0], new_from_xy[1])
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
        If Neutron shows up on White back row, player1 have won the game.
        If Neutron shows up on Black back row, player2 have won the game.
        ----
        version : version of the game 2/3 or 4/5
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
