from classPawn import Pawn
import pytest
from errors import NotIntegerError, IncorrectNumberError
from classBoard import Board
from classEmpty import Empty


def test_create_pawn():
    pawn = Pawn(1, 3, 1)
    assert pawn.figure() == 1
    assert pawn.row() == 3
    assert pawn.column() == 1
    assert pawn.CODE == "pawn"


def test_incorrect_row():
    with pytest.raises(IncorrectNumberError):
        Pawn(1, 8, 1)


def test_incorrect_column():
    with pytest.raises(IncorrectNumberError):
        Pawn(1, 4, 12)


def test_incorrect_type_of_row():
    with pytest.raises(NotIntegerError):
        Pawn(1, "4", 5)


def test_present_black_pawn():
    pawn = Pawn(1, 2, 2)
    assert str(pawn) == "🟣"


def test_present_neutron():
    pawn = Pawn(3, 2, 2)
    assert str(pawn) == "🐹"


def test_get_moves_beginning():
    pawn = Pawn(2, 3, 5)
    board = Board()
    assert pawn.get_moves(board, 3, 5) == [[3, 4], [1, 3], [5, 3]]


def test_get_moves_middle_of_the_game1():
    pawn = Pawn(3, 3, 3)
    board = Board()
    board._board[4][3] = Pawn(2, 3, 4)
    assert pawn.get_moves(board, 3, 3) == [
        [1, 3],
        [5, 3],
        [3, 2],
        [2, 4],
        [4, 4],
        [2, 2],
        [4, 2],
    ]


def test_get_moves_middle_of_the_game2():
    pawn = Pawn(1, 2, 4)
    board = Board()
    board._board[2][1] = Pawn(2, 1, 2)
    board._board[3][2] = Pawn(3, 2, 3)
    board._board[5][2] = Pawn(0, 2, 5)
    board._board[4][2] = Pawn(1, 2, 4)
    board._board[1][5] = Pawn(2, 5, 1)
    board._board[3][3] = Pawn(0, 3, 3)
    board._board[5][5] = Pawn(0, 5, 5)
    board._board[2][3] = Pawn(2, 3, 2)
    board._board[1][3] = Pawn(0, 3, 1)
    board._board[2][4] = Pawn(1, 4, 2)
    board._board[5][4] = Pawn(0, 4, 5)
    assert pawn.get_moves(board, 2, 4) == [
        [1, 4], [5, 4], [2, 5], [1, 3], [3, 3]
        ]


def test_get_moves_middle_of_the_game3():
    pawn = Pawn(1, 4, 2)
    board = Board()
    board._board[5][5] = Empty()
    board._board[1][3] = Empty()
    board._board[5][4] = Empty()
    board._board[5][2] = Empty()
    board._board[3][3] = Empty()
    board._board[4][2] = Pawn(1, 2, 4)
    board._board[2][4] = Pawn(1, 4, 2)
    board._board[2][1] = Pawn(2, 1, 2)
    board._board[2][3] = Pawn(2, 3, 2)
    board._board[1][5] = Pawn(2, 5, 1)
    board._board[3][2] = Pawn(3, 2, 3)
    assert pawn.get_moves(board, 4, 2) == [
        [5, 2], [4, 5], [3, 3], [5, 3], [3, 1]
        ]


def test_get_moves_middle_of_the_game4():
    pawn = Pawn(1, 2, 3)
    board = Board()
    board._board[5][5] = Empty()
    board._board[1][3] = Empty()
    board._board[5][4] = Empty()
    board._board[5][2] = Empty()
    board._board[3][3] = Pawn(1, 3, 3)
    board._board[4][2] = Pawn(1, 2, 4)
    board._board[2][1] = Pawn(2, 1, 2)
    board._board[2][3] = Pawn(2, 3, 2)
    board._board[1][5] = Pawn(2, 5, 1)
    board._board[3][2] = Pawn(3, 2, 3)
    assert pawn.get_moves(board, 2, 3) == [[1, 3], [2, 2], [1, 4], [4, 5]]


def test_get_moves_middle_of_the_game5():
    pawn = Pawn(1, 2, 3)
    board = Board()
    board._board[5][5] = Empty()
    board._board[1][3] = Empty()
    board._board[5][4] = Empty()
    board._board[5][2] = Empty()
    board._board[3][3] = Pawn(1, 3, 3)
    board._board[4][2] = Pawn(1, 2, 4)
    board._board[2][1] = Pawn(2, 1, 2)
    board._board[2][3] = Pawn(2, 3, 2)
    board._board[1][5] = Pawn(2, 5, 1)
    board._board[3][2] = Pawn(3, 2, 3)
    assert not pawn.get_moves(board, 5, 2) == [[1, 3], [2, 2], [1, 4], [4, 5]]


def test_get_moves_neutron_zero_moves():
    pawn = Pawn(3, 3, 2)
    board = Board()
    board._board[2][3] = Pawn(3, 3, 2)
    board._board[2][2] = Pawn(2, 2, 2)
    board._board[3][2] = Pawn(2, 2, 3)
    board._board[3][3] = Pawn(2, 3, 3)
    board._board[3][4] = Pawn(2, 4, 3)
    board._board[2][4] = Pawn(2, 4, 2)
    for j in range(1, 6):
        board._board[5][j] = Pawn(0, j, 5)
    assert pawn.get_moves(board, 3, 2) == []


def test_get_moves_for_empty():
    pawn = Pawn(0, 3, 2)
    board = Board()
    assert pawn.get_moves(board, 3, 2) == []
