from classEmpty import Empty
import pytest
from classBoard import Board
from errors import MoveEmptyError


def test_definition_empty_figure():
    empty = Empty()
    assert empty.figure() == 0
    assert empty.CODE == "empty"


def test_get_moves_for_empty():
    empty = Empty()
    board = Board()
    with pytest.raises(MoveEmptyError):
        empty.get_moves(board, 2, 3)


def test_present_empty_place():
    empty = Empty()
    assert str(empty) == " o"
