# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testXIXECB.ui'
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
        MainWindow.resize(1243, 702)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.b_Start = QPushButton(self.centralwidget)
        self.b_Start.setObjectName(u"b_Start")
        self.b_Start.setGeometry(QRect(10, 600, 91, 41))
        self.b_Exit = QPushButton(self.centralwidget)
        self.b_Exit.setObjectName(u"b_Exit")
        self.b_Exit.setGeometry(QRect(10, 540, 91, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 121, 41))
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(10, 490, 64, 23))
        self.ls_Players = QTextBrowser(self.centralwidget)
        self.ls_Players.setObjectName(u"ls_Players")
        self.ls_Players.setGeometry(QRect(10, 160, 141, 301))
        self.in_Name = QTextEdit(self.centralwidget)
        self.in_Name.setObjectName(u"in_Name")
        self.in_Name.setGeometry(QRect(10, 40, 91, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 121, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1243, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_Start.setText(QCoreApplication.translate("MainWindow", u"J\u00e1t\u00e9k Ind\u00edt\u00e1sa", None))
        self.b_Exit.setText(QCoreApplication.translate("MainWindow", u"Kil\u00e9p\u00e9s", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add meg a neved!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Eddigi eredm\u00e9nyek:", None))
    # retranslateUi




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())