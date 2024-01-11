from random import randint

from cell import Cell


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
        Метод проверка: Если индексы указаны неверно
        (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение
         """
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
        r, c = index  # распаковка
        if not (0 <= r < self._size) or not (0 <= c < self._size):
            raise IndexError('некорректно указанные индексы')

    def __update_win_status(self):
        """Метод проверки статуса игры"""
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
        """Метод очистки игрового поля"""
        for i in range(self._size):
            for j in range(self._size):
                self.pole[i][j].value = 0
        self._win = 0

    def show(self):
        """Метод отображение текущего состояния игрового поля"""
        for row in self.pole:
            print(*map(lambda x: '#' if x.value == 0 else x.value, row))
        print('--------------------------------')

    def human_go(self):
        """Метод реализации хода игрока"""
        if not self:
            return  # возвращает False, если игра окончена

        while True:
            user_input = input('Введите координаты клетки: ')
            coordinates = user_input.split()
            if len(coordinates) != 2:
                print("Пожалуйста, введите две координаты.")
                continue

            i, j = map(int, coordinates)
            if not (0 <= i < self._size) or not (0 <= j < self._size):
                print("Координаты вне диапазона.")
                continue

            if self[i, j] == self.FREE_CELL:
                self[i, j] = self.HUMAN_X
                break

    def computer_go(self):
        """Метод реализации хода компьютера"""
        if not self:
            return  # возвращает False, если игра окончена

        while True:
            i = randint(0, self._size - 1)
            j = randint(0, self._size - 1)
            if self[i, j] != self.FREE_CELL:
                continue
            self[i, j] = self.COMPUTER_O
            break

    @property
    def is_human_win(self):
        return self._win == 1

    @property
    def is_computer_win(self):
        return self._win == 2

    @property
    def is_draw(self):
        return self._win == 3

    def __bool__(self):
        return self._win == 0 and self._win not in (1, 2, 3)
