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


#Funcinones con todos los menús, conectados con su respectivo campo
def edificio_menu():
    ruta_archivo = 'edificios.txt'
    while True:
        print("\n--- Menú de Gestión de Edificios ---")
        print(f"Hay actualmente {len(edificios)} edificios")
        print("1. Crear Edificio")
        print("2. Eliminar Edificio")
        print("3. Mostrar Información de un Edificio")
        print("4. Mostrar Todos los Edificios")
        print("5. Volver al Menú Principal")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            Edificio(0, 0, 0).crear_edificio()
        elif choice == '2':
            id_edificio = input("Ingrese el ID del edificio a eliminar: ")
            edificio = Edificio(0, 0, id_edificio).buscar_edificio(id_edificio)
            if edificio:
                edificio.eliminar_edificio(ruta_archivo)
            else:
                print("Edificio no encontrado.")
        elif choice == '3':
            id_edificio = input("Ingrese el ID del edificio a consultar: ")
            edificio = Edificio(0, 0, id_edificio).buscar_edificio(id_edificio)
            if edificio:
                info = edificio.obtener_info_edificio()
                print(f"Información del edificio: {info}")
            else:
                print("Edificio no encontrado.")
        elif choice == '4':
            mostrar_edificios(edificios)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")



def edificio_menu(edificios):
    ruta_archivo = 'edificios.txt'
    while True:
        print("\n--- Menú de Gestión de Edificios ---")
        print(f"Hay actualmente {len(edificios)} edificios")
        print("1. Crear Edificio")
        print("2. Eliminar Edificio")
        print("3. Mostrar Información de un Edificio")
        print("4. Mostrar Todos los Edificios")
        print("5. Volver al Menú Principal")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            Edificio(0, 0, 0).crear_edificio(edificios)
        elif choice == '2':
            id_edificio = input("Ingrese el ID del edificio a eliminar: ")
            edificio = Edificio(0, 0, id_edificio).buscar_edificio(id_edificio, edificios)
            if edificio:
                edificio.eliminar_edificio(edificios, ruta_archivo)
            else:
                print("Edificio no encontrado.")
        elif choice == '3':
            id_edificio = input("Ingrese el ID del edificio a consultar: ")
            edificio = Edificio(0, 0, id_edificio).buscar_edificio(id_edificio, edificios)
            if edificio:
                info = edificio.obtener_info_edificio()
                print(f"Información del edificio: {info}")
            else:
                print("Edificio no encontrado.")
        elif choice == '4':
            mostrar_edificios(edificios)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def pallet_menu(inventario, clientes, edificios):
    ruta_archivo = 'pallets.txt'
    while True:
        print("\n--- Menú de Gestión de Pallets ---")
        print(f"Hay actualmente {len(inventario)} pallets")
        print("1. Registrar Pallet")
        print("2. Modificar Edificio de un Pallet")
        print("3. Eliminar Pallet")
        print("4. Mostrar Información de un Pallet")
        print("5. Mostrar Todos los Pallets")
        print("6. Volver al Menú Principal")
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            Pallet(0, 0, 0, 0).crear_pallet(inventario, clientes, edificios)
        elif choice == '2':
            id_pallet = input("Ingrese el ID del pallet a modificar: ")
            pallet = Pallet(0, 0, 0, 0).buscar_pallet(id_pallet, inventario)
            if pallet is None:
                print("Pallet no encontrada")
            else:
                nuevo_edificio_id = input("Ingrese el nuevo ID del edificio para el pallet: ")
                pallet.modificar_id_edificio(nuevo_edificio_id, inventario, edificios)
        elif choice == '3':
            id_pallet = input("Ingrese el ID del pallet a eliminar: ")
            Pallet(id_pallet, 0, 0, 0).eliminar_pallet(inventario, ruta_archivo)
        elif choice == '4':
            id_pallet = input("Ingrese el ID del pallet para mostrar información: ")
            pallet = Pallet(0, 0, 0, 0).buscar_pallet(id_pallet, inventario)
            if pallet:
                info = pallet.obtener_info_pallet()
                print(f"Información del pallet: {info}")
            else:
                print("Pallet no encontrada.")
        elif choice == '5':
            mostrar_pallets(inventario)
        elif choice == '6':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def cliente_menu(clientes):
    ruta_archivo = 'clientes.txt'
    while True:
        print("\n--- Menú de Gestión de Clientes ---")
        print(f"Hay actualmente {len(clientes)} clientes")
        print("1. Crear Cliente")
        print("2. Mostrar Información de Cliente")
        print("3. Eliminar Cliente")
        print("4. Mostrar Todos los Clientes")
        print("5. Volver al Menú Principal")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            Cliente(0, 0, 0, 0).crear_cliente(clientes)
        elif choice == '2':
            id_cliente = input("Ingrese el ID del cliente para mostrar información: ")
            cliente = Cliente(0, 0, 0, 0).buscar_cliente(id_cliente, clientes)
            if cliente:
                info = cliente.obtener_info_cliente()
                print(f"Información del cliente: {info}")
            else:
                print("Cliente no encontrado.")
        elif choice == '3':
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            cliente = Cliente(0, 0, 0, 0).buscar_cliente(id_cliente, clientes)
            if cliente:
                cliente.eliminar_cliente(clientes, ruta_archivo)
            else:
                print("Cliente no encontrado.")
        elif choice == '4':
            mostrar_clientes(clientes)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
