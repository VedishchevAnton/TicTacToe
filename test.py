class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.pole = tuple([Cell() for _ in range(3) for _ in range(3)])

    def __getitem__(self, indices):
        i, j = indices
        if not (0 <= i < 3 and 0 <= j < 3):
            raise IndexError('некорректно указанные индексы')
        return self.pole[i * 3 + j].value

    def __setitem__(self, indices, value):
        i, j = indices
        if not (0 <= i < 3 and 0 <= j < 3):
            raise IndexError('некорректно указанные индексы')
        self.pole[i * 3 + j].value = value

    def init(self):
        self.pole = tuple([Cell() for _ in range(3) for _ in range(3)])

    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.pole[i * 3 + j].value, end=' ')
            print()

    def human_go(self, i, j):
        if self.pole[i * 3 + j]:
            self.pole[i * 3 + j].value = self.HUMAN_X
        else:
            print("Клетка занята, выберите другую")

    def computer_go(self, i, j):
        import random
        available_cells = [(i, j) for i in range(3) for j in range(3) if self.pole[i * 3 + j]]
        if available_cells:
            i, j = random.choice(available_cells)
            self.pole[i * 3 + j].value = self.COMPUTER_O

    @property
    def is_human_win(self):
        # Логика проверки победы человека
        pass

    @property
    def is_computer_win(self):
        # Логика проверки победы компьютера
        pass

    @property
    def is_draw(self):
        # Логика проверки ничьи
        pass

    def __bool__(self):
        return not (self.is_human_win or self.is_computer_win or self.is_draw)
