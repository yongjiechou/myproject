# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\myproject\hoho.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btstart = QtWidgets.QPushButton(self.centralwidget)
        self.btstart.setGeometry(QtCore.QRect(180, 50, 161, 91))
        self.btstart.setObjectName("btstart")
        self.lcdhr = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdhr.setGeometry(QtCore.QRect(50, 220, 64, 23))
        self.lcdhr.setObjectName("lcdhr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 220, 47, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 220, 47, 21))
        self.label_2.setObjectName("label_2")
        self.lcdmin = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdmin.setGeometry(QtCore.QRect(180, 220, 64, 23))
        self.lcdmin.setObjectName("lcdmin")
        self.lcdsec = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdsec.setGeometry(QtCore.QRect(320, 220, 64, 23))
        self.lcdsec.setObjectName("lcdsec")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 220, 47, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 220, 47, 21))
        self.label_4.setObjectName("label_4")
        self.lcdms = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdms.setGeometry(QtCore.QRect(450, 220, 64, 23))
        self.lcdms.setObjectName("lcdms")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btstart.setText(_translate("MainWindow", "開始計時"))
        self.label.setText(_translate("MainWindow", "hr"))
        self.label_2.setText(_translate("MainWindow", "min"))
        self.label_3.setText(_translate("MainWindow", "sec"))
        self.label_4.setText(_translate("MainWindow", "ms"))
