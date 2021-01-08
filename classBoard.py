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
        for j in range(6):
            self._board[1][j] = Pawn(black, 1, j)
            self._board[5][j] = Pawn(white, 5, j)
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

    def move_pawns(self, xy_from, xy_to):
        self._board[xy_to[1]][xy_to[0]] = self._board[xy_from[1]][xy_from[0]]
        self._board[xy_from[1]][xy_from[0]] = Empty()

    def is_empty(self, x, y):
        return self.get_pawn(x, y).CODE == "empty"

    def enter_coordinates(self, figure):
        """
        Player should enter coordinates for moving pawn.
        Input x and y shoud be checked.
        Do choosen x, y (from) belong to player's figure?
        Are choosen x, y (to) possible to stand here?
        """
        correct_xy = True
        flag = True
        while correct_xy is True and flag is True:

            if figure == Figure.NEUTRON:
                # If figure is Neutron: don't ask fromXY, take from the board
                for j in range(1, 6):
                    for i in range(1, 6):
                        if self._board[j][i]._figure == figure:
                            fromXY = [i, j]
                            correct_xy = False
                break
            else:
                # Enter list of two numbers for x and y with space.
                fromXY = list((input("From X Y: ")).split())

            if len(fromXY) != 2:
                # Check number of input elements.
                print("Write X and Y of pawn: two numbers from 1 to 5 with", "SPACE")
                correct_xy = True
            else:
                correct_xy = False

            if correct_xy is False:
                # Check: is input element digit?
                if not fromXY[0].isdigit() or not fromXY[1].isdigit():
                    print("You schould write numbers")
                    correct_xy = True
                else:
                    correct_xy = False

                fromXY[0] = int(fromXY[0])
                fromXY[1] = int(fromXY[1])

                # Check: is input element 1,2,3,4,5?
                if fromXY[0] not in range(1, 6) or fromXY[1] not in range(1, 6):
                    print("You schould write numbers from 1 to 5")
                    correct_xy = True

            if correct_xy is False:
                # Check: does choosen element belong to correct figure?
                if self.check_given_coordinates(figure, fromXY[0], fromXY[1]):
                    #
                    correct_xy = False

                if not self.check_given_coordinates(figure, fromXY[0], fromXY[1]):
                    print("Enter correct X Y")
                    correct_xy = True
            if correct_xy is False:
                if len(self.get_pawn_moves(fromXY[0], fromXY[1])) == 0 and (
                    figure == Figure.WHITE or figure == Figure.BLACK
                ):
                    correct_xy = True
                    flag = True
                    print("Choose another pawn")
                    continue
                else:
                    correct_xy = False
                    break

            # Check game over by number of possible moves for Neutron
        while correct_xy is False:
            if len(self.get_pawn_moves(fromXY[0], fromXY[1])) != 0:
                correct_xy = True
                break
            else:
                correct_xy = False
                flag = False
                break
        while correct_xy is True:
            possible_moves = self.get_pawn_moves(fromXY[0], fromXY[1])
            print("HINTS")
            # Here is a list of possible moves for certain figure.
            print(f"Your possible moves: {possible_moves}")

            # Enter list of two numbers for x and y with space.
            toXY = list((input("To X Y: ")).split())

            if len(toXY) != 2:
                # Check number of input elements.
                print("Enter correctly")
                correct_xy = True
            else:
                correct_xy = False

            if correct_xy is False:
                # Check: is input element digit?
                if not toXY[0].isdigit() or not toXY[1].isdigit():
                    print("Enter numbers")
                    correct_xy = True
                else:
                    correct_xy = False

            if correct_xy is False:
                toXY[0] = int(toXY[0])
                toXY[1] = int(toXY[1])

            if correct_xy is False:
                # Check: is input element 1,2,3,4,5?
                if toXY[0] not in range(1, 6) or toXY[1] not in range(1, 6):
                    print("Enter from 1 to 5")
                    correct_xy = True

            while correct_xy is False:
                # Do chooosen elements belong to list of possible moves?
                if self.get_pawn_moves(fromXY[0], fromXY[1]).count(toXY) == 1:
                    flag = True
                    break
                else:
                    print("Enter correct X Y")
                    correct_xy = True
        if flag is False:
            return False
        if flag is True:
            self.move_pawns(fromXY, toXY)

    def check_given_coordinates(self, figure, x, y):
        """
        Check input coordinates for certain figure.
        """
        choosen_figure = self.get_figure(x, y)
        if choosen_figure == figure:
            return True
        return False

    def random_opponent_coordinates(self, figure):
        """
        Computer chooses random coordinates for "From X Y" and "To X Y".
        """
        possible = [1, 2, 3, 4, 5]
        flag = True

        while flag:
            from_xy = choices(possible, k=2)
            if self.check_given_coordinates(figure, from_xy[0], from_xy[1]):
                flag = False

            if flag is False:
                if len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 0 and (
                    figure == Figure.WHITE or figure == Figure.BLACK
                ):
                    flag = True
                    continue
                else:
                    flag = False
                    break

        while flag is False:
            if len(self.get_pawn_moves(from_xy[0], from_xy[1])) != 0:
                flag = True
                break
            else:
                flag = False
                break
        while flag:
            to_xy = choices(possible, k=2)
            if self.get_pawn_moves(from_xy[0], from_xy[1]).count(to_xy) == 1:
                break
        if flag is False:
            return False
        if flag is True:
            print(from_xy)
            print(self.get_pawn_moves(from_xy[0], from_xy[1]))
            self.move_pawns(from_xy, to_xy)

    def hard_opponent_coordinates(self, figure):
        """
        Computer chooses best coordinates for "From X Y" and "To X Y".
        """
        possible = [1, 2, 3, 4, 5]
        correct_xy = True
        flag = True
        quit = True
        while correct_xy and flag:
            from_xy = choices(possible, k=2)
            if self.check_given_coordinates(figure, from_xy[0], from_xy[1]):
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
                elif figure == Figure.BLACK:
                    if len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 0:
                        correct_xy = True
                        flag = True
                        continue
                    elif len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 1:
                        flag = False
                        correct_xy = True
                        to_xy = self.get_pawn_moves(from_xy[0], from_xy[1])[0]
                        break
                    else:
                        correct_xy = False
                        quit = True
                        flag = False
                        break

                    if flag is False:
                        for k in range(100):
                            for i in range(1, 6):
                                white_row = [i, 5]
                                # if black pawn can stand on the white row - move there
                                # to prevent empty places on white row (opponent)
                                if self.get_pawn_moves(from_xy[0], from_xy[1]).count(white_row) == 1:
                                    to_xy = white_row
                                    correct_xy = True
                                    flag = False
                                    break
                                elif (
                                    self.get_pawn_moves(from_xy[0], from_xy[1]).count(white_row) != 1
                                    and k != 99
                                ):
                                    correct_xy = True
                                    flag = True
                                    continue
                                else:
                                    correct_xy = False
                                    flag = True
                                    break

        while correct_xy is False and quit is True:
            # If figure is Black Pawn
            to_xy = choices(possible, k=2)
            if self.get_pawn_moves(from_xy[0], from_xy[1]).count(to_xy) == 1:
                flag = False
                correct_xy = True
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
                else:
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
                if ver == 23:
                    print("🟡 Player-1🟡 is Looser")
                    print("🟣 Player-2🟣 is Winner")
                    return True
                else:
                    print("🟡 Player-2🟡 is Looser")
                    print("🟣 Player-1🟣 is Winner")
                    return True
            elif self._board[5][j]._figure == Figure.NEUTRON:
                if ver == 23:
                    print("🟣 Player-2🟣 is Looser", "\n🟡 Player-1🟡 is WINNER")
                    return True
                else:
                    print("🟣 Player-1🟣 is Looser")
                    print("🟡 Player-2🟡 is Winner")
                    return True
