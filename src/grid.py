from src.cell import Cell


class Grid:
    def __init__(self):
        self.cells = [[Cell() for _ in range(9)] for _ in range(9)]

    def get_cell(self, row, col):
        return self.cells[row][col]
