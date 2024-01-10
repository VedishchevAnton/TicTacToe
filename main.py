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

    def __check_index(self, index):
        """
        Функция проверка: Если индексы указаны неверно
        (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение
         """
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
        r, c = index
        if not (0 <= r < self._size) or (0 <= c < self._size):
            raise IndexError('некорректно указанные индексы')





