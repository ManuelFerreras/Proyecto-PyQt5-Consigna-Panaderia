# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabla.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogTabla(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(531, 437)
        self.tabla = QTableWidget(Dialog)
        if (self.tabla.columnCount() < 5):
            self.tabla.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(10, 10, 511, 381))
        self.btn_volver = QPushButton(Dialog)
        self.btn_volver.setObjectName(u"btn_volver")
        self.btn_volver.setGeometry(QRect(10, 400, 111, 23))
        self.btn_volver.setStyleSheet(u"background-color: red;\n"
"border: none;\n"
"color: white;\n"
"font-weight: bold;")
        self.btn_ordenar_categoria = QPushButton(Dialog)
        self.btn_ordenar_categoria.setObjectName(u"btn_ordenar_categoria")
        self.btn_ordenar_categoria.setGeometry(QRect(260, 400, 121, 23))
        self.btn_ordenar_precio = QPushButton(Dialog)
        self.btn_ordenar_precio.setObjectName(u"btn_ordenar_precio")
        self.btn_ordenar_precio.setGeometry(QRect(400, 400, 121, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Categor\u00eda", None));
        ___qtablewidgetitem3 = self.tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Stock", None));
        ___qtablewidgetitem4 = self.tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Precio", None));
        self.btn_volver.setText(QCoreApplication.translate("Dialog", u"Volver", None))
        self.btn_ordenar_categoria.setText(QCoreApplication.translate("Dialog", u"Ordenar por Categor\u00eda", None))
        self.btn_ordenar_precio.setText(QCoreApplication.translate("Dialog", u"Ordenar por Precio", None))
    # retranslateUi

