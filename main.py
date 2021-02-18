# Importar módulos genéricos
import sys


# Importar módulos de PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot


# Importar Interfaces
from mainWindow import Ui_MainWindow
from agregarProducto import Ui_DialogAgregar
from comprarProducto import Ui_DialogComprar
from tabla import Ui_DialogTabla


''' Programa Principal '''

productos = []
productosAuxiliar = []
ganancias_totales = 0


# MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_salir.clicked.connect(self.salir)
        self.ui.btn_agregar.clicked.connect(self.mostrar_agregar)
        self.ui.btn_comprar.clicked.connect(self.mostrar_comprar)
        self.ui.btn_mostrar.clicked.connect(self.mostrar_tabla)



    @Slot()
    def mostrar_agregar(self):
        main_window.hide()
        agregar_window.reiniciarLe()
        agregar_window.show()

    @Slot()
    def mostrar_comprar(self):
        main_window.hide()
        comprar_window.reiniciarLe()
        comprar_window.reiniciarLabel()
        comprar_window.actualizarProductosTemporales()
        comprar_window.show()

    @Slot()
    def mostrar_tabla(self):
        main_window.hide()
        tabla_window.actualizar_tabla()
        tabla_window.show()

    @Slot()
    def salir(self):
        sys.exit(app.exec_())

    def actualizarLabel(self):
        global ganancias_totales
        self.ui.label_precio.setText('$ ' + str(ganancias_totales))


# AgregarWindow
class DialogAgregar(QDialog, Ui_DialogAgregar):
    def __init__(self, parent=None):
        super(DialogAgregar, self).__init__()
        self.ui = Ui_DialogAgregar()
        self.setupUi(self)

        self.btn_volver.clicked.connect(self.volver)
        self.btn_agregar_producto.clicked.connect(self.agregar_producto)

    @Slot()
    def agregar_producto(self):
        if self.le_codigo.text().isnumeric() and self.no_existe(int(self.le_codigo.text())):
            codigo = int(self.le_codigo.text())
            if self.le_nombre.text() != '':
                nombre = self.le_nombre.text()
                if self.le_categoria.text() != '':
                    categoria = self.le_categoria.text()
                    if self.le_stock.text().isnumeric() and int(self.le_stock.text()) > 0:
                        stock = int(self.le_stock.text())
                        if self.le_precio.text().isnumeric() and int(self.le_precio.text()) > 0:
                            precio = int(self.le_precio.text())

                            nuevo_producto = {
                                'codigo': codigo,
                                'nombre': nombre,
                                'categoria': categoria,
                                'stock': stock,
                                'precio': precio
                            }

                            productos.append(nuevo_producto)
                            print(productos)

                            self.reiniciarLe()


    @Slot()
    def volver(self):
        agregar_window.hide()
        main_window.show()


    def no_existe(self, valor):
        for i in range(len(productos)):
            if valor == productos[i]['codigo']:
                return False
                break
        return True

    def reiniciarLe(self):
        self.le_codigo.setText('')
        self.le_nombre.setText('')
        self.le_categoria.setText('')
        self.le_stock.setText('')
        self.le_precio.setText('')
        

# ComprarWindow
class DialogComprar(QDialog, Ui_DialogComprar):
    def __init__(self, parent=None):
        super(DialogComprar, self).__init__()
        self.ui = Ui_DialogComprar()
        self.setupUi(self)

        self.btn_volver.clicked.connect(self.volver)
        self.btn_agregar_carrito.clicked.connect(self.agregar)
        self.btn_pagar_carrito.clicked.connect(self.pagar)

        self.total_carrito = 0


    @Slot()
    def agregar(self):
        global productosAuxiliar

        if self.le_codigo.text().isnumeric():
            
            existe, indice = self.existe(int(self.le_codigo.text()))

            if existe:
                codigo_a_comprar = int(self.le_codigo.text())
                if self.le_cantidad.text().isnumeric() and int(self.le_cantidad.text()) > 0 and productosAuxiliar[indice]['stock'] >= int(self.le_cantidad.text()):
                    cantidad_a_comprar = int(self.le_cantidad.text())

                    productosAuxiliar[indice]['stock'] -= int(self.le_cantidad.text())
                    self.total_carrito += productosAuxiliar[indice]['precio'] * int(self.le_cantidad.text())
                    self.label_total_carrito.setText('$ ' + str(self.total_carrito))

                    self.reiniciarLe()

    @Slot()
    def pagar(self):
        global ganancias_totales
        global productos
        
        if self.total_carrito > 100:
            self.total_carrito -= self.total_carrito / 100 * 3
        elif self.total_carrito > 300:
            self.total_carrito -= self.total_carrito / 100 * 10
        elif self.total_carrito > 500:
            self.total_carrito -= self.total_carrito / 100 * 20

        ganancias_totales += self.total_carrito
        productos = productosAuxiliar.copy()

        comprar_window.hide()
        main_window.actualizarLabel()
        main_window.show()

    @Slot()
    def volver(self):
        comprar_window.hide()
        main_window.show()

    def actualizarProductosTemporales(self):
        global productosAuxiliar
        productosAuxiliar = productos.copy()

    def existe(self, valor):
        for i in range(len(productos)):
            if valor == productos[i]['codigo']:
                return True, i
                break
        return False

    def reiniciarLe(self):
        self.le_codigo.setText('')
        self.le_cantidad.setText('')
    
    def reiniciarLabel(self):
        self.label_total_carrito.setText('$ 0')
        self.total_carrito = 0

# TablaWindow
class DialogTabla(QDialog, Ui_DialogTabla):
    def __init__(self, parent=None):
        super(DialogTabla, self).__init__()
        self.ui = Ui_DialogTabla()
        self.setupUi(self)

        self.btn_volver.clicked.connect(self.volver)

    @Slot()
    def volver(self):
        tabla_window.hide()
        main_window.show()

    def actualizar_tabla(self):
        for i in range(len(productos)):
            numero_fila = self.tabla.rowCount()
            if i < numero_fila:
                self.tabla.setItem(i, 0, QTableWidgetItem(str(productos[i]['codigo'])))
                self.tabla.setItem(i, 1, QTableWidgetItem(productos[i]['nombre']))
                self.tabla.setItem(i, 2, QTableWidgetItem(productos[i]['categoria']))
                self.tabla.setItem(i, 3, QTableWidgetItem(str(productos[i]['stock'])))
                self.tabla.setItem(i, 4, QTableWidgetItem(str(productos[i]['precio'])))
            else:
                self.tabla.insertRow(numero_fila)

                self.tabla.setItem(numero_fila, 0, QTableWidgetItem(str(productos[i]['codigo'])))
                self.tabla.setItem(numero_fila, 1, QTableWidgetItem(productos[i]['nombre']))
                self.tabla.setItem(numero_fila, 2, QTableWidgetItem(productos[i]['categoria']))
                self.tabla.setItem(numero_fila, 3, QTableWidgetItem(str(productos[i]['stock'])))
                self.tabla.setItem(numero_fila, 4, QTableWidgetItem(str(productos[i]['precio'])))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear Ventanas
    main_window = MainWindow()
    agregar_window = DialogAgregar()
    comprar_window = DialogComprar()
    tabla_window = DialogTabla()

    main_window.show()

    sys.exit(app.exec_())