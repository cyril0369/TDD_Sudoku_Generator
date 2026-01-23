import random


class BacktrackingSolver():
    def __init__(self, grid):
        self.grid = grid

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
