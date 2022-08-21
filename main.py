from UI.settings import Ui_MainWindow_settings
from UI.loading import Ui_MainWindow_loading
from UI.startmenu import Ui_MainWindow_startmenu
from UI.rules import Ui_MainWindow_rules
from UI.readygame import Ui_MainWindow_ready
from UI.gamepvp import Ui_MainWindow_pvp
from UI.win import Ui_MainWindow_win

import sys
from random import randrange
import sqlite3

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QBasicTimer, QCoreApplication

from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QStackedWidget, QMessageBox, QInputDialog, QTableWidgetItem, QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QSound

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
NOTES = {
    'warning': QSound("sounds/warning.wav"),
    'background': QSound("sounds/background.wav"),
    'hit': QSound("sounds/hit.wav"),
    'miss': QSound("sounds/miss.wav"),
    'main_sound': QSound("sounds/main_sound.wav"),
    'win': QSound("sounds/win.wav")
}


def new_cell_mul():  # Когда ставлю звёздочку в QTableWidget
    cell_mul = QTableWidgetItem("*")
    cell_mul.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    return cell_mul


def new_cell_x():  # Когда ставлю крестик в QTableWidget
    cell_x = QTableWidgetItem("X")
    cell_x.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    return cell_x


def new_cell_dot():  # Когда ставлю точку в QTableWidget
    cell_dot = QTableWidgetItem(".")
    cell_dot.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    return cell_dot


class LoadingMain(QMainWindow, Ui_MainWindow_loading):
    """Псевдозагрузочная анимация"""

    def __init__(self, parent=None):
        super(LoadingMain, self).__init__(parent)
        self.setupUi(self)
        self.mediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.timer = QBasicTimer()
        self.step = 0
        self.initUI()

    def initUI(self):
        self.load_mp4("videos/animation.gif")
        self.pushButton.clicked.connect(self.do_action)
        # При наведении на кнопку курсор поменяется
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def load_mp4(self, filename):  # Загружаю ГИФ-файл
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QMediaContent(media)
        self.mediaplayer.setMedia(content)
        self.mediaplayer.play()
        self.mediaplayer.setVideoOutput(self.widget)

    def load_mp3(self, filename):  # Загружаю звук
        NOTES[filename].play()

    def timerEvent(self, e):  # Загрузка
        if self.step >= 100:
            self.timer.stop()
            self.pushButton.setText('Finished')
            self.load_mp3("main_sound")
            windows.setCurrentIndex(1)
            return

        self.step = self.step + randrange(0, 10)
        self.progressBar.setValue(self.step)

    def do_action(self):  # Если пользователь нажимает кнопку
        if self.timer.isActive():
            self.timer.stop()
            self.pushButton.setText('BEST PRODUCTIONS')
            # При наведении на кнопку курсор поменяется
            self.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        else:
            self.timer.start(100, self)
            self.pushButton.setText('Stop')
            # При наведении на кнопку курсор поменяется
            self.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))


