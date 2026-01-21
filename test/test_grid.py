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
