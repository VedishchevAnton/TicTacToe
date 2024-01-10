from random import randint


class Cell:
    def __init__(self):
        self.value = 0  # value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        return self.value == 0  # bool(cell) - возвращает True,
        # если клетка свободна (value = 0) и False - в противном случае.


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

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
        r, c = index  # распаковка
        if not (0 <= r < self._size) or (0 <= c < self._size):
            raise IndexError('некорректно указанные индексы')

    def __update_win_status(self):
        """Функция проверки статуса игры"""
        for row in self.pole:  # проверка в строках
            if all(x.value == self.HUMAN_X for x in row):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self._win = 2
                return

        for i in range(self._size):  # проверка в столбцах
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self._win = 1
                return

            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self._win = 2
                return

        # проверка в диагоналях
        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self._size)) or \
                all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(self._size)):
            self._win = 1
            return

        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self._size)) or \
                all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(self._size)):
            self._win = 2
            return

        # проверка ничьи
        if all(x.value != self.FREE_CELL for row in self.pole for x in row):
            self._win = 3
            return

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item  # распаковка
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        r, c = key
        self.pole[r][c].value = value
        self.__update_win_status()

    def init(self):
        """Функция очистки игрового поля"""
        for i in range(self._size):
            for j in range(self._size):
                self.pole[i][j].value = 0
        self._win = 0


