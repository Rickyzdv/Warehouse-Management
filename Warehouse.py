###Edificio###
# Clase Edificio
edificios = [] #Aquí almacenaremos a todos nuestros edificios

class Edificio:
    def __init__(self, repisa, ubicacion, id_edificio):#Definimos nuestro constructor y sus atributos 
        self.__id_edificio = id_edificio
        self.__ubicacion = ubicacion
        self.__repisa = repisa

    def getID(self):
        return self.__id_edificio


    def crear_edificio(self):#Función para crear el edificio, junto con una validación incluida para verificar su existencia o no
        while True:
            id_edificio = input("Dame el ID del edificio: ")
            if self.validar_edificio(id_edificio):
                print("¡El ID ya existe! Introduce un ID diferente.")
            else:
                break

        ubicacion = input("Dame la ubicación del edificio: ")
        repisa = input("Dame el número de repisas del edificio: ")
        edificio_nuevo = Edificio(repisa, ubicacion, id_edificio)
        edificios.append(edificio_nuevo)#Agrega el nuevo edificio creado al arreglo de edificios
        edificio_nuevo.guardar_info()#Guardar la info en el txt
        print("Edificio creado y guardado exitosamente")


    def eliminar_edificio(self):#Recorremos el arreglo y eliminamos el edificio, localizando a través del ID
        
        for edif in edificios:
            if edif.__id_edificio == self.get_id_edificio():
                edificios.remove(edif)
                print(f"Edificio con ID {self.get_id_edificio()} eliminado.")
                return
        print("Edificio no encontrado. No se pudo eliminar.")


    def validar_edificio(self, id_edificio):#Recorremos el arreglo de edificios, para verificar si ya existe o todavía no. Localizamos a través del ID
        return id_edificio in [edif.__id_edificio for edif in edificios]


    def obtener_info_edificio(self):#Recorremos el arreglo y desplegamos la info del edificio deseado
        
        for edif in edificios:
            if edif.get_id_edificio() == self.get_id_edificio():
                info = f"ID: {edif.get_id_edificio()}, Ubicación: {edif.get_ubicacion_edificio()}, Repisas: {edif.get_repisa_edificio()}"
                return info
        return "Edificio no encontrado"

    def buscar_edificio(self, id_edificio):

        for edif in edificios:
            if edif.get_id_edificio() == id_edificio:
                print(f"Edificio con ID {id_edificio} encontrado.")
                return edif
            
        #print(f"Edificio con ID {id_edificio} no encontrado.")
        return

    
    def get_id_edificio(self):
        return self.__id_edificio
    
    def get_ubicacion_edificio(self):
        return self.__ubicacion
    
    def get_repisa_edificio(self):
        return self.__repisa
    
    def guardar_info(self):
        with open('edificios.txt', 'a') as file:
            info = f"ID: {self.get_id_edificio()}, Ubicación: {self.get_ubicacion_edificio()}, Repisas: {self.get_repisa_edificio()}\n"
            file.write(info)

###Pallet###
inventario = [] #Aquí almacenaremos el inventario de las pallets

