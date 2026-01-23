class Cell:
    def __init__(self, value=0):
        if not (0 <= value <= 9):
            raise ValueError("Cell value must be between 0 and 9")
        self.value = value

    def __eq__(self, cell):
        if not isinstance(cell, Cell):
            return NotImplemented
        return self.value == cell.value

    def change_value(self, new_value):
        if not (0 <= new_value <= 9):
            raise ValueError("Cell value must be between 0 and 9")
        self.value = new_value
