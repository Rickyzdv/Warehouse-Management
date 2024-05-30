from pathlib import Path
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QInputDialog, QMessageBox
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt
###Edificios###
edificios = []

class Edificio:
    def __init__(self, repisa, ubicacion, id_edificio):
        self.__id_edificio = id_edificio
        self.__ubicacion = ubicacion
        self.__repisa = repisa

    def get_id_edificio(self):
        return self.__id_edificio

    def get_ubicacion_edificio(self):
        return self.__ubicacion

    def get_repisa_edificio(self):
        return self.__repisa

    def guardar_info(self, ruta_archivo='edificios.txt'):
        archivo = Path(ruta_archivo)
        encabezado = "Repisa|Ubicacion|ID\n"
        if not archivo.exists():
            with archivo.open('w', encoding='utf-8') as file:
                file.write(encabezado)

        with archivo.open('a', encoding='utf-8') as file:
            info = f"{self.__repisa}|{self.__ubicacion}|{self.__id_edificio}\n"
            file.write(info)

    def validar_edificio(self, id_edificio, edificios):
        return any(edif.get_id_edificio() == id_edificio for edif in edificios)

    def obtener_info_edificio(self):
        return f"ID: {self.get_id_edificio()}, Ubicación: {self.get_ubicacion_edificio()}, Repisas: {self.get_repisa_edificio()}"

    def buscar_edificio(self, id_edificio, edificios):
        for edif in edificios:
            if edif.get_id_edificio() == id_edificio:
                return edif
        return None
    
    def eliminar(self, edificios, ruta_archivo='edificios.txt'):
        for edif in edificios:
            if edif.get_id_edificio() == self.__id_edificio:
                edificios.remove(edif)
                guardar_edificios(ruta_archivo, edificios)
                print(f"Edificio con ID {self.__id_edificio} eliminado.")
                return
        print("Edificio no encontrado. No se pudo eliminar.")

def cargar_edificios(edificios, ruta_archivo='edificios.txt'):
    ruta = Path(ruta_archivo)
    if ruta.exists():
        with ruta.open('r', encoding='utf-8') as archivo:
            for i, linea in enumerate(archivo):
                if i == 0:  # Omitir el encabezado
                    continue
                repisa, ubicacion, id_edificio = linea.strip().split('|')
                edificios.append(Edificio(repisa, ubicacion, id_edificio))

def guardar_edificios(ruta_archivo, edificios):
    ruta = Path(ruta_archivo)
    encabezado = "Repisa|Ubicacion|ID\n"
    with ruta.open('w', encoding='utf-8') as archivo:
        archivo.write(encabezado)
        for edificio in edificios:
            linea = f"{edificio.get_repisa_edificio()}|{edificio.get_ubicacion_edificio()}|{edificio.get_id_edificio()}\n"
            archivo.write(linea)

def mostrar_edificios(edificios):
    if not edificios:
        print("No hay edificios guardados en el archivo.")
    else:
        for edif in edificios:
            print(f"ID: {edif.get_id_edificio()}, Ubicación: {edif.get_ubicacion_edificio()}, Repisas: {edif.get_repisa_edificio()}")

###Pallet###
inventario = []

