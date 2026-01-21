import pytest

from src.grid import Grid


def test_grid_size():
    my_grid = Grid()
    assert (9, 9) == (len(my_grid.cells), len(my_grid.cells[0]))


def test_default_grid_values():
    my_default_grid = Grid()
    assert 0 == sum(sum(cell.value for cell in row)
                    for row in my_default_grid.cells)


def test_get_cell_in_grid():
    my_grid = Grid()
    assert 0 == my_grid.get_cell(0, 0).value


def test_modify_cell_in_grid():
    my_grid = Grid()
    my_grid.change_cell_value(0, 0, 5)
    assert 5 == my_grid.get_cell(0, 0).value


def test_modify_cell_in_grid_exeption():
    my_grid = Grid()
    with pytest.raises(ValueError) as excinfo:
        my_grid.change_cell_value(0, 0, 12)
    assert str(excinfo.value) == "Cell value must be between 0 and 9"
