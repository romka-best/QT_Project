import sys
from random import randrange
import sqlite3

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QBasicTimer, QCoreApplication

from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QStackedWidget, QMessageBox, QInputDialog, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist

SCREEN_SIZE = [(960, 540), (1280, 720), (1920, 1080)]
COORDS = {
    "A1": (0, 0),
    "A2": (1, 0),
    "A3": (2, 0),
    "A4": (3, 0),
    "A5": (4, 0),
    "A6": (5, 0),
    "A7": (6, 0),
    "A8": (7, 0),
    "A9": (8, 0),
    "A10": (9, 0),
    "B1": (0, 1),
    "B2": (1, 1),
    "B3": (2, 1),
    "B4": (3, 1),
    "B5": (4, 1),
    "B6": (5, 1),
    "B7": (6, 1),
    "B8": (7, 1),
    "B9": (8, 1),
    "B10": (9, 1),
    "C1": (0, 2),
    "C2": (1, 2),
    "C3": (2, 2),
    "C4": (3, 2),
    "C5": (4, 2),
    "C6": (5, 2),
    "C7": (6, 2),
    "C8": (7, 2),
    "C9": (8, 2),
    "C10": (9, 2),
    "D1": (0, 3),
    "D2": (1, 3),
    "D3": (2, 3),
    "D4": (3, 3),
    "D5": (4, 3),
    "D6": (5, 3),
    "D7": (6, 3),
    "D8": (7, 3),
    "D9": (8, 3),
    "D10": (9, 3),
    "E1": (0, 4),
    "E2": (1, 4),
    "E3": (2, 4),
    "E4": (3, 4),
    "E5": (4, 4),
    "E6": (5, 4),
    "E7": (6, 4),
    "E8": (7, 4),
    "E9": (8, 4),
    "E10": (9, 4),
    "F1": (0, 5),
    "F2": (1, 5),
    "F3": (2, 5),
    "F4": (3, 5),
    "F5": (4, 5),
    "F6": (5, 5),
    "F7": (6, 5),
    "F8": (7, 5),
    "F9": (8, 5),
    "F10": (9, 5),
    "G1": (0, 6),
    "G2": (1, 6),
    "G3": (2, 6),
    "G4": (3, 6),
    "G5": (4, 6),
    "G6": (5, 6),
    "G7": (6, 6),
    "G8": (7, 6),
    "G9": (8, 6),
    "G10": (9, 6),
    "H1": (0, 7),
    "H2": (1, 7),
    "H3": (2, 7),
    "H4": (3, 7),
    "H5": (4, 7),
    "H6": (5, 7),
    "H7": (6, 7),
    "H8": (7, 7),
    "H9": (8, 7),
    "H10": (9, 7),
    "I1": (0, 8),
    "I2": (1, 8),
    "I3": (2, 8),
    "I4": (3, 8),
    "I5": (4, 8),
    "I6": (5, 8),
    "I7": (6, 8),
    "I8": (7, 8),
    "I9": (8, 8),
    "I10": (9, 8),
    "J1": (0, 9),
    "J2": (1, 9),
    "J3": (2, 9),
    "J4": (3, 9),
    "J5": (4, 9),
    "J6": (5, 9),
    "J7": (6, 9),
    "J8": (7, 9),
    "J9": (8, 9),
    "J10": (9, 9),
}
players = []

"""Не работают настройки
Отстутствуют некоторые видео и аудио
Код не до конца оптимизирован
Проект готов на 85%"""


class Ui_MainWindow_loading(object):  # loading.py
    """Создаю дизайн виджета загрузки"""

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 170, 961, 101))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.widget = QVideoWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 961, 101))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 360, 961, 181))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(44)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Loading"))
        self.pushButton.setText(_translate("mainWindow", "BEST PRODUCTIONS"))  # loading.py end