class Pallet:
    def __init__(self, id_pallet, id_cliente, id_edificio, fecha_ingreso, fecha_egreso=None):
        self.__id_pallet = id_pallet
        self.id_cliente = id_cliente
        self.id_edificio = id_edificio
        self.fecha_ingreso = fecha_ingreso
        self.fecha_egreso = fecha_egreso

    def get_id_pallet(self):
        return self.__id_pallet

    def guardar_info(self, ruta_archivo='pallets.txt'):
        archivo = Path(ruta_archivo)
        encabezado = "ID Pallet|ID Cliente|ID Edificio|Fecha Ingreso|Fecha Egreso\n"
        if not archivo.exists():
            with archivo.open('w', encoding='utf-8') as file:
                file.write(encabezado)
        
        with archivo.open('a', encoding='utf-8') as file:
            info = f"{self.__id_pallet}|{self.id_cliente}|{self.id_edificio}|{self.fecha_ingreso}|{self.fecha_egreso}\n"
            file.write(info)

    def modificar_id_edificio(self, nuevo_edificio_id, inventario, edificios):
        if any(edificio.get_id_edificio() == nuevo_edificio_id for edificio in edificios):
            self.id_edificio = nuevo_edificio_id
            guardar_pallets('pallets.txt', inventario)
            print(f"ID del edificio para la pallet {self.__id_pallet} actualizado a {nuevo_edificio_id}")
        else:
            print("El nuevo ID del edificio no es válido.")

    def validar_pallet(self, id_pallet, inventario):
        return any(pallet.get_id_pallet() == id_pallet for pallet in inventario)

    def obtener_info_pallet(self):
        return f"ID Pallet: {self.get_id_pallet()}, ID Cliente: {self.id_cliente}, ID Edificio: {self.id_edificio}, Fecha Ingreso: {self.fecha_ingreso}, Fecha Egreso: {self.fecha_egreso}"

    def buscar_pallet(self, id_pallet, inventario):
        for pallet in inventario:
            if pallet.get_id_pallet() == id_pallet:
                return pallet
        return None

    def validar_edificio(self, id_edificio, edificios):
        return any(edificio.get_id_edificio() == id_edificio for edificio in edificios)

    def validar_cliente(self, id_cliente, clientes):
        return any(cliente.get_id_cliente() == id_cliente for cliente in clientes)

def cargar_pallets(inventario, ruta_archivo='pallets.txt'):
    ruta = Path(ruta_archivo)
    if ruta.exists():
        with ruta.open('r', encoding='utf-8') as archivo:
            for i, linea in enumerate(archivo):
                if i == 0: 
                    continue
                id_pallet, id_cliente, id_edificio, fecha_ingreso, fecha_egreso = linea.strip().split('|')
                inventario.append(Pallet(id_pallet, id_cliente, id_edificio, fecha_ingreso, fecha_egreso))

def guardar_pallets(ruta_archivo, inventario):
    ruta = Path(ruta_archivo)
    encabezado = "ID Pallet|ID Cliente|ID Edificio|Fecha Ingreso|Fecha Egreso\n"
    with ruta.open('w', encoding='utf-8') as archivo:
        archivo.write(encabezado)
        for pallet in inventario:
            linea = f"{pallet.get_id_pallet()}|{pallet.id_cliente}|{pallet.id_edificio}|{pallet.fecha_ingreso}|{pallet.fecha_egreso}\n"
            archivo.write(linea)

def mostrar_pallets(inventario):
    if not inventario:
        print("No hay pallets cargadas.")
    else:
        for pallet in inventario:
            print(f"ID Pallet: {pallet.get_id_pallet()}, ID Cliente: {pallet.id_cliente}, ID Edificio: {pallet.id_edificio}, Fecha Ingreso: {pallet.fecha_ingreso}, Fecha Egreso: {pallet.fecha_egreso}")

###Cliente###
clientes = []

