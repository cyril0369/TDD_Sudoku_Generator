import pytest
from src.grid import Grid


grid_exemple = [
    [9, 0, 0, 1, 0, 0, 0, 0, 5],
    [0, 0, 5, 0, 9, 0, 2, 0, 1],
    [8, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 6, 0, 0, 9],
    [2, 0, 0, 3, 0, 0, 0, 0, 6],
    [0, 0, 0, 2, 0, 0, 9, 0, 0],
    [0, 0, 1, 9, 0, 4, 5, 7, 0]
]


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
    with pytest.raises(ValueError) as e:
        my_grid.change_cell_value(0, 0, 12)
    assert str(e.value) == "Cell value must be between 0 and 9"


def test_modify_grid():
    grid = Grid()
    grid.change_grid(grid_exemple)
    assert 9 == grid.get_cell(0, 0).value


def test_grids_equals():
    grid1 = Grid()
    grid2 = Grid()
    assert grid1 == grid2