class StartMenuMain(QMainWindow, Ui_MainWindow_startmenu):
    """Стартовое меню, где можно переключаться между окнами, а также выйти из игры"""

    def __init__(self, parent=None):
        super(StartMenuMain, self).__init__(parent)
        self.setupUi(self)

        self.LOGOBP = QPixmap("images/logobp.svg")  # Картинка логотипа "кампании"
        self.LOGOSB = QPixmap("images/logosb.svg")  # Картинка логотипа игры
        self.mediaplayer1 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.SOUND = True  # по умолчанию звук включён

        self.initUI()

    def initUI(self):
        self.logoImage1.setPixmap(self.LOGOBP)
        self.label.setPixmap(self.LOGOSB)

        self.load_mp4("videos/animation800.gif")  # Загружаю гифку
        self.load_mp3("background")  # Загружаю звук

        # Добавляю тулбар, возможность включать/выключать звук
        self.soundAction = QAction(QIcon('images/microphone.svg'),
                                   'Turn on / Turn off', self)
        self.soundAction.setShortcut('Ctrl+M')
        self.soundAction.triggered.connect(self.to_sound)

        self.toolbar = self.addToolBar('Sound')
        self.toolbar.addAction(self.soundAction)

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

        # Подсказки, при наведении курсора на кнопки/изображения
        self.logoImage1.setToolTip("<b>Best Productions</b>")
        self.label.setToolTip("<b>SEA BATTLE</b>/ BATTLESHIP")
        self.videoStartMenu_1.setToolTip("Animation")
        self.startButton.setToolTip("<b>Start</b> the game")
        self.rulesButton.setToolTip("Read the <b>rules</b>")
        self.settingsButton.setToolTip("Change <b>Settings</b>")
        self.exitButton.setToolTip("<b>Exit</b> to Windows/Linux/MacOS")

        # При наведении на кнопки, курсор меняется
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rulesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def to_sound(self):  # Включение/отключение звука
        if self.SOUND:
            self.soundAction.setIcon(QIcon("images/muted.svg"))
            self.SOUND = False
            self.load_mp3('background')
        else:
            self.soundAction.setIcon(QIcon("images/microphone.svg"))
            self.SOUND = True
            self.load_mp3('background')

    def load_mp3(self, filename, param=False):  # Загрузка WAV-файла
        if not self.SOUND or param:
            NOTES[filename].stop()
        elif self.SOUND:
            NOTES[filename].play()

    def load_mp4(self, filename):  # Загрузка GIF-файла
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QMediaContent(media)

        self.mediaplayer1.setMedia(content)
        self.mediaplayer1.play()
        self.mediaplayer1.setVideoOutput(self.videoStartMenu_1)

    def to_settings(self):  # Переходит в меню настроек
        self.load_mp3("main_sound")
        windows.setCurrentIndex(2)

    def to_rules(self):  # Переходит в меню правил
        self.load_mp3("main_sound")
        windows.setCurrentIndex(3)

    def to_start(self):  # Переходит в меню начала игры
        self.load_mp3("main_sound")
        self.load_mp3("background", param=True)
        windows.setCurrentIndex(4)


class SettingsMain(QMainWindow, Ui_MainWindow_settings):
    """Меню настроек, где можно изменить режим игры, а также сменить язык"""

    def __init__(self, parent=None):
        super(SettingsMain, self).__init__(parent)
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

        # self.radiopve.toggled.connect(self.changeP)
        self.radiopvp.toggled.connect(self.changeP)
        self.backButton.clicked.connect(self.to_start)
        self.saveButton.clicked.connect(self.to_save)

        self.radiopvp.setToolTip("Change <b>mode</b>")
        self.comboBox.setToolTip("Change <b>language</b>")
        self.saveButton.setToolTip("<b>Save</b> settings")
        self.logoImage.setToolTip("<b>SEA BATTLE</b>/ BATTLESHIP")
        self.backButton.setToolTip("<b>Back</b> to startmenu")

        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def load_mp3(self, filename, param=False):  # Загрузка WAV-файла
        if not self.SOUND or param:
            NOTES[filename].stop()
        elif self.SOUND:
            NOTES[filename].play()

    def to_start(self):  # Переход в стартовое меню
        self.SOUND = startmenu_window.SOUND
        self.load_mp3('main_sound')
        windows.setCurrentIndex(1)

    def to_save(self):  # Сохраняет изменения
        QMessageBox.information(self, "THAT'S OK", "SETTINGS SAVED")

    def changeP(self):  # Меняет режим игры
        self.radiopvp.setChecked(True)
        QMessageBox.critical(self, "ERROR", "YOU CANNOT DISABLE THE ONLY MODE")

    def changeL(self):  # Меняет язык
        pass


