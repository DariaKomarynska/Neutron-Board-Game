from classBoard import Board
from classPawn import Pawn
from classFigure import Figure
from classEmpty import Empty


def test_check_basic_elements():
    board = Board()
    assert board._board[0][0] == "Y|X"
    assert board._board[0][2] == "2 "


def test_str_present_board():
    board = Board()
    assert board.create_board() == str(board)


def test_get_pawn():
    board = Board()
    assert board._board[5][1] == board.get_pawn(1, 5)


def test_get_figure():
    board = Board()
    assert board.get_pawn(1, 5)._figure == board.get_figure(1, 5)


def test_get_pawn_moves():
    board = Board()
    assert board.get_pawn(1, 5).get_moves(board, 1, 5) == board.get_pawn_moves(1, 5)


def test_move_pawns_white():
    board = Board()
    xy_from = [4, 5]
    xy_to = [1, 2]
    moved = board.move_pawns(xy_from, xy_to, 0)
    assert moved is not False


def test_move_pawns_neutron_hard():
    board = Board()
    board._board[1][4] = Empty()
    board._board[3][3] = Empty()
    board._board[5][1] = Empty()
    board._board[5][4] = Empty()
    board._board[4][4] = Pawn(1, 4, 4)
    board._board[2][1] = Pawn(2, 2, 4)
    board._board[4][2] = Pawn(2, 2, 4)
    board._board[4][5] = Pawn(3, 5, 4)
    xy_from = [5, 4]
    xy_to = [4, 5]
    board.move_pawns(xy_from, xy_to, 1)
    assert board._board[5][4] != board._board[4][5]
    assert board._board[4][5] != Empty()


def test_input_coordinates_to_xy(monkeypatch):
    board = Board()
    monkeypatch.setattr('builtins.input', lambda _: "1 5")
    result = board.input_coordinates(0)
    assert result == ["1", "5"]


def test_input_coordinates_from_xy(monkeypatch):
    board = Board()
    monkeypatch.setattr('builtins.input', lambda _: "5 5")
    result = board.input_coordinates(1)
    assert result == ["5", "5"]


def test_start_xy_for_neutron_beginning():
    board = Board()
    coordinates = board.start_xy_for_neutron()
    assert coordinates == [3, 3]


def test_start_xy_for_neutron_in_game():
    board = Board()
    board._board[4][2] = Pawn(3, 2, 4)
    board._board[3][3] = Empty()
    coordinates = board.start_xy_for_neutron()
    assert coordinates == [2, 4]


def test_check_choosen_figure_true_black():
    board = Board()
    result = board.check_choosen_figure_on_the_board(1, 4, 1)
    assert result is True


def test_give_possible_moves_pawn_begin():
    board = Board()
    start_xy = [1, 5]
    result = board.give_possible_moves(start_xy)
    assert result == "Your possible moves: [[1, 2], [2, 4]]"


def test_give_possible_moves_pawn_in_game():
    board = Board()
    board._board[1][4] = Empty()
    board._board[3][3] = Empty()
    board._board[5][1] = Empty()
    board._board[4][4] = Pawn(1, 4, 4)
    board._board[4][2] = Pawn(2, 2, 4)
    board._board[4][5] = Pawn(3, 5, 4)
    start_xy = [3, 5]
    result = board.give_possible_moves(start_xy)
    assert result == "Your possible moves: [[3, 2]]"


def test_check_given_coordinates():
    board = Board()
    XY = ["4", "5"]
    result = board.check_given_coordinates(XY)
    assert result is True


def test_check_given_coordinates_x_incorrect():
    board = Board()
    XY = ["8", "5"]
    result = board.check_given_coordinates(XY)
    assert result is False


def test_check_given_coordinates_too_much_elements():
    board = Board()
    XY = ["3", "hello", "5"]
    result = board.check_given_coordinates(XY)
    assert result is False


def test_check_given_coordinates_not_isdigit():
    board = Board()
    XY = ["hello", "5"]
    result = board.check_given_coordinates(XY)
    assert result is False


def test_check_xy_to_in_possible_moves_true():
    board = Board()
    xy_from = [1, 5]
    xy_to = [2, 4]
    result = board.check_xy_to_in_possible_moves(xy_from, xy_to)
    assert result is True


def test_check_xy_to_in_possible_moves_false():
    board = Board()
    xy_from = [1, 5]
    xy_to = [5, 3]
    result = board.check_xy_to_in_possible_moves(xy_from, xy_to)
    assert result is False


def test_check_not_zero_moves_black_false():
    board = Board()
    board._board[1][1] = Empty()
    board._board[5][1] = Empty()
    board._board[5][2] = Empty()
    board._board[5][3] = Empty()
    board._board[5][5] = Empty()
    board._board[2][2] = Pawn(1, 2, 2)
    board._board[3][3] = Pawn(2, 3, 3)
    board._board[3][2] = Pawn(2, 2, 3)
    board._board[3][4] = Pawn(2, 4, 3)
    board._board[2][4] = Pawn(2, 4, 2)
    board._board[2][3] = Pawn(3, 3, 2)
    figure = Figure.BLACK
    xy_from = [3, 1]
    result = board.check_not_zero_moves(figure, xy_from)
    assert result is False


def test_check_not_zero_moves_neutron_false():
    board = Board()
    board._board[1][1] = Empty()
    board._board[5][1] = Empty()
    board._board[5][2] = Empty()
    board._board[5][3] = Empty()
    board._board[5][5] = Empty()
    board._board[2][2] = Pawn(1, 2, 2)
    board._board[3][3] = Pawn(2, 3, 3)
    board._board[3][2] = Pawn(2, 2, 3)
    board._board[3][4] = Pawn(2, 4, 3)
    board._board[2][4] = Pawn(2, 4, 2)
    board._board[2][3] = Pawn(3, 3, 2)
    figure = Figure.NEUTRON
    xy_from = [3, 2]
    result = board.check_not_zero_moves(figure, xy_from)
    assert result is False