class Cliente:
    def __init__(self, id_cliente, empresa, cliente_ingreso, nacionalidad):
        self.__id_cliente = id_cliente
        self.empresa = empresa
        self.cliente_ingreso = cliente_ingreso
        self.nacionalidad = nacionalidad

    def get_id_cliente(self):
        return self.__id_cliente
    
    def guardar_info(self, ruta_archivo='clientes.txt'):
        archivo = Path(ruta_archivo)
        encabezado = "ID Cliente|Empresa|Fecha de Ingreso|Nacionalidad\n"
        if not archivo.exists():
            with archivo.open('w', encoding='utf-8') as file:
                file.write(encabezado)
        
        with archivo.open('a', encoding='utf-8') as file:
            info = f"{self.__id_cliente}|{self.empresa}|{self.cliente_ingreso}|{self.nacionalidad}\n"
            file.write(info)

    def crear_cliente(self, clientes):
        id_cliente = input("Ingresa el ID del cliente: ")
        if self.buscar_cliente(id_cliente, clientes):
            print("¡El ID ya existe! Introduce un ID diferente.")
            return

        empresa = input("Ingresa el nombre de la empresa: ")
        cliente_ingreso = input("Ingresa la fecha de ingreso del cliente: ")
        nacionalidad = input("Ingresa la nacionalidad del cliente: ")
        cliente_nuevo = Cliente(id_cliente, empresa, cliente_ingreso, nacionalidad)
        clientes.append(cliente_nuevo)
        cliente_nuevo.guardar_info()
        print("Cliente creado y guardado exitosamente")

    def eliminar_cliente(self, clientes, ruta_archivo='clientes.txt'):
        for cliente in clientes:
            if cliente.get_id_cliente() == self.__id_cliente:
                clientes.remove(cliente)
                guardar_clientes(ruta_archivo, clientes)
                print(f"Cliente con ID {self.__id_cliente} eliminado.")
                return
        print("Cliente no encontrado. No se pudo eliminar.")

    def obtener_info_cliente(self):
        return f"ID Cliente: {self.get_id_cliente()}, Empresa: {self.empresa}, Fecha de Ingreso: {self.cliente_ingreso}, Nacionalidad: {self.nacionalidad}"

    def buscar_cliente(self, id_cliente, clientes):
        for cliente in clientes:
            if cliente.get_id_cliente() == id_cliente:
                return cliente
        return None

def cargar_clientes(clientes, ruta_archivo='clientes.txt'):
    ruta = Path(ruta_archivo)
    if ruta.exists():
        with ruta.open('r', encoding='utf-8') as archivo:
            for i, linea in enumerate(archivo):
                if i == 0:  # Omitir el encabezado
                    continue
                id_cliente, empresa, cliente_ingreso, nacionalidad = linea.strip().split('|')
                clientes.append(Cliente(id_cliente, empresa, cliente_ingreso, nacionalidad))

def guardar_clientes(ruta_archivo, clientes):
    ruta = Path(ruta_archivo)
    encabezado = "ID Cliente|Empresa|Fecha de Ingreso|Nacionalidad\n"
    with ruta.open('w', encoding='utf-8') as archivo:
        archivo.write(encabezado)
        for cliente in clientes:
            linea = f"{cliente.get_id_cliente()}|{cliente.empresa}|{cliente.cliente_ingreso}|{cliente.nacionalidad}\n"
            archivo.write(linea)

def mostrar_clientes(clientes):
    if not clientes:
        print("No hay clientes cargados.")
    else:
        for cliente in clientes:
            print(f"ID Cliente: {cliente.get_id_cliente()}, Empresa: {cliente.empresa}, Fecha de Ingreso: {cliente.cliente_ingreso}, Nacionalidad: {cliente.nacionalidad}")

#TOODO EL PROCESO DE LA CREACIÓN DEL GUI 

#Colores de los wireframes
COLORS = {
    "background": "#fafafa",
    "text": "#101010",
    "button": "#587962",
    "button_text": "#fafafa",
    "nav_bar": "#7a9983",
    "nav_bar_text": "#fafafa",
}

#Fuentes que usaremos
FONTS = {
    "title": QFont("Libre Franklin", 14, QFont.Weight.Bold),
    "text": QFont("Merriweather", 12),
    "menu": QFont("Pt Serif", 12, QFont.Weight.Bold),
}

