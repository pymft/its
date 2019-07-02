from random import randint


class MyGame:
    def __init__(self, w=4, h=4):
        self._w = w
        self._h = h

        self.board = [[0 for j in range(h)] for i in range(w)]
        self._fill_random_cells()


    def _fill_random_cells(self):
        for i in [1, 2]:
            self.board[randint(0, self._w - 1)][randint(0, self._w - 1)] = randint(1, 2) * 2

    def get_row(self, row_num):
        return self.board[row_num]

    def get_col(self, col_num):
        return [r[col_num] for r in self.board]

    def set_row(self, row_num, lst):
        self.board[row_num] =  lst

    def set_col(self, col_num, lst):
        for r, v in enumerate(lst):
            self.board[col_num][r] = v

    def move_down(self):
        direction = -1
        for col in range(self._w):
            tmp_col = self.get_col(col)
            tmp_col = tmp_col[::direction]
            tmp_col = list(filter(lambda x: x, tmp_col))
            # complete me
            tmp_col = tmp_col[::direction]
            for i in range(self._h - len(tmp_col)):
                tmp_col.append(0)

            self.set_col(col, tmp_col)


