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
