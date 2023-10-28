# Funciones con atributos


class Persona:
    def __init__(self):
        self.nombre = "Axel"
        self.edad = 20
        self.pais = "Mexico"


Personite = Persona()
print(Personite.nombre)
print(Personite.edad)
print(Personite.pais)

setattr(Personite, "nombre", "Yeray")
print(Personite.nombre)
