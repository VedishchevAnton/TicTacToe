class Cell:
    def __init__(self):
        self.value = 0  # value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        return self.value == 0  # bool(cell) - возвращает True,
        # если клетка свободна (value = 0) и False - в противном случае.
