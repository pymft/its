# Unnamed Game 

### usage

* convert `.ui` file to `.py` file:
```shell
pyuic5 form.ui > form.py
```

* to run: 
```shell 
python3.7 app.py
```

### solution 

#### `app.py`

```python
#!/usr/bin/python3

import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt

from form import Ui_Dialog


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()

        self.ui.setupUi(self)
        self.show()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Down:
            self.ui.down()
        else:
            print(e.key())


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

```

#### `form.py`

```python
from PyQt5 import QtCore, QtGui, QtWidgets
import game

class Ui_Dialog(object):
    W = 4
    H = 4
    MARG = 30
    SIZ = 60

    def setupUi(self, Dialog):
        self.game_board = game.MyGame(w=self.W, h=self.H)

        Dialog.setObjectName("My New Title")
        var = self.W * (self.SIZ + self.MARG) + self.MARG
        Dialog.resize(var, var)

        self.lbmat = []
        for i in range(self.W):
            self.lbmat.append([])
            for j in range(self.H):
                self.lbmat[i].append(QtWidgets.QLabel(Dialog))
                self.lbmat[i][j].setGeometry(QtCore.QRect(self.MARG + self.SIZ * i, self.MARG + self.SIZ * j, self.SIZ, self.SIZ))
                self.lbmat[i][j].setAlignment(QtCore.Qt.AlignCenter)
                self.lbmat[i][j].setObjectName("label")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def down(self):
        self.game_board.move_down()
        self.update_board()

    def update_board(self):
        for j in range(self.W):
            for i in range(self.H):
                self.lbmat[i][j].setText(str(self.game_board.board[i][j]))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "My Custom Title"))
        self.update_board()

```

#### `game.py`

```python
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

```