class Pallet:
    def __init__(self, id_pallet, id_cliente, id_edificio, fecha_ingreso, fecha_egreso=None): #Definimos el constructor junto con todos sus atributos principales
        self.__id_pallet = id_pallet
        self.id_cliente = id_cliente
        self.id_edificio=id_edificio
        self.fecha_ingreso=fecha_ingreso
        self.fecha_egreso=fecha_egreso


    def registrar_pallet(self):#Aquí se consiguen todos los datos de la pallet a ser registrada
        flag = True
        while flag:
            id_pallet = input("Ingresa el ID del pallet: ")
            id_cliente = input("Ingresa el cliente: ")
            id_edificio = input("Ingrese en el edificio que se encuentra: ")
            fecha_ingreso = input("Ingresar la fecha de entrada: ")
            pallet_nuevo = Pallet(id_pallet, id_cliente, id_edificio, fecha_ingreso)
            inventario.append(pallet_nuevo)
            pallet_nuevo.guardar_info()
            print("Pallet guardada existosamente!!")
            loopInput = input("¿Desea agregar otro pallet? (si/no): ")
            if loopInput.lower() != "si":
                flag = False


    def modificar_id_edificio(self, nuevo_edificio_id, lista_edificios):#Esta función recorre el arreglo de edificios y modifica el ID del edificio si se encuentra en el arreglo 
        self.id_edificio = nuevo_edificio_id
        if nuevo_edificio_id not in [edificio.__id_edificio for edificio in edificios]:
            print("El ID del edificio no es válido.")
        print("El ID del edificio se ha modificado exitosamente.")


    def validacion_pallet(self, id2):#Función que ayuda para validar la existencia de la pallet, recorriendo el arreglo y verificando el ID
        encontrado = False
        for pallet in inventario:
            if pallet.Pallet_id_pallet == id2:
                encontrado = True
                return "Producto encontrado!"
        if not encontrado:
            respuesta = input("Disponibilidad de pallet agotada. ¿Desea agregar un nuevo pallet? (si/no): ")
            if respuesta.lower() == 'si':
                cliente = input("Ingresa el cliente para el nuevo pallet: ")
                self.registrar_pallet()
            else:
                return "Hasta luego"


    def validar_edificio(self, id_edificio):#Función para validar la existencia del edificio buscado, a través del arreglo de edificios el ID
        for edificio in edificios:
            if edificio.getID() == id_edificio:
                return True
        return False


    def validar_cliente(self, id_cliente):#Funcíon para validar la existencia de un cliente en el arreglo, a través de la busqueda por ID
        for cliente in clientes:
            if cliente.getID() == id_cliente:
                return True
        return False


    def agregar_pallet(self, id_pallet, id_cliente, id_edificio):#Función para agregar la pallet al arreglo de pallets, mientras se verifica que no este repetido
        if self.validar_cliente(id_cliente) and self.validar_edificio(id_edificio):
            pallet_nuevo = Pallet(id_pallet, id_cliente, id_edificio, self.fecha_ingreso)
            inventario.append(pallet_nuevo)
            print(f"Pallet {id_pallet} agregado exitosamente.")
        else:
            print("Cliente o edificio inválido. No se pudo agregar el pallet.")
    
    def getPalletID(self):
        return self.__id_pallet

    def __eliminar_pallet(self, id_pallet):#Función para deshacerse de pallets que ya no sean necesarias, recorriendo el arreglo y buscando a través del ID
        for pallet in inventario:
            if pallet.getPalletID() == id_pallet:
                inventario.remove(pallet)
                print(f"Pallet con ID {id_pallet} eliminado.")
                break
            else:
                print("Pallet no encontrado. No se pudo eliminar.")


    def eliminar_pallet_publico(self, id_pallet):#Función para eliminar la pallet, esta es de uso público. Más que nada aquí se hace la acción de eliminar la pallet
        self.__eliminar_pallet(id_pallet)
    
    def guardar_info(self):
        with open('pallets.txt', 'a') as file:
            info = f"ID Pallet: {self.getPalletID()}, ID Cliente: {self.id_cliente}, ID Edificio: {self.id_edificio}, Fecha Ingreso: {self.fecha_ingreso}, Fecha Egreso: {self.fecha_egreso}\n"
            file.write(info)


###Cliente###
clientes=[]#Aquí almacenaremos los datos de los clientes.
class Cliente:
    def __init__(self, id_cliente, empresa, cliente_ingreso, nacionalidad):
        self.__id_cliente = id_cliente
        self.empresa = empresa
        self.cliente_ingreso = cliente_ingreso
        self.nacionalidad = nacionalidad
    
    def getID(self):
        return self.__id_cliente

    def crear_cliente(self):
        id_cliente = input("Ingresa el ID del cliente: ")
        empresa = input("Ingresa el nombre de la empresa: ")
        cliente_ingreso = input("Ingresa la fecha de ingreso del cliente: ")
        nacionalidad = input("Ingresa la nacionalidad del cliente: ")
        cliente_nuevo = Cliente(id_cliente, empresa, cliente_ingreso, nacionalidad)
        if id_cliente==self.__id_cliente:
            print("El cliente no se puede agregar cambiar el id")
        else: 
            clientes.append(cliente_nuevo)
            cliente_nuevo.guardar_info()
            print(f"Cliente {id_cliente} creado y guardado exitosamente.")

    def mostrar_info_cliente(self, id_cliente):
        for cliente in clientes:
            if cliente.__id_cliente == id_cliente:
                return f"ID: {cliente.__id_cliente}, Empresa: {cliente.empresa}, Fecha de Ingreso: {cliente.cliente_ingreso}, Nacionalidad: {cliente.nacionalidad}"
        return "Cliente no encontrado."

    def eliminar_cliente(self, id_cliente):
        for cliente in clientes:
            if cliente.__id_cliente == id_cliente:
                clientes.remove(cliente)
                print(f"Cliente con ID {id_cliente} eliminado.")
                return
        print("Cliente no encontrado. No se pudo eliminar.")
    
    def guardar_info(self):
        with open('clientes.txt', 'a') as file:
            info = f"ID Cliente: {self.getID()}, Empresa: {self.empresa}, Fecha de ingreso: {self.cliente_ingreso}, Nacionalidad: {self.nacionalidad}\n"
            file.write(info)