class Ui_MainWindow_startmenu(object):  # startmenu.py
    """Создаю дизайн виджета стартового меню"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 100, 481, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.rulesButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rulesButton.setFont(font)
        self.rulesButton.setObjectName("rulesButton")
        self.verticalLayout.addWidget(self.rulesButton)
        self.settingsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.settingsButton.setFont(font)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout.addWidget(self.settingsButton)
        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.videoStartMenu = QVideoWidget(self.centralwidget)
        self.videoStartMenu.setGeometry(QtCore.QRect(0, 0, 961, 100))
        self.videoStartMenu.setObjectName("videoStartMenu")
        self.logoImage1 = QtWidgets.QLabel(self.centralwidget)
        self.logoImage1.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.logoImage1.setText("")
        self.logoImage1.setObjectName("logoImage1")
        self.logoImage2 = QtWidgets.QLabel(self.centralwidget)
        self.logoImage2.setGeometry(QtCore.QRect(860, 0, 100, 100))
        self.logoImage2.setText("")
        self.logoImage2.setObjectName("logoImage2")
        self.videoStartMenu_2 = QVideoWidget(self.centralwidget)
        self.videoStartMenu_2.setGeometry(QtCore.QRect(740, 200, 200, 150))
        self.videoStartMenu_2.setObjectName("videoStartMenu_2")
        self.videoStartMenu_1 = QVideoWidget(self.centralwidget)
        self.videoStartMenu_1.setGeometry(QtCore.QRect(20, 200, 200, 150))
        self.videoStartMenu_1.setObjectName("videoStartMenu_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StartMenu"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.rulesButton.setText(_translate("MainWindow", "RULES"))
        self.settingsButton.setText(_translate("MainWindow", "SETTINGS"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))


class Ui_MainWindow_settings(object):  # settings.py
    """Создаю дизайн виджета загрузки"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(270, 60, 691, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radiopve = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.radiopve.setFont(font)
        self.radiopve.setChecked(False)
        self.radiopve.setObjectName("radiopve")
        self.gridLayout.addWidget(self.radiopve, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 4, 0, 1, 1)
        self.radiopvp = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.radiopvp.setFont(font)
        self.radiopvp.setChecked(True)
        self.radiopvp.setObjectName("radiopvp")
        self.gridLayout.addWidget(self.radiopvp, 0, 0, 1, 1)
        self.videoSettings = QVideoWidget(self.centralwidget)
        self.videoSettings.setGeometry(QtCore.QRect(0, 60, 271, 451))
        self.videoSettings.setObjectName("videoSettings")
        self.logoImage = QtWidgets.QLabel(self.centralwidget)
        self.logoImage.setGeometry(QtCore.QRect(270, 0, 691, 61))
        self.logoImage.setText("")
        self.logoImage.setObjectName("logoImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.backButton.setText(_translate("MainWindow", "<----- Back"))
        self.radiopve.setText(_translate("MainWindow", "PVE"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ENGLISH"))
        self.comboBox.setItemText(1, _translate("MainWindow", "RUSSIAN"))
        self.saveButton.setText(_translate("MainWindow", "SAVE"))
        self.radiopvp.setText(_translate("MainWindow", "PVP"))


class Ui_MainWindow_rules(object):  # rules.py
    """Создаю дизайн виджета правил"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.logoImage = QtWidgets.QLabel(self.centralwidget)
        self.logoImage.setGeometry(QtCore.QRect(270, 0, 691, 61))
        self.logoImage.setText("")
        self.logoImage.setObjectName("logoImage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 961, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rules"))
        self.backButton.setText(_translate("MainWindow", "<----- Back"))


class Ui_MainWindow_ready(object):  # readygame.py
    """Создаю дизайн виджета начала игры"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boardMap = QtWidgets.QTableWidget(self.centralwidget)
        self.boardMap.setGeometry(QtCore.QRect(0, 50, 531, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.boardMap.setFont(font)
        self.boardMap.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.boardMap.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.boardMap.setObjectName("boardMap")
        self.boardMap.setColumnCount(10)
        self.boardMap.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(9, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 531, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playerLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playerLabel.setFont(font)
        self.playerLabel.setObjectName("playerLabel")
        self.horizontalLayout_2.addWidget(self.playerLabel)
        self.readyButton = QtWidgets.QPushButton(self.centralwidget)
        self.readyButton.setGeometry(QtCore.QRect(530, 0, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.readyButton.setFont(font)
        self.readyButton.setObjectName("readyButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(530, 50, 261, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.linkorImage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.linkorImage.setText("")
        self.linkorImage.setObjectName("linkorImage")
        self.verticalLayout.addWidget(self.linkorImage)
        self.kreyserImage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.kreyserImage.setText("")
        self.kreyserImage.setObjectName("kreyserImage")
        self.verticalLayout.addWidget(self.kreyserImage)
        self.esminecImage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.esminecImage.setText("")
        self.esminecImage.setObjectName("esminecImage")
        self.verticalLayout.addWidget(self.esminecImage)
        self.torpedImage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.torpedImage.setText("")
        self.torpedImage.setObjectName("torpedImage")
        self.verticalLayout.addWidget(self.torpedImage)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(790, 50, 171, 461))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.linkorButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.linkorButton.setFont(font)
        self.linkorButton.setObjectName("linkorButton")
        self.verticalLayout_2.addWidget(self.linkorButton)
        self.kreyserButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kreyserButton.setFont(font)
        self.kreyserButton.setObjectName("kreyserButton")
        self.verticalLayout_2.addWidget(self.kreyserButton)
        self.esminecButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.esminecButton.setFont(font)
        self.esminecButton.setObjectName("esminecButton")
        self.verticalLayout_2.addWidget(self.esminecButton)
        self.torpedButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.torpedButton.setFont(font)
        self.torpedButton.setObjectName("torpedButton")
        self.verticalLayout_2.addWidget(self.torpedButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.boardMap.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.boardMap.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.boardMap.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.boardMap.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.boardMap.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.boardMap.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.boardMap.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.boardMap.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.boardMap.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.boardMap.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.boardMap.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.boardMap.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.boardMap.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.boardMap.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.boardMap.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.boardMap.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F"))
        item = self.boardMap.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "G"))
        item = self.boardMap.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "H"))
        item = self.boardMap.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "I"))
        item = self.boardMap.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "J"))
        self.playerLabel.setText(_translate("MainWindow", "PLAYER1"))
        self.readyButton.setText(_translate("MainWindow", "I am ready"))
        self.linkorButton.setText(_translate("MainWindow", "Choose where to put"))
        self.kreyserButton.setText(_translate("MainWindow", "Choose where to put"))
        self.esminecButton.setText(_translate("MainWindow", "Choose where to put"))
        self.torpedButton.setText(_translate("MainWindow", "Choose where to put"))


class Ui_MainWindow_pvp(object):  # gamepvp.py
    """Создаю дизайн виджета самой игры"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 441, 461))
        self.tableWidget.setMinimumSize(QtCore.QSize(441, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(520, 50, 441, 461))
        self.tableWidget_2.setMinimumSize(QtCore.QSize(441, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(10)
        self.tableWidget_2.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        self.vsLable = QtWidgets.QLabel(self.centralwidget)
        self.vsLable.setGeometry(QtCore.QRect(440, 230, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Digital Counter 7")
        font.setPointSize(36)
        self.vsLable.setFont(font)
        self.vsLable.setText("")
        self.vsLable.setObjectName("vsLable")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.board1Label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.board1Label.setFont(font)
        self.board1Label.setObjectName("board1Label")
        self.horizontalLayout.addWidget(self.board1Label)
        self.linkorP1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.linkorP1.setText("")
        self.linkorP1.setObjectName("linkorP1")
        self.horizontalLayout.addWidget(self.linkorP1)
        self.kreyserP1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.kreyserP1.setText("")
        self.kreyserP1.setObjectName("kreyserP1")
        self.horizontalLayout.addWidget(self.kreyserP1)
        self.esminecP1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.esminecP1.setText("")
        self.esminecP1.setObjectName("esminecP1")
        self.horizontalLayout.addWidget(self.esminecP1)
        self.torpedP1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.torpedP1.setText("")
        self.torpedP1.setObjectName("torpedP1")
        self.horizontalLayout.addWidget(self.torpedP1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(520, 0, 441, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.board2Label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.board2Label.setFont(font)
        self.board2Label.setObjectName("board2Label")
        self.horizontalLayout_2.addWidget(self.board2Label)
        self.linkorP2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.linkorP2.setText("")
        self.linkorP2.setObjectName("linkorP2")
        self.horizontalLayout_2.addWidget(self.linkorP2)
        self.kreyserP2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.kreyserP2.setText("")
        self.kreyserP2.setObjectName("kreyserP2")
        self.horizontalLayout_2.addWidget(self.kreyserP2)
        self.esminecP2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.esminecP2.setText("")
        self.esminecP2.setObjectName("esminecP2")
        self.horizontalLayout_2.addWidget(self.esminecP2)
        self.torpedP2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.torpedP2.setText("")
        self.torpedP2.setObjectName("torpedP2")
        self.horizontalLayout_2.addWidget(self.torpedP2)
        self.labelWho = QtWidgets.QLabel(self.centralwidget)
        self.labelWho.setGeometry(QtCore.QRect(440, 0, 81, 51))
        self.labelWho.setText("")
        self.labelWho.setObjectName("labelWho")
        self.courseButton = QtWidgets.QPushButton(self.centralwidget)
        self.courseButton.setGeometry(QtCore.QRect(440, 50, 81, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.courseButton.setFont(font)
        self.courseButton.setObjectName("courseButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Game PVP"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "G"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "H"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "I"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "J"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "G"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "H"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "I"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "J"))
        self.board1Label.setText(_translate("MainWindow", "Your board"))
        self.board2Label.setText(_translate("MainWindow", "Enemy\'s board"))
        self.courseButton.setText(_translate("MainWindow", "Course"))


class Ui_MainWindow_win(object):
    """Создаю дизайн виджета выиграша"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 180, 760, 131))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QVideoWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 0, 510, 100))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 320, 510, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WIN"))
        self.pushButton.setText(_translate("MainWindow", "EXIT"))


