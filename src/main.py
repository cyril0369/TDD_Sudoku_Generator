from backtracking_solver import BacktrackingSolver
from grid import Grid


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

solveur.affichage()
solveur.is_valid(0)
solveur.affichage()
