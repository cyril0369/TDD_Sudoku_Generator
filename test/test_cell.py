import pytest

from src.cell import Cell


def test_creat_a_default_cell():
    my_default_cell = Cell()
    assert 0 == my_default_cell.value


def test_creat_a_cell():
    my_default_cell = Cell(4)
    assert 4 == my_default_cell.value


def test_cell_value_exeption():
    with pytest.raises(ValueError) as excinfo:
        Cell(10)
    assert str(excinfo.value) == "Cell value must be between 0 and 9"
    with pytest.raises(ValueError) as excinfo:
        Cell(-1)
    assert str(excinfo.value) == "Cell value must be between 0 and 9"