class Loading_Main(QMainWindow, Ui_MainWindow_loading):
    """Псевдозагрузочная анимация, но в дальнейшем данное умение пригодится"""

    def __init__(self, parent=None):
        super(Loading_Main, self).__init__(parent)
        self.setupUi(self)
        self.mediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.timer = QBasicTimer()
        self.step = 0
        self.initUI()

    def initUI(self):
        self.load_mp4("videos/animation.gif")
        self.pushButton.clicked.connect(self.doAction)

    def load_mp4(self, filename):  # Загружаю ГИФ-файл
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QMediaContent(media)
        self.mediaplayer.setMedia(content)
        self.mediaplayer.play()
        self.mediaplayer.setVideoOutput(self.widget)

    def timerEvent(self, e):  # Загрузка
        if self.step >= 100:
            self.timer.stop()
            self.pushButton.setText('Finished')
            windows.setCurrentIndex(1)
            return

        self.step = self.step + randrange(0, 10)
        self.progressBar.setValue(self.step)

    def doAction(self):  # Если пользователь нажимает кнопку
        if self.timer.isActive():
            self.timer.stop()
            self.pushButton.setText('BEST PRODUCTIONS')
        else:
            self.timer.start(100, self)
            self.pushButton.setText('Stop')


class Startmenu_Main(QMainWindow, Ui_MainWindow_startmenu):  # Нужно вставить видео
    """Стартовое меню, где можно переключаться между окнами, а также выйти из игры"""

    def __init__(self, parent=None):
        super(Startmenu_Main, self).__init__(parent)
        self.setupUi(self)

        self.LOGOBP = QPixmap("images/logobp.svg")
        self.mediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.initUI()

    def initUI(self):
        self.logoImage1.setPixmap(self.LOGOBP)
        self.logoImage2.setPixmap(self.LOGOBP)

        self.load_mp4("videos/animation800.gif")

        # Задаю цвет кнопкам
        self.startButton.setStyleSheet("color: white; background-color: #082567;"
                                       "border-radius: 20px;")
        self.rulesButton.setStyleSheet("color: white; background-color: #082567;"
                                       "border-radius: 20px;")
        self.settingsButton.setStyleSheet("color: white; background-color: #082567;"
                                          "border-radius: 20px;")
        self.exitButton.setStyleSheet("color: white; background-color: #082567;"
                                      "border-radius: 20px;")

        self.startButton.clicked.connect(self.to_start)
        self.rulesButton.clicked.connect(self.to_rules)
        self.exitButton.clicked.connect(QCoreApplication.instance().quit)
        self.settingsButton.clicked.connect(self.to_settings)

    def load_mp4(self, filename):  # Загрузка GIF-файла
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QMediaContent(media)
        self.mediaplayer.setMedia(content)
        self.mediaplayer.play()
        self.mediaplayer.setVideoOutput(self.videoStartMenu_1)

    def to_settings(self):  # Переходит в меню настроек
        windows.setCurrentIndex(2)

    def to_rules(self):  # Переходит в меню правил
        windows.setCurrentIndex(3)

    def to_start(self):  # Переходит в меню начала игры
        windows.setCurrentIndex(4)