'''
#MAIN
cargar_edificios(edificios)
cargar_pallets(inventario)
cargar_clientes(clientes)

while True:
    print("\n--- Menú Principal de la WareHouse ---")
    print("1. Edificios")
    print("2. Pallets")
    print("3. Clientes")
    print("4. Salir")
    choice = input("Seleccione una opción: ")
    
    if choice == '1':
        edificio_menu(edificios)
    elif choice == '2':
        pallet_menu(inventario, clientes, edificios)
    elif choice == '3':
        cliente_menu(clientes)
    elif choice == '4':
        print("Gracias por usar el sistema. Hasta luego.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
'''
#TOODO EL PROCESO DE LA CREACIÓN DEL GUI 

COLORS = {
    "background": "#fafafa",
    "text": "#101010",
    "button": "#587962",
    "button_text": "#fafafa",
    "nav_bar": "#7a9983",
    "nav_bar_text": "#fafafa",
}

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

        btn_edificios = QPushButton("Edificios")
        btn_edificios.setFont(FONTS["text"])
        btn_edificios.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_edificios.clicked.connect(self.show_edificio_menu)
        layout.addWidget(btn_edificios)

        btn_pallets = QPushButton("Pallets")
        btn_pallets.setFont(FONTS["text"])
        btn_pallets.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_pallets.clicked.connect(self.show_pallet_menu)
        layout.addWidget(btn_pallets)

        btn_clientes = QPushButton("Clientes")
        btn_clientes.setFont(FONTS["text"])
        btn_clientes.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_clientes.clicked.connect(self.show_cliente_menu)
        layout.addWidget(btn_clientes)

        btn_salir = QPushButton("Salir")
        btn_salir.setFont(FONTS["text"])
        btn_salir.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_salir.clicked.connect(self.close_application)
        layout.addWidget(btn_salir)

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
    
    def close_application(self):
        sys.exit()

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

        btn_create = QPushButton("Crear Edificio")
        btn_create.setFont(FONTS["text"])
        btn_create.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_create.clicked.connect(self.crear_edificio)
        layout.addWidget(btn_create)

        btn_delete = QPushButton("Eliminar Edificio")
        btn_delete.setFont(FONTS["text"])
        btn_delete.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_delete.clicked.connect(self.eliminar_edificio_menu)
        layout.addWidget(btn_delete)

        btn_show_all = QPushButton("Mostrar Edificios")
        btn_show_all.setFont(FONTS["text"])
        btn_show_all.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_show_all.clicked.connect(self.mostrar_edificios)
        layout.addWidget(btn_show_all)

        btn_show_info = QPushButton("Mostrar información de un edificio")
        btn_show_info.setFont(FONTS["text"])
        btn_show_info.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_show_info.clicked.connect(self.mostrar_info_edificio)
        layout.addWidget(btn_show_info)

        btn_back = QPushButton("Volver al menú principal")
        btn_back.setFont(FONTS["text"])
        btn_back.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_back.clicked.connect(self.back_to_main)
        layout.addWidget(btn_back)

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

        btn_create = QPushButton("Registrar Pallet")
        btn_create.setFont(FONTS["text"])
        btn_create.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_create.clicked.connect(self.crear_pallet)
        layout.addWidget(btn_create)

        btn_modify = QPushButton("Modificar Edificio de un Pallet")
        btn_modify.setFont(FONTS["text"])
        btn_modify.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_modify.clicked.connect(self.modificar_pallet)
        layout.addWidget(btn_modify)

        btn_delete = QPushButton("Eliminar Pallet")
        btn_delete.setFont(FONTS["text"])
        btn_delete.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_delete.clicked.connect(self.eliminar_pallet_menu)
        layout.addWidget(btn_delete)

        btn_show_all = QPushButton("Mostrar Pallets")
        btn_show_all.setFont(FONTS["text"])
        btn_show_all.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_show_all.clicked.connect(self.mostrar_pallets)
        layout.addWidget(btn_show_all)

        btn_show_info = QPushButton("Mostrar información de un pallet")
        btn_show_info.setFont(FONTS["text"])
        btn_show_info.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_show_info.clicked.connect(self.mostrar_info_pallet)
        layout.addWidget(btn_show_info)

        btn_back = QPushButton("Volver al menú principal")
        btn_back.setFont(FONTS["text"])
        btn_back.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_back.clicked.connect(self.back_to_main)
        layout.addWidget(btn_back)

        self.setCentralWidget(central_widget)

    def back_to_main(self):
        self.close() 
        self.main_window.show()  

    def crear_pallet(self):
        id_pallet, ok = QInputDialog.getText(self, "Registrar Pallet", "Ingrese el ID del pallet:")
        if ok:
            id_cliente, ok = QInputDialog.getText(self, "Registrar Pallet", "Ingrese el ID del cliente:")
            if ok:
                id_edificio, ok = QInputDialog.getText(self, "Registrar Pallet", "Ingrese el ID del edificio:")
                if ok:
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

        btn_create = QPushButton("Crear Cliente")
        btn_create.setFont(FONTS["text"])
        btn_create.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_create.clicked.connect(self.crear_cliente)
        layout.addWidget(btn_create)

        btn_show_info = QPushButton("Mostrar información de Cliente")
        btn_show_info.setFont(FONTS["text"])
        btn_show_info.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_show_info.clicked.connect(self.mostrar_info_cliente)
        layout.addWidget(btn_show_info)

        btn_show_all = QPushButton("Mostrar información de todos los Clientes")
        btn_show_all.setFont(FONTS["text"])
        btn_show_all.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_show_all.clicked.connect(self.mostrar_clientes)
        layout.addWidget(btn_show_all)

        btn_delete = QPushButton("Eliminar Cliente")
        btn_delete.setFont(FONTS["text"])
        btn_delete.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_delete.clicked.connect(self.eliminar_cliente_menu)
        layout.addWidget(btn_delete)

        btn_back = QPushButton("Volver al menú principal")
        btn_back.setFont(FONTS["text"])
        btn_back.setStyleSheet(f"background-color: {COLORS['button']}; color: {COLORS['button_text']}")
        btn_back.clicked.connect(self.back_to_main)
        layout.addWidget(btn_back)

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