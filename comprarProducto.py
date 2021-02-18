# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comprarProducto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogComprar(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(411, 235)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 61, 16))
        self.le_codigo = QLineEdit(Dialog)
        self.le_codigo.setObjectName(u"le_codigo")
        self.le_codigo.setGeometry(QRect(10, 60, 391, 20))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 100, 61, 16))
        self.le_cantidad = QLineEdit(Dialog)
        self.le_cantidad.setObjectName(u"le_cantidad")
        self.le_cantidad.setGeometry(QRect(10, 120, 391, 20))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 0, 161, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.btn_agregar_carrito = QPushButton(Dialog)
        self.btn_agregar_carrito.setObjectName(u"btn_agregar_carrito")
        self.btn_agregar_carrito.setGeometry(QRect(140, 160, 131, 23))
        self.btn_pagar_carrito = QPushButton(Dialog)
        self.btn_pagar_carrito.setObjectName(u"btn_pagar_carrito")
        self.btn_pagar_carrito.setGeometry(QRect(10, 160, 111, 23))
        self.btn_pagar_carrito.setStyleSheet(u"background-color: #3fe70e;\n"
"border:none;")
        self.btn_volver = QPushButton(Dialog)
        self.btn_volver.setObjectName(u"btn_volver")
        self.btn_volver.setGeometry(QRect(290, 160, 111, 23))
        self.btn_volver.setStyleSheet(u"background-color: red;\n"
"border: none;\n"
"color: white;\n"
"font-weight: bold;")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 199, 101, 21))
        self.label_total_carrito = QLabel(Dialog)
        self.label_total_carrito.setObjectName(u"label_total_carrito")
        self.label_total_carrito.setGeometry(QRect(360, 200, 47, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"C\u00f3digo:", None))
        self.le_codigo.setText("")
        self.le_codigo.setPlaceholderText(QCoreApplication.translate("Dialog", u"C\u00f3digo del Producto", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Cantidad:", None))
        self.le_cantidad.setText("")
        self.le_cantidad.setPlaceholderText(QCoreApplication.translate("Dialog", u"Cantidad de Productos a Comprar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Comprar Producto", None))
        self.btn_agregar_carrito.setText(QCoreApplication.translate("Dialog", u"Agregar al Carrito", None))
        self.btn_pagar_carrito.setText(QCoreApplication.translate("Dialog", u"Pagar Carrito", None))
        self.btn_volver.setText(QCoreApplication.translate("Dialog", u"Volver", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total del Carrito:", None))
        self.label_total_carrito.setText(QCoreApplication.translate("Dialog", u"$ 0", None))
    # retranslateUi