class Settings_Main(QMainWindow, Ui_MainWindow_settings):  # Доработать всё!
    """Меню настроек, где можно изменить режим игры, а также сменить язык"""

    def __init__(self, parent=None):
        super(Settings_Main, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.LOGOSB = QPixmap("images/logosb.svg")
        self.logoImage.setPixmap(self.LOGOSB)

        # Задаю цвет кнопкам
        self.backButton.setStyleSheet("color: white; background-color: #082567;"
                                      "border-radius: 20px;")
        self.saveButton.setStyleSheet("color: white; background-color: #082567;"
                                      "border-radius: 20px;")

        self.radiopve.toggled.connect(self.changeP)
        self.radiopvp.toggled.connect(self.changeP)
        self.backButton.clicked.connect(self.to_start)
        self.saveButton.clicked.connect(self.to_save)

    def to_start(self):  # Переход в стартовое меню
        windows.setCurrentIndex(1)

    def to_save(self):  # Сохраняет изменения
        pass

    def changeP(self):  # Меняет режим игры
        pass
        # who = self.sender().text()


class Rules_Main(QMainWindow, Ui_MainWindow_rules):
    """Меню правил"""

    def __init__(self, parent=None):
        super(Rules_Main, self).__init__(parent)
        self.setupUi(self)
        self.LOGOSB = QPixmap("images/logosb.svg")
        self.initUI()

    def initUI(self):
        self.backButton.setStyleSheet("color: white; background-color: #082567;"
                                      "border-radius: 20px;")
        self.backButton.clicked.connect(self.to_start)

        self.logoImage.setPixmap(self.LOGOSB)
        self.label.setText("""The game is played on four grids, two for each player.
        The grids are typically square – usually 10×10 – and the individual squares 
        in the grid are identified by letter and number.
        
        On one grid the player arranges ships and records the shots by the opponent.
        
        On the other grid the player records their own shots.
        
        Before play begins, each player secretly arranges their ships on their primary grid.
        
        Each ship occupies a number of consecutive squares on the grid,
        arranged either horizontally or vertically.
        
        The number of squares for each ship is determined by the type of the ship.
        
        The ships cannot overlap (i.e., only one ship can occupy any given square in the grid).
        The types and numbers of ships allowed are the same for each player.""")

    def to_start(self):  # Переход в стартовое меню
        windows.setCurrentIndex(1)


class Ready_Main(QMainWindow, Ui_MainWindow_ready):  # Вставить изображения, оптимизировать код
    """Меню подготовления к самой игре"""

    def __init__(self, parent=None):
        super(Ready_Main, self).__init__(parent)
        self.setupUi(self)

        self.map = SeaMap(self.boardMap)
        self.new_count()  # Обновление переменных-счётчиков
        self.new_map()  # Обновление карты
        self.new_images('green')  # Добавления изображений

        self.initUI()

    def initUI(self):
        self.readyButton.clicked.connect(self.start)

        # Задаю цвет и форму кнопкам
        self.readyButton.setStyleSheet("color: white; background-color: #082567;"
                                       "border-radius: 10px;")
        self.linkorButton.setStyleSheet("color: white; background-color: #082567;"
                                        "border-radius: 10px;")
        self.kreyserButton.setStyleSheet("color: white; background-color: #082567;"
                                         "border-radius: 10px;")
        self.esminecButton.setStyleSheet("color: white; background-color: #082567;"
                                         "border-radius: 10px;")
        self.torpedButton.setStyleSheet("color: white; background-color: #082567;"
                                        "border-radius: 10px;")

        self.linkorButton.clicked.connect(self.setLinkor)
        self.kreyserButton.clicked.connect(self.setKreyser)
        self.esminecButton.clicked.connect(self.setEsminec)
        self.torpedButton.clicked.connect(self.setTorped)

    def new_map(self):  # Метод создаёт(обновляет) карту
        for i in range(self.boardMap.columnCount()):
            for j in range(self.boardMap.rowCount()):
                cell = QTableWidgetItem(".")
                cell.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.boardMap.setItem(i, j, cell)
        self.boardMap.resizeColumnsToContents()
        self.boardMap.resizeRowsToContents()

    def new_db(self, who):  # Занесения данных в базу данных
        self.con = sqlite3.connect("Players.db")
        self.cur = self.con.cursor()
        for i, j in COORDS.items():
            self.cur.execute(f"""UPDATE {who} SET {i[0]} = '{str(self.boardMap.item(*COORDS[i]).text())}'
                         WHERE id={int(i[1:])}""")
        self.con.commit()

    def new_images(self, who):  # Создание(обновление) изображений
        self.pixmap_linkor = QPixmap(f"images/Linkor_{who}.svg")
        self.pixmap_kreyser = QPixmap(f"images/Kreyser_{who}.svg")
        self.pixmap_esminec = QPixmap(f"images/Esminec_{who}.svg")
        self.pixmap_torped = QPixmap(f"images/Torped_{who}.svg")

        self.pixmap_linkor = self.pixmap_linkor.scaled(259, 110)
        self.pixmap_kreyser = self.pixmap_kreyser.scaled(260, 110)
        self.pixmap_esminec = self.pixmap_esminec.scaled(260, 110)
        self.pixmap_torped = self.pixmap_torped.scaled(260, 110)

        self.linkorImage.setPixmap(self.pixmap_linkor)
        self.kreyserImage.setPixmap(self.pixmap_kreyser)
        self.esminecImage.setPixmap(self.pixmap_esminec)
        self.torpedImage.setPixmap(self.pixmap_torped)

    def start(self):
        """Если Игрок1 нажал кнопку,
        то Игрок2 начинает заполнять данные.
        Иначе переходит в меню игры"""
        """if self.countL != 0 or self.countK != 0 or self.countE != 0 or self.countT != 0:
            self.error("You haven't set all the ships")
            return"""
        if self.sender().text() == 'I am ready':
            self.new_db("Player1")
            players.append(Player('Player1', self.boardMap))  # Добавление в список игрока
            self.readyButton.setText("I am ready too")
            self.playerLabel.setText("PLAYER 2")
            self.new_count()  # Обновление переменных-счётчиков
            self.new_map()  # Обновление карты
            self.new_images('red')  # Обновление изображений
        else:
            self.new_db("Player2")
            players.append(Player('Player2', self.boardMap))  # Добавление в список игрока
            windows.setCurrentIndex(5)

    def new_count(self):  # Создание(обновление) переменных-счётчиков
        self.countL = 1
        self.countK = 2
        self.countE = 3
        self.countT = 4

    def coords_is_right(self, new_coords, num, mode='dual'):
        # проверка на правильность введённых координат
        new_coords[0] = new_coords[0].upper()
        new_coords[1] = new_coords[1].upper()
        if mode != 'v':
            return (COORDS[new_coords[1]][0] - COORDS[new_coords[0]][0] == 0 and
                    COORDS[new_coords[1]][1] - COORDS[new_coords[0]][1] == num) or \
                   (COORDS[new_coords[1]][0] - COORDS[new_coords[0]][0] == num and
                    COORDS[new_coords[1]][1] - COORDS[new_coords[0]][1] == 0)
        return (COORDS[new_coords[1]][0] - COORDS[new_coords[0]][0] == num and
                COORDS[new_coords[1]][1] - COORDS[new_coords[0]][1] == 0)

    def check(self, c1, c2, i, num):
        # Проверка, если в координатах есть * или X,
        # то возвращает ложь, иначе правду
        if num == 1:
            return (str(self.boardMap.item(c1 + i, c2).text()) == "*" or
                    str(self.boardMap.item(c1 + i, c2).text()) == "X")
        return (str(self.boardMap.item(c1, c2 + i).text()) == "*" or
                str(self.boardMap.item(c1, c2 + i).text()) == "X")

    def error(self, text="You entered the coordinates incorrectly."):  # Вызов ошибки
        QMessageBox.critical(self, 'ERROR!', text)

    def setShip(self, coords, num, who):  # Создание любого корабля на поле
        error = False
        new_coords = coords.split('-')
        if self.coords_is_right(new_coords, num):
            if self.coords_is_right(new_coords, num, 'v'):
                vertical = True
            else:
                vertical = False
            c1, c2 = COORDS[new_coords[0]][0], COORDS[new_coords[0]][1]
            for i in range(num + 1):
                if not vertical:
                    if self.check(c1, c2, i, 2):
                        error = True
                        self.error()
                        break
                    self.boardMap.setItem(c1, c2 + i, QTableWidgetItem("X"))
                    if i == num:
                        self.map.shoot(c1, c2 + i, "sink")
                else:
                    if self.check(c1, c2, i, 1):
                        error = True
                        self.error()
                        break
                    self.boardMap.setItem(c1 + i, c2, QTableWidgetItem("X"))
                    if i == num:
                        self.map.shoot(c1 + i, c2, 'sink')
            if not error:
                if who == "L":
                    self.countL -= 1
                elif who == "K":
                    self.countK -= 1
                elif who == "E":
                    self.countE -= 1
        else:
            self.error()

    def setLinkor(self):  # Создание Линкора
        if self.countL == 0:
            self.error("Ships ended")
            return
        coords, ok = QInputDialog.getText(self, f'{self.countL} left', 'Enter coords for Linkor:\n'
                                                                       'Example: A1-D1')
        if ok and self.countL != 0:
            try:
                self.setShip(coords, 3, "L")
            except BaseException:
                self.error()

    def setKreyser(self):  # Создание Крейсера
        if self.countK == 0:
            self.error("Ships ended")
            return
        coords, ok = QInputDialog.getText(self, f'{self.countK} left', 'Enter coords for Kreyser:\n'
                                                                       'Example: A3-C3')
        if ok and self.countK != 0:
            try:
                self.setShip(coords, 2, "K")
            except BaseException:
                self.error()

    def setEsminec(self):  # Создание Есминца
        if self.countE == 0:
            self.error("Ships ended")
            return
        coords, ok = QInputDialog.getText(self, f'{self.countE} left', 'Enter coords for Esminec:\n'
                                                                       'Example: A5-B5')
        if ok and self.countE != 0:
            try:
                self.setShip(coords, 1, "E")
            except BaseException:
                self.error()

    def setTorped(self):  # Создание торпедной лодки
        if self.countT == 0:
            self.error("Ships ended")
            return
        coord, ok = QInputDialog.getText(self, f'{self.countT} left', 'Enter coord for Torped:\n'
                                                                      'Example: A7')
        if ok and self.countT != 0:
            try:
                if str(self.boardMap.item(*COORDS[coord.upper()]).text()) == ".":
                    self.boardMap.setItem(*COORDS[coord.upper()], QTableWidgetItem("X"))
                    self.map.shoot(*COORDS[coord.upper()], 'sink')
                    self.countT -= 1
                else:
                    self.error()
            except BaseException:
                self.error()


class PVP_Main(QMainWindow, Ui_MainWindow_pvp):  # дописать!
    def __init__(self, parent=None):
        super(PVP_Main, self).__init__(parent)
        self.setupUi(self)

        self.pixmap_your_green = QPixmap("images/your_board_green.svg")
        self.pixmap_your_red = QPixmap("images/your_board_red.svg")
        self.pixmap_enemy_green = QPixmap("images/enemys_board_green.svg")
        self.pixmap_enemy_red = QPixmap("images/enemys_board_red.svg")
        self.pixmap_vs = QPixmap("images/vs.svg")

        self.turn = "Player1"  # Очередь первого игрока

        self.map1 = SeaMap(self.tableWidget)
        self.map2 = SeaMap(self.tableWidget_2)

        self.new_boards()  # Создание игрового поля

        self.initUI()

    def initUI(self):
        self.courseButton.clicked.connect(self.course)

        self.board1Label.setPixmap(self.pixmap_your_green)
        self.board2Label.setPixmap(self.pixmap_enemy_red)

        self.vsLable.setPixmap(self.pixmap_vs)
        self.courseButton.setStyleSheet("color: white; background-color: #082567;")

    def new_boards(self):
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                cell = QTableWidgetItem(".")
                cell.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, cell)
        for i in range(self.tableWidget_2.columnCount()):
            for j in range(self.tableWidget_2.rowCount()):
                cell = QTableWidgetItem(".")
                cell.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableWidget_2.setItem(i, j, cell)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.resizeRowsToContents()

    def change_of_course(self):  # Смена хода
        if self.turn == "Player1":
            self.board1Label.setPixmap(self.pixmap_enemy_green)
            self.board2Label.setPixmap(self.pixmap_your_red)
            self.turn = "Player2"
            players[0], players[1] = players[1], players[0]
        elif self.turn == "Player2":
            self.board1Label.setPixmap(self.pixmap_your_green)
            self.board2Label.setPixmap(self.pixmap_enemy_red)
            self.turn = "Player1"
            players[0], players[1] = players[1], players[0]

    def info(self, text="Your coord is right"):  # Информационное табло
        QMessageBox.information(self, "INFO", text)

    def course(self):  # Ход
        if all(players[0].board[i][j] == 0 for i in range(10) for j in range(10)):
            self.info(f"WIN {self.turn}!")
            windows.setCurrentIndex(6)
            return
        coord, ok = QInputDialog.getText(self, f'{self.turn}', 'Enter coord:\n'
                                                               'Example: A7')
        coord = coord.upper()
        try:
            if COORDS[coord]:
                self.info()
        except KeyError:
            QMessageBox.critical(self, "ERROR", "Your coord isn't right")
        else:
            c1, c2 = COORDS[coord][0], COORDS[coord][1]
            if self.dot_or_notdot(coord):
                if any(self.hasOne(COORDS[coord], shift)
                       for shift in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    self.info("HIT!")
                    if self.turn[-1] == '1':
                        self.map2.shoot(c1, c2, 'hit')
                    else:
                        self.map1.shoot(c1, c2, 'hit')
                    players[1].board[c1][c2] = 0
                    self.course()
                    return
                else:
                    self.info("SINK!")
                    if self.turn[-1] == '1':
                        self.map2.shoot(c1, c2, 'sink')
                    else:
                        self.map1.shoot(c1, c2, 'sink')
                    players[1].board[c1][c2] = 0
                    self.course()
                    return
            else:
                self.info("MISS!")
                if self.turn[-1] == '1':
                    self.map2.shoot(c1, c2, 'miss')
                else:
                    self.map1.shoot(c1, c2, 'miss')
            self.change_of_course()

    def dot_or_notdot(self, coord):  # Проверка попал, не попал
        con = sqlite3.connect("Players.db")
        cur = con.cursor()
        result = cur.execute(
            f"""SELECT {coord[0]} FROM Player{players[1].who[-1]}
            WHERE id={COORDS[coord][0] + 1}""").fetchone()
        if result[0] == "." or result[0] == "*":
            return False
        return True

    def hasOne(self, pos, shift):  # Проверка, потопил или ранил
        x, y = pos
        dx, dy = shift
        x += dx
        y += dy
        if 0 <= x < 10 and 0 <= y < 10:
            if players[1].board[x][y] == 1:
                return True
        return False


class Win_Main(QMainWindow, Ui_MainWindow_win):  # Дописать
    """Меню выиграша"""

    def __init__(self, parent=None):
        super(Win_Main, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton.setStyleSheet("color: white; background-color: #082567;"
                                      "border-radius: 20px;")
        self.label.setText(f"CONGRATULATIONS!")


class Player:
    def __init__(self, who, map):
        self.who = who
        self.board = []
        for i in range(10):
            self.board.append([])
            for j in range(10):
                self.board[i].append(0)
        for i in range(10):
            for j in range(10):
                if str(map.item(i, j).text()) == 'X':
                    self.board[i][j] = 1


class SeaMap:
    def __init__(self, board):
        self.map = board

    def shoot(self, row, col, result):
        if result == 'miss':
            self.map.setItem(row, col, QTableWidgetItem("*"))
        elif result == 'hit':
            self.map.setItem(row, col, QTableWidgetItem("X"))
        elif result == 'sink':
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        if str(self.map.item(i, j).text()) == '.':
                            self.map.setItem(i, j, QTableWidgetItem("*"))
            self.map.setItem(row, col, QTableWidgetItem("X"))
            for j in range(10):
                if str(self.map.item(row, j).text()) == 'X':
                    col = j
                    for i in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= i < 10 and 0 <= u < 10:
                                if str(self.map.item(i, u).text()) == '.':
                                    self.map.setItem(i, u, QTableWidgetItem("*"))
            for v in range(10):
                if str(self.map.item(v, col).text()) == 'X':
                    row = v
                    for v in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= v < 10 and 0 <= u < 10:
                                if str(self.map.item(v, u).text()) == '.':
                                    self.map.setItem(v, u, QTableWidgetItem('*'))


if __name__ == '__main__':  # Дописать
    app = QApplication(sys.argv)

    loading_window = Loading_Main()
    startmenu_window = Startmenu_Main()
    settings_window = Settings_Main()
    rules_window = Rules_Main()
    ready_window = Ready_Main()
    pvp_window = PVP_Main()
    win_window = Win_Main()

    windows = QStackedWidget()
    windows.addWidget(loading_window)  # 0
    windows.addWidget(startmenu_window)  # 1
    windows.addWidget(settings_window)  # 2
    windows.addWidget(rules_window)  # 3
    windows.addWidget(ready_window)  # 4
    windows.addWidget(pvp_window)  # 5
    windows.addWidget(win_window)  # 6

    windows.setWindowTitle("SEA BATTLE")
    windows.setWindowIcon(QIcon("images/icon.svg"))
    windows.resize(*SCREEN_SIZE[0])
    windows.show()
    sys.exit(app.exec())
