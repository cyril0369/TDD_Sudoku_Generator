class Cell:
    def __init__(self, value=0):
        if not (0 <= value <= 9):
            raise ValueError("Cell value must be between 0 and 9")
        self.value = value
