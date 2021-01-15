from classFigure import Figure
# import pytest


def test_define_empty_figure():
    figure = Figure()
    assert figure.EMPTY == 0


def test_define_black_figure():
    figure = Figure()
    assert figure.BLACK == 1


def test_define_white_figure():
    figure = Figure()
    assert figure.WHITE == 2


def test_define_neutron_as_figure():
    figure = Figure()
    assert figure.NEUTRON == 3


def test_incorrect_definition_string():
    figure = Figure()
    assert not figure.BLACK == "black"


def test_incorrect_definition_number():
    figure = Figure()
    assert not figure.NEUTRON == 25
