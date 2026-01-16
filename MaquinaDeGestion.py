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
    e1 = Entidad("igna", "igna@gmail.com") 
    c1 = Cliente ("Ales", "Aless@gmail.com", 12)
    p1 = Proveedor("HAHA", "HAHA@gmail","ahah")

    e1.mostrar()

    c1.mostrarC()

    p1.mostrarP()

