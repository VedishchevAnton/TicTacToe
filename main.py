from random import randint


class Cell:
    def __init__(self):
        self._value = 0  # value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        return self._value == 0  # bool(cell) - возвращает True,
        # если клетка свободна (value = 0) и False - в противном случае.


class TicTacToe:

    def __init__(self):
        self._size = 3
        self._win = 0  # 0 - игра, 1 - победа человека, 2 - победа компьютера, 3 - ничья
        self.pole = tuple(
            tuple(Cell() for _ in range(self._size)) for _ in range(self._size))  # двумерный кортеж, размером 3x3.




