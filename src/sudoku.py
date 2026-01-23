import random
from grid import Grid


class Sudoku():
    def __init__(self, grid=None):
        self.grid = grid if grid is not None else Grid()

    def affichage(self):
        for i in range(9):
            for j in range(9):
                val = self.grid.cells[i][j].value
                ch = '.' if val == 0 else str(val)
                end_char = '|' if (j + 1) % 3 == 0 and j != 8 else ' '
                print(ch + end_char, end='')
            print()
            if (i + 1) % 3 == 0 and i != 8:
                print("------------------")
        print()

    def not_on_row(self, value, row):
        for i in range(9):
            if value == self.grid.cells[row][i].value:
                return False
        return True

    def not_on_col(self, value, col):
        for i in range(9):
            if value == self.grid.cells[i][col].value:
                return False
        return True

    def not_on_block(self, value, i_block, j_block):
        for i in range(i_block*3, i_block*3 + 3):
            for j in range(j_block*3, j_block*3 + 3):
                if value == self.grid.cells[i][j].value:
                    return False
        return True

    def is_valid(self, position=None, id=0):
        if (position == 9*9):
            return True

        i = position//9
        j = position % 9

        if (self.grid.cells[i][j].value != 0):
            return self.is_valid(position+1)

        nums = list(range(1, 10))
        random.shuffle(nums)
        for k in nums:
            row_ok = self.not_on_row(k, i)
            col_ok = self.not_on_col(k, j)
            block_ok = self.not_on_block(k, i//3, j // 3)
            if row_ok and col_ok and block_ok:
                self.grid.change_cell_value(i, j, k)
                if self.is_valid(position+1):
                    return True
        self.grid.change_cell_value(i, j, 0)
        return False

    def count_solutions(self, position=0, limit=2):
        if position == 9*9:
            return 1

        i = position // 9
        j = position % 9

        if self.grid.cells[i][j].value != 0:
            return self.count_solutions(position+1, limit)

        count = 0
        for k in range(1, 10):
            row_ok = self.not_on_row(k, i)
            col_ok = self.not_on_col(k, j)
            block_ok = self.not_on_block(k, i//3, j//3)
            if row_ok and col_ok and block_ok:
                self.grid.change_cell_value(i, j, k)
                count += self.count_solutions(position+1, limit)
                if count >= limit:
                    self.grid.change_cell_value(i, j, 0)
                    return count
        self.grid.change_cell_value(i, j, 0)
        return count

    def remove_cell(self, i, j):
        self.grid.cells[i][j].value = 0

    def count_zeros(self):
        return sum(1 for i in range(9) for j in range(9)
                   if self.grid.cells[i][j].value == 0)

    def return_fill_cell(self):
        if self.count_zeros == 81:
            return "No fill cell"
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        while self.grid.cells[i][j].value == 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
        return (i, j)

    def remove_n_cells(self, n, limit=64):
        print(f"effacage de {n} case")
        for _ in range(n):
            if self.count_zeros() >= limit:
                return
            (i, j) = self.return_fill_cell()
            v = self.grid.cells[i][j].value
            self.remove_cell(i, j)
            while self.count_solutions() > 1:
                self.grid.change_cell_value(i, j, v)
                (i, j) = self.return_fill_cell()
                v = self.grid.cells[i][j].value
                self.remove_cell(i, j)
        return
