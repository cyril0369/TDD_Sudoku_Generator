import random
from sudoku import Sudoku


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


sudoku = generate_suduku("expert")
sudoku.affichage()
