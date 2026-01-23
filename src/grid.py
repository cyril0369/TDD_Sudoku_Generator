from src.cell import Cell


class Grid:
    def __init__(self):
        self.cells = [[Cell() for _ in range(9)] for _ in range(9)]

    def __eq__(self, grid):
        if not isinstance(grid, Grid):
            return NotImplemented
        for i in range(9):
            for j in range(9):
                if self.cells[i][j] != grid.cells[i][j]:
                    return False
        return True

    def get_cell(self, row, col):
        return self.cells[row][col]

    def change_cell_value(self, row, col, new_value):
        self.cells[row][col].change_value(new_value)

    def change_grid(self, new_grid):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].change_value(new_grid[i][j])
