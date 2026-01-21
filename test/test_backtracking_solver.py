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
    solveur.affichage()
    solveur.is_valid(0)
    solveur.affichage()
