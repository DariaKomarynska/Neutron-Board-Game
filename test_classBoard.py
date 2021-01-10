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


def test_check_choosen_figure_true():
    board = Board()
    result = board.check_choosen_figure_on_the_board(1, 4, 1)
    assert result == True


def test_check_choosen_figure_false_not_black():
    board = Board()
    result = board.check_choosen_figure_on_the_board(2, 4, 1)
    assert result == False


def test_check_choosen_figure_false_empty():
    board = Board()
    result = board.check_choosen_figure_on_the_board(2, 4, 2)
    assert result == False

# def test_game_over():
#     board = Board()
#     board._board[1][3]._figure == Figure.NEUTRON
#     assert board.game_over(23) == True


def test_input_coordinates(monkeypatch):
    board = Board()
    monkeypatch.setattr('builtins.input', lambda _: "1 5")
    result = board.input_coordinates(0)
    assert result == ["1", "5"]


def test_start_xy_for_neutron_correct():
    board = Board()
    figure = Figure.NEUTRON
    coordinates = board.start_xy_for_neutron(figure)
    assert coordinates == [3, 3]


def test_start_xy_for_neutron_another():
    board = Board()
    board._board[4][2] = Pawn(3, 2, 4)
    board._board[3][3] = Empty()
    figure = Figure.NEUTRON
    coordinates = board.start_xy_for_neutron(figure)
    assert coordinates == [2, 4]


def test_give_possible_moves_pawn1():
    board = Board()
    start_XY = [1, 5]
    result = board.give_possible_moves(start_XY)
    assert result == "Your possible moves: [[1, 2], [2, 4]]"


def test_give_possible_moves_pawn2():
    board = Board()
    board._board[1][4] = Empty()
    board._board[3][3] = Empty()
    board._board[5][1] = Empty()
    board._board[4][4] = Pawn(1, 4, 4)
    board._board[4][2] = Pawn(2, 2, 4)
    board._board[4][5] = Pawn(3, 5, 4)
    start_XY = [3, 5]
    result = board.give_possible_moves(start_XY)
    assert result == "Your possible moves: [[3, 2]]"


def test_check_given_coordinates():
    board = Board()
    XY = ["4", "5"]
    result = board.check_given_coordinates(XY)
    assert result == True


def test_check_given_coordinates_x_incorrect():
    board = Board()
    XY = ["8", "5"]
    result = board.check_given_coordinates(XY)
    assert result == False


def test_check_given_coordinates_too_much_elements():
    board = Board()
    XY = ["3", "hello", "5"]
    result = board.check_given_coordinates(XY)
    assert result == False


def test_check_given_coordinates_not_isdigit():
    board = Board()
    XY = ["hello", "5"]
    result = board.check_given_coordinates(XY)
    assert result == False


def test_check_xyTo_in_possible_moves_true():
    board = Board()
    xyFrom = [1, 5]
    xyTo = [2, 4]
    result = board.check_xyTo_in_possible_moves(xyFrom, xyTo)
    assert result is True


def test_check_xyTo_in_possible_moves_false():
    board = Board()
    xyFrom = [1, 5]
    xyTo = [5, 3]
    result = board.check_xyTo_in_possible_moves(xyFrom, xyTo)
    assert result is False


def test_check_pawn_not_zero_moves_black_false():
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
    xyFrom = [3, 1]
    result = board.check_pawn_not_zero_moves(figure, xyFrom)
    assert result == False


def test_check_pawn_not_zero_moves_neutron_false():
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
    xyFrom = [3, 2]
    result = board.check_pawn_not_zero_moves(figure, xyFrom)
    assert result == False


def test_check_pawn_not_zero_moves_black_true():
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
    xyFrom = [2, 1]
    result = board.check_pawn_not_zero_moves(figure, xyFrom)
    assert result == True


def test_choose_correct_fromXY_white(monkeypatch):
    board = Board()
    monkeypatch.setattr('builtins.input', lambda _: "1 5")
    result = board.choose_correct_fromXY(Figure.WHITE)
    assert result == [1, 5]


def test_choose_correct_fromXY_black(monkeypatch):
    board = Board()
    monkeypatch.setattr('builtins.input', lambda _: "3 1")
    result = board.choose_correct_fromXY(Figure.BLACK)
    assert result == [3, 1]


def test_choose_correct_fromXY_neutron():
    board = Board()
    board._board[3][3] = Pawn(2, 3, 3)
    board._board[2][4] = Pawn(3, 4, 2)
    result = board.choose_correct_fromXY(Figure.NEUTRON)
    assert result == [4, 2]


def test_random_fromXY_black(monkeypatch):
    board = Board()

    def new_result(a, k):
        res = [3, 1]
        return res
    monkeypatch.setattr('classBoard.choices', new_result)
    result = board.random_fromXY(Figure.BLACK)
    assert result == [3, 1]


def test_random_fromXY_white(monkeypatch):
    board = Board()

    def new_result(a, k):
        res = [4, 5]
        return res
    monkeypatch.setattr('classBoard.choices', new_result)
    result = board.random_fromXY(Figure.WHITE)
    assert result == [4, 5]


def test_random_to_xy_black(monkeypatch):
    board = Board()

    def new_result(a, k):
        res = [4, 2]
        return res
    monkeypatch.setattr('classBoard.choices', new_result)
    result = board.random_toXY(Figure.WHITE, [4, 5])
    assert result == [4, 2]
