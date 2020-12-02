import sys
from labirintus import getMaze
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from gui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QDialogButtonBox, QVBoxLayout, QDialog, QMessageBox
from Player import Player, MissingDataException
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtCore import (
    Qt,
    QBasicTimer, QLineF
)
from PyQt5.QtGui import (
    QBrush,
    QPixmap
)
from PyQt5.QtWidgets import (QWidget,
    QGraphicsLineItem,
    QApplication,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView,QMessageBox,QPushButton
    )

from PyQt5.QtWidgets import *

class Walls(QtWidgets.QLabel):
    walls = []
    def __init__(self, parent=None):
        super().__init__( parent)
        self.setPixmap(QtGui.QPixmap('lab_fal.png'))

class Finish(QtWidgets.QLabel):
    finish = []
    def __init__(self, parent=None):
        super().__init__( parent)
        self.setPixmap(QtGui.QPixmap('lab_cel.png'))

class Path(QtWidgets.QLabel):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QtGui.QPixmap('lab_ut.png'))


class Babu(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__( parent)
        self.setPixmap(QtGui.QPixmap('lab_babu.png'))



    def keyPressEvent(self, event):
        try:

            if (self.x(), self.y()) in Finish.finish:
                self.setPixmap(QtGui.QPixmap('lab_nyert.png'))
                msg = QMessageBox()
                msg.setText('Vege')
                msg.exec()
                sys.exit()


            if event.key() == Qt.Key_Right:
                if self.x() <808:
                    move_to_x = self.x()+32
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.move(move_to_x, move_to_y)
            if event.key() == Qt.Key_Left:
                if self.x() >200:
                    move_to_x = self.x()-32
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.move(move_to_x, move_to_y)
            if event.key() == Qt.Key_Up:
                if self.y()>200:
                    move_to_x = self.x()
                    move_to_y = self.y() -32
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.move(move_to_x, move_to_y)
            if event.key() == Qt.Key_Down:
                if self.y() <808:
                    move_to_x = self.x()
                    move_to_y = self.y() +32
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.move(move_to_x, move_to_y)
            else:
                QtWidgets.QLabel.keyPressEvent(self, event)

        except Exception as e:
            print(e)

# class Gomb(QtWidgets.QPushButton):
#     def __init__(self, parent=None):
#         super().__init__('Start',parent)
#
#     def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
#         try:
#             if e:
#                 MainWindow.createGame(MainWindow)
#                 self.show()
#         except Exception as e:
#             print(e)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setGeometry(0, 0, 1243, 702)
        self.setFixedSize(1243, 900)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.b_Start = QPushButton(self.centralWidget)
        self.b_Start.setText('Játék inditása')
        self.b_Start.setGeometry(10, 600, 91, 41)
        self.b_Start.clicked.connect(self.clickStart)
        self.b_Exit = QPushButton(self.centralWidget)
        self.b_Exit.setText('Kilépés')
        self.b_Exit.setGeometry(10, 540, 91, 41)
        self.b_Exit.clicked.connect(self.clickExit)
        self.label = QLabel(self.centralWidget)
        self.label.setText("Add meg a neved!")
        self.label.setGeometry(10, 0, 121, 41)
        self.in_Name = QTextEdit(self.centralWidget)
        self.in_Name.setGeometry(10, 40, 91, 31)
        self.lcdNumber = QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(10, 490, 64, 23)
        self.timer0 = QtCore.QTimer()
        self.label2 = QLabel(self.centralWidget)
        self.label2.setText('Eddigi eredmények')
        self.label2.setGeometry(10, 100, 121, 41)
        self.ls_Players = QTextBrowser(self.centralWidget)
        self.ls_Players.setGeometry(10, 160, 141, 301)
        self.timer0 = QtCore.QTimer()
        self.time = QtCore.QTime(00, 00, 00)

        self.list = []
        self.loadData()

        self.createGame()
        self.show()








    def createGame(self):
        maze = getMaze()
        for i in range(len(maze)):
            for j in range(len(maze)):
                if maze[i][j] =='0':

                    self.wall = Walls(self.centralWidget)
                    self.wall.setGeometry(200+i*32, 200+j*32, 32, 32)
                    Walls.walls.append((self.wall.x(), self.wall.y()))
                if maze[i][j] == '1' :
                    self.path = Path(self.centralWidget)
                    self.path.setGeometry(200+i*32, 200+j*32, 32, 32)
                if maze[i][j] == '2':
                    self.finish = Finish(self.centralWidget)
                    self.finish.setGeometry(200+i*32, 200+j*32, 32, 32)
                    Finish.finish.append((self.finish.x(),self.finish.y()))
                if maze[i][j] == '3':
                    x = 200+i*32
                    y = 200+j*32
                    self.path = Path(self.centralWidget)
                    self.path.setGeometry(x, y, 32, 32)
        self.babu = Babu(self.centralWidget)
        self.babu.setGeometry(x, y, 32, 32)


    def closeEvent(self, event):
        print("test")
        reply = QMessageBox.question(self, "Bezárás", "Biztosan ki akar lépni?", "Kilépés esetén nem véhezhető el a mentés!", QMessageBox.Yes, QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def clickExit(self):
        try:
            msg = QMessageBox()
            msg.setWindowTitle("Kilépés megerősítése")
            msg.setText("Biztosan ki akar lépni?")
            msg.setInformativeText("Kilépés esetén a mentés nem végezhető el.")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.buttonClicked.connect(self.popup_button)
            msg.exec()
        except Exception as e:
            print(e)

    def popup_button(self, i):
        # print(i.text())
        if i.text() == "OK":
            QtWidgets.QApplication.instance().quit()


    def clickStart(self):
        try:
            self.name = self.in_Name.toPlainText()

            if self.name == "":
                msg = QMessageBox()
                msg.setWindowTitle("FIGYELEM!")
                msg.setText("Adjon meg egy nevet a játék indulásához!")
                msg.setIcon(QMessageBox.Information)
                msg.exec()
            else:
                self.babu.setFocus()
                self.b_Start.setEnabled(False)
                self.curr_time = QtCore.QTime(00, 00, 00)

                self.timer0.setInterval(1000)
                self.timer0.timeout.connect(self.calc)
                self.timer0.start()
                self.lcdNumber.display(str(self.calc()))
        except Exception as e:
            print(e)

    def calc(self):
        global time
        self.time = self.time.addSecs(1)
        self.lcdNumber.display(self.time.toString("hh:mm:ss"))

    def loadData(self):
        first = True
        fin = open("database.txt", "r")
        for r in fin:
            if r != "\n":
                ls = r.split(";")
                nw = Player(ls[0], ls[1])
                self.list.append(nw)

                try:
                    # int(ls[1])
                    #ellenőrizni, hogy idő-e azaz int
                    pass
                except Exception:
                    if first:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("FIGYELEM!")
                        msg.setText("Hiba a beolvasás során!")
                        msg.setIcon(QtWidgets.QMessageBox.Information)
                        msg.exec()
                    first = False
                    continue

                self.ls_Players.append(str("NÉV: " + ls[0] + '\n' + "IDŐ: " + ls[1]))
            else:
                continue

        fin.close()

    def saveData(self, name, time):
        try:
            if name == "":
                raise MissingDataException("név")
            if time == "":
                raise MissingDataException("időtartam")

            # print(type(time))
            # print(isinstance(time, ))

            newPlayer = Player(name, time)
            self.list.append(newPlayer)
            print(self.list)
            fout = open("database.txt", "w")
            for w in self.list:
                w.save2File(fout)
            fout.close()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setText('Hiba történt:\n' + e.__str__())
            msg.exec()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainWindow()
    sys.exit(app.exec())