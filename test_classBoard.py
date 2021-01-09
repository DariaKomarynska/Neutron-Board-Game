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


def test_check_given_coordinates_true():
    board = Board()
    assert board.check_given_coordinates(1, 4, 1) == True


def test_check_given_coordinates_false_not_black():
    board = Board()
    assert board.check_given_coordinates(2, 4, 1) == False


def test_check_given_coordinates_false_empty():
    board = Board()
    assert board.check_given_coordinates(2, 4, 2) == False

# def test_game_over():
#     board = Board()
#     board._board[1][3]._figure == Figure.NEUTRON
#     assert board.game_over(23) == True