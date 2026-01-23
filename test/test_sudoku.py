from src.grid import Grid
from src.sudoku import Sudoku

grid = [
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
grid_exemple = Grid()
grid_exemple.change_grid(grid)
sudoku_exemple = Sudoku(grid_exemple)

sudoku_from_scratch = Sudoku()
sudoku_from_scratch.is_valid(0)


def test_create_sudoku():
    grid = Grid()
    solveur = Sudoku(grid)
    assert isinstance(solveur.grid, Grid)


def test_not_on_row():
    assert sudoku_exemple.not_on_row(2, 2)


def test_on_row():
    assert not sudoku_exemple.not_on_row(9, 0)


def test_not_on_col():
    assert sudoku_exemple.not_on_col(2, 1)


def test_on_col():
    assert not sudoku_exemple.not_on_col(9, 8)


def test_not_on_block():
    assert sudoku_exemple.not_on_block(3, 1, 1)


def test_on_block():
    assert not sudoku_exemple.not_on_block(9, 2, 2)


def test_is_valid_out_of_grill():
    assert sudoku_exemple.is_valid(81)


def test_is_valid():
    assert sudoku_exemple.is_valid(0)


def test_generate_different_grids():
    grid1 = Grid()
    grid2 = Grid()
    solveur1 = Sudoku(grid1)
    solveur2 = Sudoku(grid2)
    solveur1.is_valid(0)
    solveur2.is_valid(0)
    assert solveur1.grid != solveur2.grid


def test_unicity_numbers_by_line():
    grid = sudoku_from_scratch.grid
    for i in range(9):
        numbers = [grid.cells[i][j].value for j in range(9)]
        assert len(numbers) == len(set(numbers))
        assert set(numbers) == set(range(1, 10))


def test_unicity_numbers_by_column():
    grid = sudoku_from_scratch.grid
    for j in range(9):
        numbers = [grid.cells[i][j].value for i in range(9)]
        assert len(numbers) == len(set(numbers))
        assert set(numbers) == set(range(1, 10))


def test_unicity_numbers_by_block():
    grid = sudoku_from_scratch.grid
    for block_i in range(3):
        for block_j in range(3):
            numbers = [grid.cells[i][j].value for i in range(
                block_i*3, block_i*3+3) for j in range(block_j*3, block_j*3+3)]
            assert len(numbers) == len(set(numbers))
            assert set(numbers) == set(range(1, 10))


def test_unicity_solution():
    sudoku = Sudoku(grid_exemple)
    assert 1 == sudoku.count_solutions()


def test_several_solution():
    sudoku = Sudoku()
    assert 1 < sudoku.count_solutions()


def test_remove_one_cell():
    sudoku_from_scratch.remove_cell(4, 5)
    assert 0 == sudoku_from_scratch.grid.cells[4][5].value


def test_count_zeros():
    assert 1 == sudoku_from_scratch.count_zeros()


def test_return_fill_cell():
    sudoku_from_scratch.affichage()
    (i, j) = sudoku_from_scratch.return_fill_cell()
    assert 0 < sudoku_from_scratch.grid.cells[i][j].value


def test_remove_n_cells():
    sudoku_from_scratch.remove_n_cells(10)
    zeros = sudoku_from_scratch.count_zeros()
    assert 11 == zeros
