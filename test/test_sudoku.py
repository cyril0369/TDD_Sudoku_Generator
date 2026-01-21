from src.suduku import Sudoku


def test_create_suduku():
    sudoku = Sudoku()
    assert 0 == sudoku.grid.cells[0][0].value