class RulesMain(QMainWindow, Ui_MainWindow_rules):
    """Меню правил"""

    def __init__(self, parent=None):
        super(RulesMain, self).__init__(parent)
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

        self.backButton.setToolTip("<b>Back</b> to startmenu")
        self.logoImage.setToolTip("<b>SEA BATTLE</b>/ BATTLESHIP")
        self.label.setToolTip("<b>rules</b>")

        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def load_mp3(self, filename, param=False):
        if not self.SOUND or param:
            NOTES[filename].stop()
        elif self.SOUND:
            NOTES[filename].play()

    def to_start(self):  # Переход в стартовое меню
        self.SOUND = startmenu_window.SOUND
        self.load_mp3("main_sound")
        windows.setCurrentIndex(1)


class ReadyMain(QMainWindow, Ui_MainWindow_ready):
    """Меню подготовления к самой игре"""

    def __init__(self, parent=None):
        super(ReadyMain, self).__init__(parent)
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

        self.linkorButton.clicked.connect(self.set_linkor)
        self.kreyserButton.clicked.connect(self.set_kreyser)
        self.esminecButton.clicked.connect(self.set_esminec)
        self.torpedButton.clicked.connect(self.set_torped)

        # При наведении меняется курсор
        self.linkorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kreyserButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.esminecButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.torpedButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Подсказки
        self.linkorImage.setToolTip("<b>Battleship</b>")
        self.kreyserImage.setToolTip("<b>Cruiser</b>")
        self.esminecImage.setToolTip("<b>Destroyer</b>")
        self.torpedImage.setToolTip("<b>Torpedo boat</b>")
        self.readyButton.setToolTip("The choice of the <b>other player</b>/<b>Start</b> the game.")
        self.boardMap.setToolTip("This is your board")

    def load_mp3(self, filename, param=False):
        if not self.SOUND or param:
            NOTES[filename].stop()
        elif self.SOUND:
            NOTES[filename].play()

    def new_map(self):  # Метод создаёт(обновляет) карту
        for i in range(self.boardMap.columnCount()):
            for j in range(self.boardMap.rowCount()):
                self.boardMap.setItem(i, j, new_cell_dot())
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
        Иначе начинает игру"""
        # Проверка, все ли корабли поставлены
        if self.countL != 0 or self.countK != 0 or self.countE != 0 or self.countT != 0:
            self.error("You haven't set all the ships")
            return
        if self.sender().text() == 'I am ready':
            self.new_db("Player1")
            players.append(Player('Player1', self.boardMap))  # Добавление в список игрока
            self.readyButton.setText("I am ready too")
            self.playerLabel.setText("PLAYER 2")
            self.new_count()  # Обновление переменных-счётчиков
            self.new_map()  # Обновление карты
            self.new_images('red')  # Обновление изображений
            self.SOUND = startmenu_window.SOUND
            self.load_mp3("main_sound")
        else:
            self.new_db("Player2")
            players.append(Player('Player2', self.boardMap))  # Добавление в список игрока
            self.SOUND = startmenu_window.SOUND
            self.load_mp3("main_sound")
            windows.setCurrentIndex(5)

    def new_count(self):  # Создание(обновление) переменных-счётчиков
        self.countL = 1
        self.countK = 2
        self.countE = 3
        self.countT = 4
        self.linkorButton.setToolTip(f"{self.countL} left")
        self.kreyserButton.setToolTip(f"{self.countK} left")
        self.esminecButton.setToolTip(f"{self.countE} left")
        self.torpedButton.setToolTip(f"{self.countT} left")

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

    def set_ship(self, coords, num, who):  # Создание любого корабля на поле
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
                    self.boardMap.setItem(c1, c2 + i, new_cell_x())
                    if i == num:
                        self.map.shoot(c1, c2 + i, "sink")
                else:
                    if self.check(c1, c2, i, 1):
                        error = True
                        self.error()
                        break
                    self.boardMap.setItem(c1 + i, c2, new_cell_x())
                    if i == num:
                        self.map.shoot(c1 + i, c2, 'sink')
            if not error:
                if who == "L":
                    self.countL -= 1
                    self.linkorButton.setToolTip(f"{self.countL} left")
                elif who == "K":
                    self.countK -= 1
                    self.kreyserButton.setToolTip(f"{self.countK} left")
                elif who == "E":
                    self.countE -= 1
                    self.esminecButton.setToolTip(f"{self.countE} left")
        else:
            self.error()
        self.is_null()

    def is_null(self):
        if self.countL == 0:
            self.pixmap_linkor = QPixmap(f"images/Linkor_white.svg")
            self.pixmap_linkor = self.pixmap_linkor.scaled(259, 110)
            self.linkorImage.setPixmap(self.pixmap_linkor)
        if self.countK == 0:
            self.pixmap_kreyser = QPixmap(f"images/Kreyser_white.svg")
            self.pixmap_kreyser = self.pixmap_kreyser.scaled(259, 110)
            self.kreyserImage.setPixmap(self.pixmap_kreyser)
        if self.countE == 0:
            self.pixmap_esminec = QPixmap(f"images/Esminec_white.svg")
            self.pixmap_esminec = self.pixmap_esminec.scaled(259, 110)
            self.esminecImage.setPixmap(self.pixmap_esminec)
        if self.countT == 0:
            self.pixmap_torped = QPixmap(f"images/Torped_white.svg")
            self.pixmap_torped = self.pixmap_torped.scaled(259, 110)
            self.torpedImage.setPixmap(self.pixmap_torped)

    def set_linkor(self):  # Создание Линкора
        if self.countL == 0:
            self.error("Ships ended")
            return
        coords, ok = QInputDialog.getText(self, f'{self.countL} left', 'Enter coords for Linkor:\n'
                                                                       'Example: A1-D1')
        if ok and self.countL != 0:
            try:
                self.set_ship(coords, 3, "L")
            except BaseException:
                self.error()

    def set_kreyser(self):  # Создание Крейсера
        if self.countK == 0:
            self.error("Ships ended")
            return
        coords, ok = QInputDialog.getText(self, f'{self.countK} left', 'Enter coords for Kreyser:\n'
                                                                       'Example: A3-C3')
        if ok and self.countK != 0:
            try:
                self.set_ship(coords, 2, "K")
            except BaseException:
                self.error()

    def set_esminec(self):  # Создание Эсминца
        if self.countE == 0:
            self.error("Ships ended")
            return
        coords, ok = QInputDialog.getText(self, f'{self.countE} left', 'Enter coords for Esminec:\n'
                                                                       'Example: A5-B5')
        if ok and self.countE != 0:
            try:
                self.set_ship(coords, 1, "E")
            except BaseException:
                self.error()

    def set_torped(self):  # Создание торпедной лодки
        if self.countT == 0:
            self.error("Ships ended")
            return
        coord, ok = QInputDialog.getText(self, f'{self.countT} left', 'Enter coord for Torped:\n'
                                                                      'Example: A7')
        if ok and self.countT != 0:
            try:
                if str(self.boardMap.item(*COORDS[coord.upper()]).text()) == ".":
                    self.boardMap.setItem(*COORDS[coord.upper()], new_cell_x())
                    self.map.shoot(*COORDS[coord.upper()], 'sink')
                    self.countT -= 1
                    self.torpedButton.setToolTip(f"{self.countT} left")
                else:
                    self.error()
                self.is_null()
            except BaseException:
                self.error()


class PVPMain(QMainWindow, Ui_MainWindow_pvp):
    def __init__(self, parent=None):
        super(PVPMain, self).__init__(parent)
        self.setupUi(self)

        self.pixmap_your_green = QPixmap("images/your_board_green.svg")
        self.pixmap_your_red = QPixmap("images/your_board_red.svg")
        self.pixmap_enemy_green = QPixmap("images/enemys_board_green.svg")
        self.pixmap_enemy_red = QPixmap("images/enemys_board_red.svg")
        self.pixmap_vs = QPixmap("images/vs.svg")
        self.pixmap_linkor_red = QPixmap(f"images/Linkor_red.svg")
        self.pixmap_kreyser_red = QPixmap(f"images/Kreyser_red.svg")
        self.pixmap_esminec_red = QPixmap(f"images/Esminec_red.svg")
        self.pixmap_torped_red = QPixmap(f"images/Torped_red.svg")
        self.pixmap_linkor_green = QPixmap(f"images/Linkor_green.svg")
        self.pixmap_kreyser_green = QPixmap(f"images/Kreyser_green.svg")
        self.pixmap_esminec_green = QPixmap(f"images/Esminec_green.svg")
        self.pixmap_torped_green = QPixmap(f"images/Torped_green.svg")
        self.pixmap_linkor_green = self.pixmap_linkor_green.scaled(60, 30)
        self.pixmap_kreyser_green = self.pixmap_kreyser_green.scaled(60, 30)
        self.pixmap_esminec_green = self.pixmap_esminec_green.scaled(60, 30)
        self.pixmap_torped_green = self.pixmap_torped_green.scaled(60, 30)
        self.pixmap_linkor_red = self.pixmap_linkor_red.scaled(60, 30)
        self.pixmap_kreyser_red = self.pixmap_kreyser_red.scaled(60, 30)
        self.pixmap_esminec_red = self.pixmap_esminec_red.scaled(60, 30)
        self.pixmap_torped_red = self.pixmap_torped_red.scaled(60, 30)

        self.turn = "Player1"  # Очередь первого игрока
        # Подсказки
        self.tableWidget.setToolTip("Your board")
        self.tableWidget_2.setToolTip("Not your board")

        self.map1 = SeaMap(self.tableWidget)
        self.map2 = SeaMap(self.tableWidget_2)

        self.new_boards()  # Создание игрового поля

        self.initUI()

    def initUI(self):
        self.tableWidget.cellClicked[int, int].connect(self.course1)
        self.tableWidget_2.cellClicked[int, int].connect(self.course2)

        self.board1Label.setPixmap(self.pixmap_your_green)
        self.board2Label.setPixmap(self.pixmap_enemy_red)

        self.vsLable.setPixmap(self.pixmap_vs)

        self.linkorP1.setPixmap(self.pixmap_linkor_green)
        self.kreyserP1.setPixmap(self.pixmap_kreyser_green)
        self.esminecP1.setPixmap(self.pixmap_esminec_green)
        self.torpedP1.setPixmap(self.pixmap_torped_green)
        self.linkorP2.setPixmap(self.pixmap_linkor_red)
        self.kreyserP2.setPixmap(self.pixmap_kreyser_red)
        self.esminecP2.setPixmap(self.pixmap_esminec_red)
        self.torpedP2.setPixmap(self.pixmap_torped_red)

    def load_mp3(self, filename, param=False):
        if not self.SOUND or param:
            NOTES[filename].stop()
        elif self.SOUND:
            NOTES[filename].play()

    def new_boards(self):
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                self.tableWidget.setItem(i, j, new_cell_dot())
        for i in range(self.tableWidget_2.columnCount()):
            for j in range(self.tableWidget_2.rowCount()):
                self.tableWidget_2.setItem(i, j, new_cell_dot())
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
            self.tableWidget.setToolTip("Not your board")
            self.tableWidget_2.setToolTip("Your board")
        elif self.turn == "Player2":
            self.board1Label.setPixmap(self.pixmap_your_green)
            self.board2Label.setPixmap(self.pixmap_enemy_red)
            self.turn = "Player1"
            players[0], players[1] = players[1], players[0]
            self.tableWidget.setToolTip("Your board")
            self.tableWidget_2.setToolTip("Not your board")

    def info(self, text="Your coord is right"):  # Информационное табло
        QMessageBox.information(self, "INFO", text)

    def check(self):
        if all(players[1].board[i][j] == 0 for i in range(10) for j in range(10)):
            self.info(f"WIN {self.turn}!")
            self.SOUND = startmenu_window.SOUND
            self.load_mp3("win")
            windows.setCurrentIndex(6)
            return

    def course1(self, c1, c2):
        self.course(c1, c2, 1)

    def course2(self, c1, c2):
        self.course(c1, c2, 2)

    def course(self, r, c, num):  # Ход
        if self.turn[-1] == '1' and num == 2 or self.turn[-1] == '2' and num == 1:
            flag = True
            coord = (r, c)
        else:
            flag = False
        if flag:
            if self.is_dot((r, c)):
                if any(self.has_one((r, c), shift)
                       for shift in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    self.info("HIT!")
                    if self.turn[-1] == '1':
                        self.map2.shoot(r, c, 'hit')
                    else:
                        self.map1.shoot(r, c, 'hit')
                    players[1].board[r][c] = 0
                    self.SOUND = startmenu_window.SOUND
                    self.load_mp3("hit")
                else:
                    self.info("SINK!")
                    if self.turn[-1] == '1':
                        self.map2.shoot(r, c, 'sink')
                    else:
                        self.map1.shoot(r, c, 'sink')
                    players[1].board[r][c] = 0
                    self.SOUND = startmenu_window.SOUND
                    self.load_mp3("warning")
                    self.check()
            else:
                self.info("MISS!")
                if self.turn[-1] == '1':
                    self.map2.shoot(r, c, 'miss')
                else:
                    self.map1.shoot(r, c, 'miss')
                self.SOUND = startmenu_window.SOUND
                self.load_mp3("miss")
                self.change_of_course()
        else:
            QMessageBox.critical(self, "ERROR", "NOT YOUR TURN!")

    def is_dot(self, coord):  # Проверка попал, не попал
        new_coord = None
        for key, value in COORDS.items():
            if value == coord:
                new_coord = (key, value)
                break
        con = sqlite3.connect("Players.db")
        cur = con.cursor()
        result = cur.execute(
            f"""SELECT {new_coord[0][0]} FROM Player{players[1].who[-1]}
            WHERE id={new_coord[1][0] + 1}""").fetchone()
        return not (result[0] == "." or result[0] == "*")

    def has_one(self, pos, shift):  # Проверка, потопил или ранил
        x, y = pos
        dx, dy = shift
        x += dx
        y += dy
        if 0 <= x < 10 and 0 <= y < 10:
            if players[1].board[x][y] == 1:
                return True
        return False


class WinMain(QMainWindow, Ui_MainWindow_win):  # Дописать
    """Меню выиграша"""

    def __init__(self, parent=None):
        super(WinMain, self).__init__(parent)
        self.setupUi(self)
        self.LOGOSB = QPixmap("images/logosb.svg")
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton.setStyleSheet("color: white; background-color: #082567;"
                                      "border-radius: 20px;")
        self.label_2.setPixmap(self.LOGOSB)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


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
            self.map.setItem(row, col, new_cell_mul())
        elif result == 'hit':
            self.map.setItem(row, col, new_cell_x())
        elif result == 'sink':
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        if str(self.map.item(i, j).text()) == '.':
                            self.map.setItem(i, j, new_cell_mul())
            self.map.setItem(row, col, new_cell_x())
            for j in range(10):
                if str(self.map.item(row, j).text()) == 'X':
                    col = j
                    for i in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= i < 10 and 0 <= u < 10:
                                if str(self.map.item(i, u).text()) == '.':
                                    self.map.setItem(i, u, new_cell_mul())
            for v in range(10):
                if str(self.map.item(v, col).text()) == 'X':
                    row = v
                    for v in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= v < 10 and 0 <= u < 10:
                                if str(self.map.item(v, u).text()) == '.':
                                    self.map.setItem(v, u, new_cell_mul())


if __name__ == '__main__':  # Дописать
    app = QApplication(sys.argv)

    loading_window = LoadingMain()
    startmenu_window = StartMenuMain()
    settings_window = SettingsMain()
    rules_window = RulesMain()
    ready_window = ReadyMain()
    pvp_window = PVPMain()
    win_window = WinMain()

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
