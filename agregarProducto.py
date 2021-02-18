# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregarProducto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogAgregar(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 397)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 0, 161, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"text-align: center;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 61, 16))
        self.le_codigo = QLineEdit(Dialog)
        self.le_codigo.setObjectName(u"le_codigo")
        self.le_codigo.setGeometry(QRect(10, 70, 391, 20))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 61, 16))
        self.le_nombre = QLineEdit(Dialog)
        self.le_nombre.setObjectName(u"le_nombre")
        self.le_nombre.setGeometry(QRect(10, 130, 391, 20))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 61, 16))
        self.le_categoria = QLineEdit(Dialog)
        self.le_categoria.setObjectName(u"le_categoria")
        self.le_categoria.setGeometry(QRect(10, 190, 391, 20))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 230, 61, 16))
        self.le_stock = QLineEdit(Dialog)
        self.le_stock.setObjectName(u"le_stock")
        self.le_stock.setGeometry(QRect(10, 250, 391, 20))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 290, 61, 16))
        self.le_precio = QLineEdit(Dialog)
        self.le_precio.setObjectName(u"le_precio")
        self.le_precio.setGeometry(QRect(10, 310, 391, 20))
        self.btn_agregar_producto = QPushButton(Dialog)
        self.btn_agregar_producto.setObjectName(u"btn_agregar_producto")
        self.btn_agregar_producto.setGeometry(QRect(10, 350, 111, 23))
        self.btn_volver = QPushButton(Dialog)
        self.btn_volver.setObjectName(u"btn_volver")
        self.btn_volver.setGeometry(QRect(290, 350, 111, 23))
        self.btn_volver.setStyleSheet(u"background-color: red;\n"
"border: none;\n"
"color: white;\n"
"font-weight: bold;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Agregar Producto", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"C\u00f3digo:", None))
        self.le_codigo.setText("")
        self.le_codigo.setPlaceholderText(QCoreApplication.translate("Dialog", u"C\u00f3digo del Producto", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.le_nombre.setText("")
        self.le_nombre.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nombre del Producto", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Categor\u00eda:", None))
        self.le_categoria.setText("")
        self.le_categoria.setPlaceholderText(QCoreApplication.translate("Dialog", u"Categor\u00eda del Producto", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Stock:", None))
        self.le_stock.setText("")
        self.le_stock.setPlaceholderText(QCoreApplication.translate("Dialog", u"Stock del Producto", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Precio:", None))
        self.le_precio.setText("")
        self.le_precio.setPlaceholderText(QCoreApplication.translate("Dialog", u"Precio del Producto", None))
        self.btn_agregar_producto.setText(QCoreApplication.translate("Dialog", u"Agregar Producto", None))
        self.btn_volver.setText(QCoreApplication.translate("Dialog", u"Volver", None))
    # retranslateUi

