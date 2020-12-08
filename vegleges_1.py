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
                # QtWidgets.QMainWindow.finish(self)
                view.endGame()


            if event.key() == Qt.Key_Right:
                if self.x() <908:
                    move_to_x = self.x()+32
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.move(move_to_x, move_to_y)
            if event.key() == Qt.Key_Left:
                if self.x() >300:
                    move_to_x = self.x()-32
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.move(move_to_x, move_to_y)
            if event.key() == Qt.Key_Up:
                if self.y()>50:
                    move_to_x = self.x()
                    move_to_y = self.y() -32
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.move(move_to_x, move_to_y)
            if event.key() == Qt.Key_Down:
                if self.y() <658:
                    move_to_x = self.x()
                    move_to_y = self.y() +32
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.move(move_to_x, move_to_y)
            #else:
                #QtWidgets.QLabel.keyPressEvent(self, event)

        except Exception as e:
            print(e)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setGeometry(0, 0, 1000, 750)
        self.setFixedSize(1000, 750)
        self.setStyleSheet("background-color: rgb(0, 147, 0)")
        self.setWindowTitle("Labirintus")
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.flag = False
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPixelSize(18)
        font.setBold(True)
        font_name = QtGui.QFont()
        font_name.setFamily("Comic Sans MS")
        font_name.setPixelSize(18)
        font_data = QtGui.QFont()
        font_data.setFamily("Comic Sans MS")
        font_data.setPixelSize(14)
        font_b = QtGui.QFont()
        font_b.setFamily("Comic Sans MS")
        font_b.setPixelSize(16)
        self.label = QLabel(self.centralWidget)
        self.label.setText("Add meg a neved!")
        self.label.setGeometry(50, 120, 200, 50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.in_Name = QTextEdit(self.centralWidget)
        self.in_Name.setGeometry(50, 160, 200, 35)
        self.in_Name.setStyleSheet("background-color: rgb(70, 170, 204)")
        self.in_Name.setFont(font_name)
        self.in_Name.setAlignment(Qt.AlignCenter)
        self.b_Start = QPushButton(self.centralWidget)
        self.b_Start.setText('Játék inditása')
        self.b_Start.setGeometry(50, 200, 200, 40)
        self.b_Start.clicked.connect(self.clickStart)
        self.b_Start.setStyleSheet("background-color: rgb(0, 200, 0)")
        self.b_Start.setFont(font_b)
        self.label3 = QLabel(self.centralWidget)
        self.label3.setText("Levélről levélre szállva juss el a virághoz!")
        self.label3.setGeometry(50, 40, 200, 70)
        self.label3.setFont(font)
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setWordWrap(True)
        self.label3.setStyleSheet("color: rgb(255, 255, 0)")
        self.lcdNumber = QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(110, 280, 70, 30)
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 200, 0)")
        self.timer0 = QtCore.QTimer()
        self.timer0 = QtCore.QTimer()
        self.time = QtCore.QTime(00, 00, 00)
        self.label2 = QLabel(self.centralWidget)
        self.label2.setText('Eddigi eredmények')
        self.label2.setGeometry(50, 320, 200, 30)
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)
        self.ls_Players = QTextBrowser(self.centralWidget)
        self.ls_Players.setGeometry(50, 350, 200, 270)
        self.ls_Players.setStyleSheet("background-color: rgb(70, 170, 204)")
        self.ls_Players.setFont(font_data)
        self.b_Exit = QPushButton(self.centralWidget)
        self.b_Exit.setText('Kilépés')
        self.b_Exit.setGeometry(50, 650, 200, 40)
        self.b_Exit.clicked.connect(self.clickExit)
        self.b_Exit.setStyleSheet("background-color: rgb(0, 200, 0)")
        self.b_Exit.setFont(font_b)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

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
                    self.wall.setGeometry(300+i*32, 50+j*32, 32, 32)
                    Walls.walls.append((self.wall.x(), self.wall.y()))
                if maze[i][j] == '1' :
                    self.path = Path(self.centralWidget)
                    self.path.setGeometry(300+i*32, 50+j*32, 32, 32)
                if maze[i][j] == '2':
                    z = 300+i*32
                    w = 50+i*32
                    self.finish = Finish(self.centralWidget)
                    self.finish.setGeometry(300+i*32, 50+j*32, 32, 32)
                    Finish.finish.append((self.finish.x(),self.finish.y()))
                if maze[i][j] == '3':
                    x = 300+i*32
                    y = 50+j*32
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
            if self.flag == False:
                self.babu.setFocus()
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
                self.in_Name.setEnabled(False)
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
        try:
            fin = open("database.txt", "r")
        except Exception:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("FIGYELEM!")
            msg.setText("Hiba a beolvasás során! A fájl nem található!")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec()

        for r in fin:
            if r != "\n":
                try:
                    ls = r.split(";")
                    nw = Player(ls[0], ls[1])
                    self.list.append(nw)
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

    def endGame(self):
        self.timer0.stop()
        tim = str(self.time.toString("hh:mm:ss"))
        self.saveData(self.name, tim)

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('GRATULÁLUNK!')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Az Ön ideje: " + str(self.time.toString("hh:mm:ss")))
        msg.exec()
        self.flag = True
        self.ls_Players.append(str("NÉV: " + self.name + '\n' + "IDŐ: " + tim))
        self.babu.clearFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainWindow()
    sys.exit(app.exec())
