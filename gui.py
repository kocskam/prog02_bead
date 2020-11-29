# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testNuIOGn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.b_Start = QPushButton(self.centralwidget)
        self.b_Start.setObjectName(u"b_Start")
        self.b_Start.setGeometry(QRect(30, 480, 91, 41))
        self.b_Exit = QPushButton(self.centralwidget)
        self.b_Exit.setObjectName(u"b_Exit")
        self.b_Exit.setGeometry(QRect(670, 480, 91, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 121, 41))
        self.in_Name = QTextEdit(self.centralwidget)
        self.in_Name.setObjectName(u"in_Name")
        self.in_Name.setGeometry(QRect(30, 130, 91, 41))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(119, 29, 661, 431))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.b_Result = QPushButton(self.centralwidget)
        self.b_Result.setObjectName(u"b_Result")
        self.b_Result.setGeometry(QRect(320, 490, 131, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.ls_Players = QTextBrowser(self.centralwidget)
        self.ls_Players.setObjectName(u"ls_Players")
        self.ls_Players.setGeometry(QRect(240, 290, 256, 192))

        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(30, 360, 64, 23))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_Start.setText(QCoreApplication.translate("MainWindow", u"J\u00e1t\u00e9k Ind\u00edt\u00e1sa", None))
        self.b_Exit.setText(QCoreApplication.translate("MainWindow", u"Kil\u00e9p\u00e9s", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add meg a neved!", None))
        self.b_Result.setText(QCoreApplication.translate("MainWindow", u"Eddigi eredm\u00e9nyek", None))
    # retranslateUi



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())