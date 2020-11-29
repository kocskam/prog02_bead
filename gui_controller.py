import sys

from labirintus import getMaze
from PyQt5 import QtWidgets, QtCore, QtGui
from gui import Ui_MainWindow
from labWin import Ui_Dialog
from PySide2.QtWidgets import QMainWindow, QDialogButtonBox, QVBoxLayout, QDialog, QMessageBox
from Player import Player, MissingDataException

class Controller:

    def __init__(self):
        self.mw = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mw)

        self.ui.b_Start.clicked.connect(self.clickStart)
        self.ui.b_Exit.clicked.connect(self.clickExit)
        # self.ui.b_Result.clicked.connect(self.saveResults())

        self.list = []
        self.name = self.ui.in_Name.toPlainText()
        # self.loadData()
        # self.save3File("kecsa", "dsadas")
        # self.saveData()

        self.mw.show()



    def clickExit(self):
        print("Na")
        msg = QMessageBox()
        msg.setWindowTitle("Kilépés megerősítése")
        msg.setText("Biztosan ki akar lépni?")
        msg.setInformativeText("Kilépés esetén a mentés nem végezhető el.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)

        msg.buttonClicked.connect(self.popup_button)
        msg.exec_()

    def popup_button(self, i):
        print(i.text())
        if i.text() == "OK":
            QtWidgets.QApplication.instance().quit()

    def clickStart(self):
        # print("VÉGE")
        # msg = QtWidgets.QMessageBox()
        # msg.setWindowTitle('GRATULÁLUNK!')
        # msg.setIcon(QtWidgets.QMessageBox.Information)
        # msg.setText(str(self.time.toString("hh:mm:ss")))
        # msg.exec()
        # print()
        self.name = self.ui.in_Name.toPlainText()

        if self.name == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("FIGYELEM!")
            msg.setText("Adjon meg egy nevet a játék indulásához!")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec()
        else:
            # try:
            #     if self.name == "":
            #         raise Exception('név')
            # except Exception as e:
            #     msg = QtWidgets.QMessageBox()
            #     msg.setWindowTitle("Hiba")
            #     msg.setText("Hiányzó " + str(e) + ".")
            #     msg.exec()

            self.curr_time = QtCore.QTime(00, 00, 00)
            self.timer0 = QtCore.QTimer()
            self.time = QtCore.QTime(00, 00, 00)
            self.timer0.setInterval(1000)
            self.timer0.timeout.connect(self.calc)
            self.timer0.start()
            self.ui.lcdNumber.display(str(self.calc()))

    def loadData(self):
        fin = open("database.txt", "r")
        for r in fin:
            ls = r.split(";")
            nw = Player(ls[0], ls[1])
            self.list.append(nw)
            print(ls)
            #self.ui-ra hibát dob!
            # self.ui.ls_Players.addItem(nw.__str__())
        fin.close()

    def saveData(self):
        try:
            fout = open("database.txt", "a")
            for w in self.list:
                w.save2File(fout)
            fout.close()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setText('Hiba történt:\n' + e.__str__())
            msg.exec()

    def save3File(self, name, time):
        try:
            if name == "":
                raise MissingDataException("név")
            if time == "":
                raise MissingDataException("időtartam")



            fout = open("database.txt", "a")
            for w in self.list:
                w.save2File(fout)
            fout.close()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setText('Hiba történt:\n' + e.__str__())
            msg.exec()

    def saveResults(self):

        try:
            time = "dsad"
            if self.name=='':
                raise MissingDataException('name')
            if time=='':
                raise MissingDataException('time')

            newPlayer = Player(self.name, time)
            self.list.append(newPlayer)
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setText('Hiba történt:\n' + e.__str__())
            msg.exec()

    def calc(self):
        global time
        self.time = self.time.addSecs(1)
        self.ui.lcdNumber.display(self.time.toString("hh:mm:ss"))

    def clickResult(self):
        name = QtWidgets.QApplication.ui.in_Name.text()
        print(name)

    #main
    # t_maze = getMaze()
    # print(t_maze[0][0])

#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec())
