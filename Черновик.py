"""def gen_cord():
Генератор
всех
возможных
комбинаций
координат
    all_comb = [[x / 10, x % 10] for x in range(100)]
    for_1_ship = filter(lambda x: x[0] in range(2, 8) and x[1] in range(2, 8), all_comb)
    for_other_ship = filter(lambda x: x not in for_1_ship, all_comb)
    cord_comb = {1: [[x] for x in for_1_ship], 2: [], 3: [], 4: []}
    for ship in filter(lambda x: x != 1, cord_comb.keys()):
        for cord in for_other_ship:
            hor_direction = [cord] + [[cord[0] + x, cord[1]] for x in range(1, ship)]
            ver_direction = [cord] + [[cord[0], cord[1] + x] for x in range(1, ship)]
            for dir_d in [hor_direction, ver_direction]:
                for cord_d in dir_d:
                    if cord_d not in for_other_ship:
                        break
                else:
                    cord_comb[ship].append(dir_d)
    return cord_comb

from PyQt5 import QtWidgets


class App(QtWidgets.QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.data = [1, 2, 3, 4, 5]

        self.table = QtWidgets.QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(['V1', 'V2', 'V3', 'V4', 'V5'])
        self.table.setMouseTracking(True)

        # ------------------------------------------------------------
        # Этот сигнал испускается при каждом щелчке ячейки в таблице.
        self.table.cellClicked[int, int].connect(self.clickedRowColumn)

        # Этот сигнал испускается, когда ячейка, указанная в строке и столбце, активирована
        self.table.cellActivated[int, int].connect(self.activatedRowColumn)

        # Этот сигнал излучается всякий раз, когда данные элемента в ячейке изменяются.
        self.table.cellChanged[int, int].connect(self.changedRowColumn)

        # Этот сигнал испускается, когда курсор мыши входит в ячейку.
        self.table.cellEntered[int, int].connect(self.enteredRowColumn)
        # -------------------------------------------------------------

        self.lbl = QtWidgets.QLabel()
        self.btn_add = QtWidgets.QPushButton('Добавить строку')

        self.btn_add.clicked.connect(self.add_row)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.lbl)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.btn_add)
        self.setLayout(self.layout)

    def activatedRowColumn(self, r, c):
        self.lbl.setText("Активная: строка->`{}`, столбец->`{}`, ячейка->`<b> {} : {}</b> `".format(r, c, r, c, ))

    def changedRowColumn(self, r, c):
        self.lbl.setText("Изменились данные ячейки->`<b> {} : {}<b>`".format(r, c, ))

    def clickedRowColumn(self, r, c):
        print(self.sender())
        self.lbl.setText("<b>Вы кликнули ячейку->`<i style='color:blue'> {} : {} </i>`</b>".format(r, c, ))

    def enteredRowColumn(self, r, c):
        self.lbl.setText("<b>Курсор мыши в ячейкe->`<i style='color:red'> {} : {} </i>`</b>".format(r, c, ))

    def add_row(self):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        for i in range(5):
            self.table.setItem(rowPosition,
                               i,
                               QtWidgets.QTableWidgetItem(str(self.data[i])))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ex = App()
    ex.show()
    app.exec_()"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CreatePage(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.homeBtn = QPushButton("Home")

        self.frontLabel = QLabel("Front")
        self.frontLabel.setFont(QFont("Decorative", 20))
        self.frontEdit = QTextEdit(placeholderText="frontEdit")
        self.frontEdit.setFont(QFont("Decorative", 11))

        self.backLabel = QLabel("Back")
        self.backLabel.setFont(QFont("Decorative", 20))
        self.backEdit = QTextEdit(placeholderText="backEdit")
        self.backEdit.setFont(QFont("Decorative", 11))

        grid = QGridLayout()
        grid.addWidget(self.homeBtn, 0, 0, alignment=Qt.AlignTop | Qt.AlignLeft)
        grid.addWidget(self.frontLabel, 1, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.frontEdit, 2, 0)
        grid.addWidget(self.backLabel, 3, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.backEdit, 4, 0)

        self.setLayout(grid)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = CreatePage()
    myapp.show()
    sys.exit(app.exec_())
