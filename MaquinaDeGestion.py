import sqlite3

class Entidad:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(f"\nNombre de la Entidad: {self.nombre}")
        print(f"Email de la Entidad: {self.email}")

class Cliente(Entidad):
    def __init__(self, nombre, email, credito):
        super().__init__(nombre, email)
        self.credito = credito

    def mostrarC(self):
        super().mostrar()
        print(f"Su crédito es de {self.credito}€")

class Proveedor(Entidad):
    def __init__(self, nombre, email, nombre_comercial):
        super().__init__(nombre, email)
        self.nombre_comercial = nombre_comercial

    def mostrarP(self):
        super().mostrar()
        print(f"Su nombre comercial es: {self.nombre_comercial}")

if __name__ == "__main__":
    clientes = []
    proveedores = []

    # Ejemplos iniciales
    e1 = Entidad("igna", "igna@gmail.com")
    c1 = Cliente("Ales", "Aless@gmail.com", 12)
    p1 = Proveedor("HAHA", "HAHA@gmail.com", "ahah")

    e1.mostrar()
    c1.mostrarC()
    p1.mostrarP()

    while True:
        print("\nMenú de la Base de Datos.")
        print("1 - Gestionar Cliente")
        print("2 - Gestionar Proveedor")
        print("3 - Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            while True:
                print("\nMenú de Cliente.")
                print("1 - Crear Cliente")
                print("2 - Mostrar Clientes")
                print("3 - Volver al menú principal")

                opcionc = input("Elige una opción de Cliente: ")

                if opcionc == "1":
                    nombre = input("Nombre del cliente: ")
                    email = input("Email del cliente: ")
                    credito = float(input("Crédito del cliente: "))
                    nuevo_cliente = Cliente(nombre, email, credito)
                    clientes.append(nuevo_cliente)
                    print("Cliente creado exitosamente.")
                elif opcionc == "2":
                    if not clientes: 
                        print("No hay clientes registrados.")
                        #he buscado como volver hacia atras, me ha parecido interesante ponerlo
                    else:
                        for c in clientes:
                            c.mostrarC()
                elif opcionc == "3":
                    break
                else:
                    print("Opción no válida, intenta de nuevo.")

        elif opcion == "2":
            while True:
                print("\nMenú de Proveedor.")
                print("1 - Crear Proveedor")
                print("2 - Mostrar Proveedores")
                print("3 - Volver al menú principal")

                opcionp = input("Elige una opción de Proveedor: ")

                if opcionp == "1":
                    nombre = input("Nombre del proveedor: ")
                    email = input("Email del proveedor: ")
                    nombre_comercial = input("Nombre comercial: ")
                    nuevo_proveedor = Proveedor(nombre, email, nombre_comercial)
                    proveedores.append(nuevo_proveedor)
                    print("Proveedor creado exitosamente.")
                elif opcionp == "2":
                    if not proveedores:
                        print("No hay proveedores registrados.")
                    else:
                        for p in proveedores:
                            p.mostrarP()
                elif opcionp == "3":
                    break
                else:
                    print("Opción no válida, intenta de nuevo.")

        elif opcion == "3":
            print("¡ADIOS!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
