from src.grid import Grid
from src.backtracking_solver import BacktrackingSolver

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
solveur = BacktrackingSolver(grid_exemple)

solveur_from_scratch = BacktrackingSolver(Grid())
solveur_from_scratch.is_valid(0)


def test_create_solveur():
    grid = Grid()
    solveur = BacktrackingSolver(grid)
    assert isinstance(solveur.grid, Grid)


def test_not_on_row():
    assert solveur.not_on_row(2, 2)


def test_on_row():
    assert not solveur.not_on_row(9, 0)


def test_not_on_col():
    assert solveur.not_on_col(2, 1)


def test_on_col():
    assert not solveur.not_on_col(9, 8)


def test_not_on_block():
    assert solveur.not_on_block(3, 1, 1)


def test_on_block():
    assert not solveur.not_on_block(9, 2, 2)


def test_is_valid_out_of_grill():
    assert solveur.is_valid(81)


def test_is_valid():
    assert solveur.is_valid(0)


def test_generate_different_grids():
    grid1 = Grid()
    grid2 = Grid()
    solveur1 = BacktrackingSolver(grid1)
    solveur2 = BacktrackingSolver(grid2)
    solveur1.is_valid(0)
    solveur2.is_valid(0)
    assert solveur1.grid != solveur2.grid


def test_unicity_numbers_by_line():
    grid = solveur_from_scratch.grid
    for i in range(9):
        numbers = [grid.cells[i][j].value for j in range(9)]
        assert len(numbers) == len(set(numbers))
        assert set(numbers) == set(range(1, 10))


def test_unicity_numbers_by_column():
    grid = solveur_from_scratch.grid
    for j in range(9):
        numbers = [grid.cells[i][j].value for i in range(9)]
        assert len(numbers) == len(set(numbers))
        assert set(numbers) == set(range(1, 10))


def test_unicity_numbers_by_block():
    grid = solveur_from_scratch.grid
    for block_i in range(3):
        for block_j in range(3):
            numbers = [grid.cells[i][j].value for i in range(
                block_i*3, block_i*3+3) for j in range(block_j*3, block_j*3+3)]
            assert len(numbers) == len(set(numbers))
            assert set(numbers) == set(range(1, 10))


def test_unicity_solution():
    assert 1 == solveur.count_solutions()


def test_several_solution():
    solveur = BacktrackingSolver(Grid())
    assert 1 < solveur.count_solutions()
