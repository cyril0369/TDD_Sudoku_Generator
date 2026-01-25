import random
from src.sudoku import Sudoku
from src.grid import Grid


def generate_suduku(difficulty):
    print(f"generation d'un grille de difficulté {difficulty}")
    if difficulty == "easy":
        target = random.randint(30, 35)
    elif difficulty == "medium":
        target = random.randint(36, 45)
    elif difficulty == "hard":
        target = random.randint(46, 52)
    elif difficulty == "expert":
        target = random.randint(53, 58)
    sudoku = Sudoku()
    sudoku.is_valid(0)
    sudoku.remove_n_cells(target)
    return sudoku


def generate_sudoku_from_json(json):
    grid_json = [
        [cell["value"] for cell in json["sudoku"]["grid"]["cells"][i]]
        for i in range(9)
    ]
    grid = Grid()
    grid.change_grid(grid_json)
    sudoku = Sudoku(grid)
    return sudoku