# Ventana Principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        cargar_edificios(edificios)
        cargar_pallets(inventario)
        cargar_clientes(clientes)
        self.iniciar_ventana()

    def iniciar_ventana(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Gestión de Almacén")
        self.setStyleSheet(f"background-color: {COLORS['background']}")

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        title = QLabel("Menú Principal del Almacén")
        title.setFont(FONTS["title"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {COLORS['text']}")
        layout.addWidget(title)

        boton_edificios = QPushButton("Edificios")
        boton_edificios.setFont(FONTS["text"])
        boton_edificios.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_edificios.clicked.connect(self.show_edificio_menu)
        layout.addWidget(boton_edificios)

        boton_pallets = QPushButton("Pallets")
        boton_pallets.setFont(FONTS["text"])
        boton_pallets.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_pallets.clicked.connect(self.show_pallet_menu)
        layout.addWidget(boton_pallets)

        boton_clientes = QPushButton("Clientes")
        boton_clientes.setFont(FONTS["text"])
        boton_clientes.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_clientes.clicked.connect(self.show_cliente_menu)
        layout.addWidget(boton_clientes)

        boton_salir = QPushButton("Salir")
        boton_salir.setFont(FONTS["text"])
        boton_salir.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_salir.clicked.connect(self.close_application)
        layout.addWidget(boton_salir)

        self.setCentralWidget(central_widget)

        self.show()
    
    def show_edificio_menu(self):
        self.close()
        self.edificio_menu = EdificioMenu(self)
        self.edificio_menu.show()

    def show_pallet_menu(self):
        self.close()
        self.pallet_menu = PalletMenu(self)
        self.pallet_menu.show()

    def show_cliente_menu(self):
        self.close()
        self.cliente_menu = ClienteMenu(self)
        self.cliente_menu.show()
    #Implementado simplemente para cerrar ventanas al momento de querer abrir otra
    def close_application(self):
        sys.exit()

#Ventana de edificios
class EdificioMenu(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Gestión de Edificios")
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet(f"background-color: {COLORS['background']}")

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        title = QLabel("Gestión de Edificios")
        title.setFont(FONTS["title"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {COLORS['text']}")
        layout.addWidget(title)

        boton_create_edificio = QPushButton("Crear Edificio")
        boton_create_edificio.setFont(FONTS["text"])
        boton_create_edificio.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_create_edificio.clicked.connect(self.crear_edificio)
        layout.addWidget(boton_create_edificio)

        boton_delete_edificio = QPushButton("Eliminar Edificio")
        boton_delete_edificio.setFont(FONTS["text"])
        boton_delete_edificio.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_delete_edificio.clicked.connect(self.eliminar_edificio_menu)
        layout.addWidget(boton_delete_edificio)

        boton_mostrar_edificios= QPushButton("Mostrar Edificios")
        boton_mostrar_edificios.setFont(FONTS["text"])
        boton_mostrar_edificios.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_mostrar_edificios.clicked.connect(self.mostrar_edificios)
        layout.addWidget(boton_mostrar_edificios)

        boton_mostrar_info_edificio= QPushButton("Mostrar información de un edificio")
        boton_mostrar_info_edificio.setFont(FONTS["text"])
        boton_mostrar_info_edificio.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_mostrar_info_edificio.clicked.connect(self.mostrar_info_edificio)
        layout.addWidget(boton_mostrar_info_edificio)

        boton_volver= QPushButton("Volver al menú principal")
        boton_volver.setFont(FONTS["text"])
        boton_volver.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_volver.clicked.connect(self.back_to_main)
        layout.addWidget(boton_volver)

        self.setCentralWidget(central_widget)

    def back_to_main(self):
        self.close() 
        self.main_window.show()  

    def crear_edificio(self):
        id_edificio, ok = QInputDialog.getText(self, "Crear Edificio", "Ingrese el ID del edificio:")
        if ok:
            ubicacion, ok = QInputDialog.getText(self, "Crear Edificio", "Ingrese la ubicación del edificio:")
            if ok:
                repisa, ok = QInputDialog.getText(self, "Crear Edificio", "Ingrese el número de repisas del edificio:")
                if ok:
                    if not Edificio(0, 0, 0).validar_edificio(id_edificio, edificios):
                        edificio_nuevo = Edificio(repisa, ubicacion, id_edificio)
                        edificios.append(edificio_nuevo)
                        edificio_nuevo.guardar_info()
                        QMessageBox.information(self, "Éxito", "Edificio creado y guardado exitosamente")
                    else:
                        QMessageBox.warning(self, "Error", "¡El ID ya existe! Introduce un ID diferente.")

    def eliminar_edificio_menu(self):
        id_edificio, ok = QInputDialog.getText(self, "Eliminar Edificio", "Ingrese el ID del edificio a eliminar:")
        if ok:
            edificio = Edificio(0, 0, id_edificio).buscar_edificio(id_edificio, edificios)
            if edificio:
                edificio.eliminar(edificios)
                QMessageBox.information(self, "Éxito", f"Edificio con ID {id_edificio} eliminado exitosamente.")
            else:
                QMessageBox.warning(self, "Error", "Edificio no encontrado.")

    def mostrar_edificios(self):
        info = ""
        for edif in edificios:
            info += f"ID: {edif.get_id_edificio()}, Ubicación: {edif.get_ubicacion_edificio()}, Repisas: {edif.get_repisa_edificio()}\n"
        if not info:
            info = "No hay edificios guardados en el archivo."
        QMessageBox.information(self, "Edificios", info)

    def mostrar_info_edificio(self):
        id_edificio, ok = QInputDialog.getText(self, "Mostrar Información de Edificio", "Ingrese el ID del edificio a consultar:")
        if ok:
            edificio = Edificio(0, 0, id_edificio).buscar_edificio(id_edificio, edificios)
            if edificio:
                info = edificio.obtener_info_edificio()
                QMessageBox.information(self, "Información del Edificio", info)
            else:
                QMessageBox.warning(self, "Error", "Edificio no encontrado.")
#Ventana de pallets
class PalletMenu(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Gestión de Pallets")
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet(f"background-color: {COLORS['background']}")

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        title = QLabel("Gestión de Pallets")
        title.setFont(FONTS["title"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {COLORS['text']}")
        layout.addWidget(title)

        boton_create_pallet = QPushButton("Registrar Pallet")
        boton_create_pallet.setFont(FONTS["text"])
        boton_create_pallet.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_create_pallet.clicked.connect(self.crear_pallet)
        layout.addWidget(boton_create_pallet)

        boton_mover_de_edificio= QPushButton("Modificar Edificio de un Pallet")
        boton_mover_de_edificio.setFont(FONTS["text"])
        boton_mover_de_edificio.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_mover_de_edificio.clicked.connect(self.modificar_pallet)
        layout.addWidget(boton_mover_de_edificio)

        boton_delete_pallet = QPushButton("Eliminar Pallet")
        boton_delete_pallet.setFont(FONTS["text"])
        boton_delete_pallet.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_delete_pallet.clicked.connect(self.eliminar_pallet_menu)
        layout.addWidget(boton_delete_pallet)

        boton_mostrar_pallets= QPushButton("Mostrar Pallets")
        boton_mostrar_pallets.setFont(FONTS["text"])
        boton_mostrar_pallets.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_mostrar_pallets.clicked.connect(self.mostrar_pallets)
        layout.addWidget(boton_mostrar_pallets)

        boton_mostrar_un_pallet= QPushButton("Mostrar información de un pallet")
        boton_mostrar_un_pallet.setFont(FONTS["text"])
        boton_mostrar_un_pallet.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_mostrar_un_pallet.clicked.connect(self.mostrar_info_pallet)
        layout.addWidget(boton_mostrar_un_pallet)

        boton_volver = QPushButton("Volver al menú principal")
        boton_volver.setFont(FONTS["text"])
        boton_volver.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_volver.clicked.connect(self.back_to_main)
        layout.addWidget(boton_volver)

        self.setCentralWidget(central_widget)

    def back_to_main(self):
        self.close() 
        self.main_window.show()  

    def crear_pallet(self):
        id_pallet, ok = QInputDialog.getText(self, "Registrar Pallet", "Ingrese el ID del pallet:")
        if ok:
                id_cliente, ok = QInputDialog.getText(self, "Registrar Pallet", "Ingrese el ID del cliente:")
                if ok:
                    if not Pallet(0, 0, 0, 0).validar_cliente(id_cliente, clientes):
                        QMessageBox.warning(self, "Error", "El ID del cliente no es válido.")
                        return
                    
                    id_edificio, ok = QInputDialog.getText(self, "Registrar Pallet", "Ingrese el ID del edificio:")
                    if ok:
                        if not Pallet(0, 0, 0, 0).validar_edificio(id_edificio, edificios):
                            QMessageBox.warning(self, "Error", "El ID del edificio no es válido.")
                            return
                        
                        fecha_ingreso, ok = QInputDialog.getText(self, "Registrar Pallet", "Ingrese la fecha de ingreso:")
                        if ok:
                            if not Pallet(0, 0, 0, 0).validar_pallet(id_pallet, inventario):
                                pallet_nuevo = Pallet(id_pallet, id_cliente, id_edificio, fecha_ingreso)
                                inventario.append(pallet_nuevo)
                                pallet_nuevo.guardar_info()
                                QMessageBox.information(self, "Éxito", "Pallet registrado y guardado exitosamente")
                            else:
                                QMessageBox.warning(self, "Error", "¡El ID ya existe! Introduce un ID diferente.")

    def modificar_pallet(self):
        id_pallet, ok = QInputDialog.getText(self, "Modificar Pallet", "Ingrese el ID del pallet a modificar:")
        if ok:
            pallet = Pallet(0, 0, 0, 0).buscar_pallet(id_pallet, inventario)
            if pallet is None:
                QMessageBox.warning(self, "Error", "Pallet no encontrada")
            else:
                nuevo_edificio_id, ok = QInputDialog.getText(self, "Modificar Pallet", "Ingrese el nuevo ID del edificio para el pallet:")
                if ok:
                    if any(edificio.get_id_edificio() == nuevo_edificio_id for edificio in edificios):
                        pallet.modificar_id_edificio(nuevo_edificio_id, inventario, edificios)
                        QMessageBox.information(self, "Éxito", f"ID del edificio para la pallet {id_pallet} actualizado a {nuevo_edificio_id}")
                    else:
                        QMessageBox.warning(self, "Error", "El nuevo ID del edificio no es válido.")

    def eliminar_pallet_menu(self):
        id_pallet, ok = QInputDialog.getText(self, "Eliminar Pallet", "Ingrese el ID del pallet a eliminar:")
        if ok:
            pallet = Pallet(0, 0, 0, 0).buscar_pallet(id_pallet, inventario)
            if pallet:
                pallet.eliminar_pallet(inventario)
                QMessageBox.information(self, "Éxito", f"Pallet con ID {id_pallet} eliminada exitosamente.")
            else:
                QMessageBox.warning(self, "Error", "Pallet no encontrada.")

    def mostrar_pallets(self):
        info = ""
        for pallet in inventario:
            info += f"ID Pallet: {pallet.get_id_pallet()}, ID Cliente: {pallet.id_cliente}, ID Edificio: {pallet.id_edificio}, Fecha Ingreso: {pallet.fecha_ingreso}, Fecha Egreso: {pallet.fecha_egreso}\n"
        if not info:
            info = "No hay pallets registradas."
        QMessageBox.information(self, "Pallets", info)

    def mostrar_info_pallet(self):
        id_pallet, ok = QInputDialog.getText(self, "Mostrar Información de Pallet", "Ingrese el ID del pallet a consultar:")
        if ok:
            pallet = Pallet(0, 0, 0, 0).buscar_pallet(id_pallet, inventario)
            if pallet:
                info = pallet.obtener_info_pallet()
                QMessageBox.information(self, "Información del Pallet", info)
            else:
                QMessageBox.warning(self, "Error", "Pallet no encontrada.")
#Ventana de cliente
class ClienteMenu(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Gestión de Clientes")
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet(f"background-color: {COLORS['background']}")

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        title = QLabel("Gestión de Clientes")
        title.setFont(FONTS["title"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {COLORS['text']}")
        layout.addWidget(title)

        boton_create_cliente = QPushButton("Crear Cliente")
        boton_create_cliente.setFont(FONTS["text"])
        boton_create_cliente.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_create_cliente.clicked.connect(self.crear_cliente)
        layout.addWidget(boton_create_cliente)

        boton_mostrar_info_cliente = QPushButton("Mostrar información de Cliente")
        boton_mostrar_info_cliente.setFont(FONTS["text"])
        boton_mostrar_info_cliente.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_mostrar_info_cliente.clicked.connect(self.mostrar_info_cliente)
        layout.addWidget(boton_mostrar_info_cliente)

        boton_mostrar_clientes = QPushButton("Mostrar información de todos los Clientes")
        boton_mostrar_clientes.setFont(FONTS["text"])
        boton_mostrar_clientes.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_mostrar_clientes.clicked.connect(self.mostrar_clientes)
        layout.addWidget(boton_mostrar_clientes)

        boton_delete_cliente = QPushButton("Eliminar Cliente")
        boton_delete_cliente.setFont(FONTS["text"])
        boton_delete_cliente.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_delete_cliente.clicked.connect(self.eliminar_cliente_menu)
        layout.addWidget(boton_delete_cliente)

        boton_volver = QPushButton("Volver al menú principal")
        boton_volver.setFont(FONTS["text"])
        boton_volver.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        boton_volver.clicked.connect(self.back_to_main)
        layout.addWidget(boton_volver)

        self.setCentralWidget(central_widget)

    def back_to_main(self):
        self.close()  
        self.main_window.show() 

    def crear_cliente(self):
        id_cliente, ok = QInputDialog.getText(self, "Crear Cliente", "Ingrese el ID del cliente:")
        if ok:
            empresa, ok = QInputDialog.getText(self, "Crear Cliente", "Ingrese el nombre de la empresa:")
            if ok:
                cliente_ingreso, ok = QInputDialog.getText(self, "Crear Cliente", "Ingrese la fecha de ingreso del cliente:")
                if ok:
                    nacionalidad, ok = QInputDialog.getText(self, "Crear Cliente", "Ingrese la nacionalidad del cliente:")
                    if ok:
                        if not Cliente(0, 0, 0, 0).buscar_cliente(id_cliente, clientes):
                            cliente_nuevo = Cliente(id_cliente, empresa, cliente_ingreso, nacionalidad)
                            clientes.append(cliente_nuevo)
                            cliente_nuevo.guardar_info()
                            QMessageBox.information(self, "Éxito", "Cliente creado y guardado exitosamente")
                        else:
                            QMessageBox.warning(self, "Error", "¡El ID ya existe! Introduce un ID diferente.")

    def mostrar_info_cliente(self):
        id_cliente, ok = QInputDialog.getText(self, "Mostrar Información de Cliente", "Ingrese el ID del cliente a consultar:")
        if ok:
            cliente = Cliente(0, 0, 0, 0).buscar_cliente(id_cliente, clientes)
            if cliente:
                info = cliente.obtener_info_cliente()
                QMessageBox.information(self, "Información del Cliente", info)
            else:
                QMessageBox.warning(self, "Error", "Cliente no encontrado.")

    def mostrar_clientes(self):
        info = ""
        for cliente in clientes:
            info += f"ID Cliente: {cliente.get_id_cliente()}, Empresa: {cliente.empresa}, Fecha de Ingreso: {cliente.cliente_ingreso}, Nacionalidad: {cliente.nacionalidad}\n"
        if not info:
            info = "No hay clientes registrados."
        QMessageBox.information(self, "Clientes", info)

    def eliminar_cliente_menu(self):
        id_cliente, ok = QInputDialog.getText(self, "Eliminar Cliente", "Ingrese el ID del cliente a eliminar:")
        if ok:
            cliente = Cliente(0, 0, 0, 0).buscar_cliente(id_cliente, clientes)
            if cliente:
                cliente.eliminar_cliente(clientes)
                QMessageBox.information(self, "Éxito", f"Cliente con ID {id_cliente} eliminado exitosamente.")
            else:
                QMessageBox.warning(self, "Error", "Cliente no encontrado.")

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()  
sys.exit(app.exec())