#Funcinones con todos los menús, conectados con su respectivo campo


def edificio_menu():
    
    repisa = 0
    ubicacion = 0
    id_edificio = 0
    
    while True:

        print("\n--- Menú de Gestión de Edificios ---")

        print(f"Hay actualmente {len(edificios)}")

        print("1. Crear Edificio")
        print("2. Eliminar Edificio")
        print("3. Mostrar Información de un Edificio")
        print("4. Volver al Menú Principal")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            Edificio(repisa, ubicacion, id_edificio).crear_edificio() 

        elif choice == '2':
            id_edificio = input("Ingrese el ID del edificio a eliminar: ")
            edificio = Edificio(repisa, ubicacion, id_edificio).buscar_edificio(id_edificio)
            edificio.eliminar_edificio()

        elif choice == '3':
            id_edificio = input("Ingrese el ID del edificio a consultar: ")
            edificio = Edificio(repisa, ubicacion, id_edificio).buscar_edificio(id_edificio)
            if edificio is None:
                print (f"Edificio {id_edificio} no encontrado.")
            
            else:
                info = edificio.obtener_info_edificio()
                print (f"Información del edificio: {info}")

        elif choice == '4':
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def pallet_menu():
    
    id_pallet = 0
    id_cliente = 0
    id_edificio = 0
    fecha_ingreso = 0
    
    while True:

        print("\n--- Menú de Gestión de Pallets ---")
        print("1. Registrar Pallet")
        print("2. Modificar Edificio de un Pallet")
        print("3. Eliminar Pallet")
        print("4. Volver al Menú Principal")
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            Pallet(id_pallet, id_cliente, id_edificio, fecha_ingreso).registrar_pallet()  
        elif choice == '2':
            id_pallet = input("Ingrese el ID del pallet a modificar: ")
            nuevo_edificio_id = input("Ingrese el nuevo ID del edificio para el pallet: ")
            pallet=Pallet(id_pallet, id_cliente, id_edificio, fecha_ingreso, fecha_egreso=None)
            if id_pallet is None:
                print("Pallet no encontrado")
            else:
                if nuevo_edificio_id in edificios:
                    pallet.modificar_id_edificio(nuevo_edificio_id, edificios)
        elif choice == '3':
            id_pallet = input("Ingrese el ID del pallet a eliminar: ")
            Pallet(id_pallet, id_cliente, id_edificio, fecha_ingreso).eliminar_pallet_publico(id_pallet)  
        elif choice == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def cliente_menu():
    id_cliente = 0
    empresa = 0
    cliente_ingreso = 0
    nacionalidad = 0

    while True:
        print("\n--- Menú de Gestión de Clientes ---")
        print("1. Crear Cliente")
        print("2. Mostrar Información de Cliente")
        print("3. Eliminar Cliente")
        print("4. Volver al Menú Principal")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            Cliente(id_cliente, empresa, cliente_ingreso, nacionalidad).crear_cliente()
        elif choice == '2':
            id_cliente = input("Ingrese el ID del cliente para mostrar información: ")
            cliente=Cliente(id_cliente, empresa, cliente_ingreso, nacionalidad)
            if cliente is None: 
                 print (f"Cliente {id_cliente} no encontrado.")
            else:
                info = cliente.mostrar_info_cliente(id_cliente)
                print (f"Información del cliente: {info}")
        elif choice == '3':
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            Cliente(id_cliente, empresa, cliente_ingreso, nacionalidad).eliminar_cliente(id_cliente)
        elif choice == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

#MAIN
while True:

    print("\n--- Menú Principal de la WareHouse ---")
    print("1. Edificios")
    print("2. Pallets")
    print("3. Clientes")
    print("4. Salir")
    choice = input("Seleccione una opción: ")
       
    if choice == '1':
        edificio_menu()
    elif choice == '2':
        pallet_menu()
    elif choice == '3':
        cliente_menu()
    elif choice == '4':
        print("Gracias por usar el sistema. Hasta luego.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")