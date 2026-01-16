import sqlite3
import os


#busqué el codigo para el guardado en base de datos
RUTA_DB = os.path.join(os.path.dirname(__file__), "contactos.db")

#Aqui inicia la Base de Datos
def conectar_db():
    return sqlite3.connect(RUTA_DB)

def crear_tablas():
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT,
        credito REAL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS proveedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT,
        nombre_comercial TEXT
    )
    """)

    conn.commit()
    conn.close()
    
    
#Fin de la base de datos

#Aqui defino las clases
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

    def guardar_db(self):
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, email, credito) VALUES (?, ?, ?)",
            (self.nombre, self.email, self.credito)
        )
        conn.commit()
        conn.close()


class Proveedor(Entidad):
    def __init__(self, nombre, email, nombre_comercial):
        super().__init__(nombre, email)
        self.nombre_comercial = nombre_comercial

    def mostrarP(self):
        super().mostrar()
        print(f"Su nombre comercial es: {self.nombre_comercial}")

    def guardar_db(self):
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO proveedores (nombre, email, nombre_comercial) VALUES (?, ?, ?)",
            (self.nombre, self.email, self.nombre_comercial)
        )
        conn.commit()
        conn.close()


#Aqui la funciones principales

def mostrar_clientes():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, email, credito FROM clientes")
    filas = cursor.fetchall()
    conn.close()

    if not filas:
        print("No hay clientes registrados.")
    else:
        for nombre, email, credito in filas:
            Cliente(nombre, email, credito).mostrarC()

def mostrar_proveedores():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, email, nombre_comercial FROM proveedores")
    filas = cursor.fetchall()
    conn.close()

    if not filas:
        print("No hay proveedores registrados.")
    else:
        for nombre, email, nombre_comercial in filas:
            Proveedor(nombre, email, nombre_comercial).mostrarP()

#Aqui empieza el main
if __name__ == "__main__":
    
    #clientes = []
    #proveedores = []

    # Ejemplos iniciales
    #e1 = Entidad("igna", "igna@gmail.com")
    #c1 = Cliente("Ales", "Aless@gmail.com", 12)
    #p1 = Proveedor("HAHA", "HAHA@gmail.com", "ahah")

    #e1.mostrar()
    #c1.mostrarC()
    #p1.mostrarP()

    crear_tablas()

    while True:
        print("\nMenú de la Base de Datos")
        print("1 - Gestionar Cliente")
        print("2 - Gestionar Proveedor")
        print("3 - Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            while True:
                print("\nMenú de Cliente")
                print("1 - Crear Cliente")
                print("2 - Mostrar Clientes")
                print("3 - Volver")

                opcionc = input("Elige una opción: ")

                if opcionc == "1":
                    nombre = input("Nombre: ")
                    email = input("Email: ")
                    credito = float(input("Crédito: "))
                    cliente = Cliente(nombre, email, credito)
                    cliente.guardar_db()
                    print("Cliente guardado en la base de datos.")

                elif opcionc == "2":
                    mostrar_clientes()

                elif opcionc == "3":
                    break

                else:
                    print("Opción no válida.")

        elif opcion == "2":
            while True:
                print("\nMenú de Proveedor")
                print("1 - Crear Proveedor")
                print("2 - Mostrar Proveedores")
                print("3 - Volver")

                opcionp = input("Elige una opción: ")

                if opcionp == "1":
                    nombre = input("Nombre: ")
                    email = input("Email: ")
                    nombre_comercial = input("Nombre comercial: ")
                    proveedor = Proveedor(nombre, email, nombre_comercial)
                    proveedor.guardar_db()
                    print("Proveedor guardado en la base de datos.")

                elif opcionp == "2":
                    mostrar_proveedores()

                elif opcionp == "3":
                    break

                else:
                    print("Opción no válida.")

        elif opcion == "3":
            print("¡ADIOS!")
            break

        else:
            print("Opción no válida.")