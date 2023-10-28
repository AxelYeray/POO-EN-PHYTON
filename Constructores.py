# Constructores en Python


class Persona:
    pass

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return "{} tiene {} años".format(self.nombre, self.edad)

    def frase(self, frase):
        return "{} dice: {}".format(self.nombre, frase)


Victor = Persona("Victor", 20)
print(Victor.saludar())
print(Victor.frase("Hola mundo"))