def test_check_not_zero_moves_black_true():
    board = Board()
    board._board[1][1] = Empty()
    board._board[5][1] = Empty()
    board._board[5][2] = Empty()
    board._board[5][3] = Empty()
    board._board[5][5] = Empty()
    board._board[2][2] = Pawn(1, 2, 2)
    board._board[3][3] = Pawn(2, 3, 3)
    board._board[3][2] = Pawn(2, 2, 3)
    board._board[3][4] = Pawn(2, 4, 3)
    board._board[2][4] = Pawn(2, 4, 2)
    board._board[2][3] = Pawn(3, 3, 2)
    figure = Figure.BLACK
    xy_from = [2, 1]
    result = board.check_not_zero_moves(figure, xy_from)
    assert result is True


def test_check_choosen_figure_white():
    board = Board()
    board._board[5][5] = Empty()
    board._board[2][5] = Pawn(2, 5, 2)
    result = board.check_choosen_figure_on_the_board(2, 5, 2)
    assert result is True


def test_check_choosen_figure_false_not_black():
    board = Board()
    result = board.check_choosen_figure_on_the_board(2, 4, 1)
    assert result is False


def test_check_choosen_figure_false_empty():
    board = Board()
    result = board.check_choosen_figure_on_the_board(2, 4, 2)
    assert result is False


def test_get_list_of_pawns():
    board = Board()
    figure = Figure.BLACK
    board._board[1][1] = Empty()
    board._board[1][3] = Empty()
    board._board[1][5] = Empty()
    board._board[1][2] = Pawn(1, 3, 3)
    board._board[1][4] = Pawn(1, 3, 3)
    result = board.get_list_of_pawns(figure)
    assert result == [[2, 1], [4, 1]]


def test_get_list_of_pawns_another():
    board = Board()
    figure = Figure.BLACK
    board._board[5][1] = Empty()
    board._board[3][3] = Pawn(2, 3, 3)
    board._board[2][3] = Pawn(1, 3, 2)
    board._board[1][5] = Pawn(2, 5, 1)
    board._board[5][3] = Pawn(3, 3, 5)
    result = board.get_list_of_pawns(figure)
    assert result == [[1, 1], [2, 1], [3, 1], [3, 2], [4, 1]]


# input_and_check_coordinates


def test_choose_correct_from_xy_white(monkeypatch):
    board = Board()
    monkeypatch.setattr('builtins.input', lambda _: "1 5")
    result = board.choose_correct_from_xy(Figure.WHITE)
    assert result == [1, 5]


def test_choose_correct_from_xy_black(monkeypatch):
    board = Board()
    monkeypatch.setattr('builtins.input', lambda _: "3 1")
    result = board.choose_correct_from_xy(Figure.BLACK)
    assert result == [3, 1]


def test_choose_correct_from_xy_neutron():
    board = Board()
    board._board[3][3] = Pawn(2, 3, 3)
    board._board[2][4] = Pawn(3, 4, 2)
    result = board.choose_correct_from_xy(Figure.NEUTRON)
    assert result == [4, 2]

# choose_correct_to_xy
# human_makes_move


def test_random_from_xy_black(monkeypatch):
    board = Board()

    def new_result(a):
        res = [3, 1]
        return res
    monkeypatch.setattr('classBoard.choice', new_result)
    result = board.random_from_xy(Figure.BLACK, 0)
    assert result == [3, 1]


def test_random_from_xy_white(monkeypatch):
    board = Board()

    def new_result(a):
        res = [4, 5]
        return res
    monkeypatch.setattr('classBoard.choice', new_result)
    result = board.random_from_xy(Figure.WHITE, 0)
    assert result == [4, 5]


def test_random_to_xy_black(monkeypatch):
    board = Board()

    def new_result(a):
        res = [4, 2]
        return res
    monkeypatch.setattr('classBoard.choice', new_result)
    from_xy = [4, 5]
    possible = board.get_pawn_moves(from_xy[0], from_xy[1])
    result = board.random_to_xy(Figure.WHITE, from_xy, 0, possible)
    assert result == [4, 2]


def test_random_to_xy_neutron(monkeypatch):
    board = Board()

    def new_result(a):
        res = [1, 3]
        return res
    monkeypatch.setattr('classBoard.choice', new_result)
    from_xy = [3, 3]
    possible = board.get_pawn_moves(from_xy[0], from_xy[1])
    result = board.random_to_xy(Figure.NEUTRON, from_xy, 1, possible)
    assert result == [1, 3]


# randomly_makes_move
# hard_victory_to_xy_neutron
# neutron_looks_moves_not_on_white
# hard_check_black_goes_on_white

def test_hard_opponent_coordinates_to_xy_black():
    board = Board()
    board._board[5][2] = Empty()
    board._board[4][1] = Pawn(2, 1, 4)
    figure = Figure.BLACK
    fromXY = [2, 1]
    to_xy = board.hard_opponent_coordinates_to_xy_black(figure, fromXY)
    assert to_xy[1] == [2, 5]


def test_hard_opponent_coordinates():
    board = Board()
    figure = Figure.BLACK
    fromXY = [3, 1]
    # def new_result(a):
    #     res = [5, 3]
    #     return res
    # monkeypatch.setattr('classBoard.choice', new_result)
    to_xy = board.hard_opponent_coordinates(figure)
    assert to_xy[1] == [5, 3]

def test_hard_opponent_coordinates():
    b = Board()

    assert b.hard_opponent_coordinates(Figure.NEUTRON)


