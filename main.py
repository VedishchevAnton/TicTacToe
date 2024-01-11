import random


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2

    def __init__(self):
        self.__n = 3
        self.pole = tuple(tuple(Cell() for _ in range(self.__n)) for _ in range(self.__n))
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    def init(self):
        self.clear()

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    def __check(self, item):
        if type(item) != tuple or len(item) != 2:
            raise IndexError('неверный индекс клетки')
        for i in item:
            if not isinstance(i, int) or i < 0 or i > 2:
                raise IndexError('неверный индекс клетки')

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, value):
        self.__is_human_win = value

    def __human_win_method(self):
        for i in range(self.__n):
            j = 0
            m = 0
            while j < self.__n:
                if self.pole[i][j].value == self.HUMAN_X:
                    m += 1
                j += 1
            if m == 3:
                return True
            j = 0
            n = 0
            while j < self.__n:
                if self.pole[j][i].value == self.HUMAN_X:
                    n += 1
                j += 1
            if n == 3:
                return True
        s = 0
        for k in range(self.__n):
            if self.pole[k][k].value == self.HUMAN_X:
                s += 1
        if s == 3:
            return True

        return False

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, value):
        self.__is_computer_win = value

    def __computer_win_method(self):
        for i in range(self.__n):
            j = 0
            m = 0
            while j < self.__n:
                if self.pole[i][j].value == self.COMPUTER_O:
                    m += 1
                j += 1
            if m == 3:
                return True
            j = 0
            n = 0
            while j < self.__n:
                if self.pole[j][i].value == self.COMPUTER_O:
                    n += 1
                j += 1
            if n == 3:
                return True
        s = 0
        for k in range(self.__n):
            if self.pole[k][k].value == self.COMPUTER_O:
                s += 1
        if s == 3:
            return True

        return False

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, value):
        self.__is_draw = value

    def __draw_method(self):
        m = 0
        for i in range(self.__n):
            for j in range(self.__n):
                item = i, j
                if self.pole[i][j].value != self.FREE_CELL:
                    m += 1
        if m == self.__n ** 2:
            return True
        return False

    def __setitem__(self, key, value):
        self.__check(key)
        r, c = key
        if self.pole[r][c]:
            self.pole[r][c].value = value
        if self.__human_win_method():
            self.__is_human_win = True
        if self.__computer_win_method():
            self.__is_computer_win = True
        if self.__draw_method():
            self.__is_draw = True

    def __getitem__(self, item):
        r, c = item
        return self.pole[r][c].value

    def show(self):
        for k in range(self.__n):
            print([i.value for i in self.pole[k]])

    def human_go(self):
        coords = [int(i) for i in input().split()]
        item = coords[0], coords[1]
        self.__check(item)
        if self.__getitem__(item) == self.FREE_CELL:
            self.__setitem__(item, self.HUMAN_X)
        else:
            raise ValueError('клетка уже занята')

    def computer_go(self):
        flag = True
        while flag:
            i, j = random.randint(0, self.__n - 1), random.randint(0, self.__n - 1)
            item = i, j
            if self.pole[i][j].value == self.FREE_CELL:
                self.__setitem__(item, self.COMPUTER_O)
                flag = False

    def __end(self):
        flag = False
        if self.__human_win_method():
            self.__is_human_win = True
            flag = True

        if self.__computer_win_method():
            self.__is_computer_win = True
            flag = True

        if self.__draw_method():
            self.__is_draw = True
            flag = True
        return flag

    def __bool__(self):
        return not self.__end()


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
