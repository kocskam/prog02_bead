import sys

import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from gui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QDialogButtonBox, QVBoxLayout, QDialog, QMessageBox
from Player import Player, MissingDataException
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)

class Controller:

    def __init__(self):
        self.mw = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mw)

        self.ui.b_Start.clicked.connect(self.clickStart)
        self.ui.b_Exit.clicked.connect(self.clickExit)

        # self.ui.b_Exit.clicked.connect(self.finish)

        self.list = []
        self.name = self.ui.in_Name.toPlainText()
        self.timer0 = QtCore.QTimer()
        self.time = QtCore.QTime(00, 00, 00)

        self.loadData()

        self.mw.show()

    def clickExit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Kilépés megerősítése")
        msg.setText("Biztosan ki akar lépni?")
        msg.setInformativeText("Kilépés esetén a mentés nem végezhető el.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(self.popup_button)
        msg.exec_()

    def closeEvent(self, event):
        print("test")
        reply = QMessageBox.question(self, "Bezárás", "Biztosan ki akar lépni?", "Kilépés esetén nem véhezhető el a mentés!", QMessageBox.Yes, QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def popup_button(self, i):
        # print(i.text())
        if i.text() == "OK":
            QtWidgets.QApplication.instance().quit()

    def finish(self):
        self.timer0.stop()
        tim = str(self.time.toString("hh:mm:ss"))
        # print(tim)
        # print(self.name)
        self.saveData(self.name, tim)

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('GRATULÁLUNK!')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Az Ön ideje: " + str(self.time.toString("hh:mm:ss")))
        msg.exec()

    def clickStart(self):
        self.name = self.ui.in_Name.toPlainText()

        if self.name == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("FIGYELEM!")
            msg.setText("Adjon meg egy nevet a játék indulásához!")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec()
        else:
            self.ui.b_Start.setEnabled(False)
            self.curr_time = QtCore.QTime(00, 00, 00)

            self.timer0.setInterval(1000)
            self.timer0.timeout.connect(self.calc)
            self.timer0.start()
            self.ui.lcdNumber.display(str(self.calc()))


    def calc(self):
        global time
        self.time = self.time.addSecs(1)
        self.ui.lcdNumber.display(self.time.toString("hh:mm:ss"))

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

                self.ui.ls_Players.append(str("NÉV: " + ls[0] + '\n' + "IDŐ: " + ls[1]))
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

    #main
    # t_maze = getMaze()
    # print(t_maze[0][0])

#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec())
