from pathlib import Path

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

    def crear_edificio(self, edificios):
        while True:
            id_edificio = input("Dame el ID del edificio: ")
            if self.validar_edificio(id_edificio, edificios):
                print("¡El ID ya existe! Introduce un ID diferente.")
            else:
                break

        ubicacion = input("Dame la ubicación del edificio: ")
        repisa = input("Dame el número de repisas del edificio: ")
        edificio_nuevo = Edificio(repisa, ubicacion, id_edificio)
        edificios.append(edificio_nuevo)
        edificio_nuevo.guardar_info()
        print("Edificio creado y guardado exitosamente")

    def eliminar_edificio(self, edificios, ruta_archivo='edificios.txt'):
        for edif in edificios:
            if edif.get_id_edificio() == self.__id_edificio:
                edificios.remove(edif)
                guardar_edificios(ruta_archivo, edificios)
                print(f"Edificio con ID {self.__id_edificio} eliminado.")
                return
        print("Edificio no encontrado. No se pudo eliminar.")

    def validar_edificio(self, id_edificio, edificios):
        return any(edif.get_id_edificio() == id_edificio for edif in edificios)

    def obtener_info_edificio(self):
        return f"ID: {self.get_id_edificio()}, Ubicación: {self.get_ubicacion_edificio()}, Repisas: {self.get_repisa_edificio()}"

    def buscar_edificio(self, id_edificio, edificios):
        for edif in edificios:
            if edif.get_id_edificio() == id_edificio:
                return edif
        return None

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

    def crear_pallet(self, inventario, clientes, edificios):
        if not clientes:
            print("No hay clientes disponibles. Crea un cliente antes de crear un pallet.")
            return
        if not edificios:
            print("No hay edificios disponibles. Crea un edificio antes de crear un pallet.")
            return
        
        while True:
            id_pallet = input("Ingresa el ID del pallet: ")
            if self.validar_pallet(id_pallet, inventario):
                print("¡El ID ya existe! Introduce un ID diferente.")
                continue
            
            print("Clientes disponibles:")
            mostrar_clientes(clientes)
            id_cliente = input("Ingresa el ID del cliente: ")
            if not self.validar_cliente(id_cliente, clientes):
                print("¡El cliente no existe! Introduce un cliente válido.")
                continue
            
            print("Edificios disponibles:")
            mostrar_edificios(edificios)
            id_edificio = input("Ingresa el ID del edificio: ")
            if not self.validar_edificio(id_edificio, edificios):
                print("¡El edificio no existe! Introduce un edificio válido.")
                continue
            
            fecha_ingreso = input("Ingresa la fecha de ingreso: ")
            pallet_nuevo = Pallet(id_pallet, id_cliente, id_edificio, fecha_ingreso)
            inventario.append(pallet_nuevo)
            pallet_nuevo.guardar_info()
            print("Pallet creada y guardada exitosamente!")
            break

    def eliminar_pallet(self, inventario, ruta_archivo='pallets.txt'):
        for pallet in inventario:
            if pallet.get_id_pallet() == self.__id_pallet:
                inventario.remove(pallet)
                guardar_pallets(ruta_archivo, inventario)
                print(f"Pallet con ID {self.__id_pallet} eliminada.")
                return
        print("Pallet no encontrada. No se pudo eliminar.")

    def modificar_id_edificio(self, nuevo_edificio_id, inventario, edificios):
        if self.validar_edificio(nuevo_edificio_id, edificios):
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