# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(619, 360)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 10, 181, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"text-transform: uppercase;")
        self.btn_agregar = QPushButton(self.centralwidget)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setGeometry(QRect(190, 92, 231, 31))
        self.btn_comprar = QPushButton(self.centralwidget)
        self.btn_comprar.setObjectName(u"btn_comprar")
        self.btn_comprar.setGeometry(QRect(190, 130, 231, 31))
        self.btn_mostrar = QPushButton(self.centralwidget)
        self.btn_mostrar.setObjectName(u"btn_mostrar")
        self.btn_mostrar.setGeometry(QRect(190, 170, 231, 31))
        self.btn_salir = QPushButton(self.centralwidget)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setGeometry(QRect(190, 220, 231, 31))
        self.btn_salir.setStyleSheet(u"background-color: red;\n"
"border: none;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 310, 201, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_precio = QLabel(self.centralwidget)
        self.label_precio.setObjectName(u"label_precio")
        self.label_precio.setGeometry(QRect(220, 310, 47, 16))
        self.label_precio.setFont(font1)
        self.label_precio.setStyleSheet(u"color: #3fe70e;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Panaderia GLORIA", None))
        self.btn_agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar Producto", None))
        self.btn_comprar.setText(QCoreApplication.translate("MainWindow", u"Comprar Productos", None))
        self.btn_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar Productos", None))
        self.btn_salir.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ganacias Hasta el Momento:", None))
        self.label_precio.setText(QCoreApplication.translate("MainWindow", u"$ 0", None))
    # retranslateUi

