from classPawn import Pawn
import pytest
from errors import NotIntegerError, IncorrectNumberError
from classBoard import Board


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


# Test class Pawn. Basic elements, raise error if incorrect
 number, column, row