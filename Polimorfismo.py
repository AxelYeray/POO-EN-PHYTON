#Polimorfismo

class Animales:
    def __init__(self, nombre):
        self.nombre = nombre

    def tipoAnimal(self):
        pass

class Leon(Animales):
    def tipoAnimal(self):
        print('animal salvaje')

class perro(Animales):
    def tipoAnimal(self):
        print('Animal domestico')

nuevo_animal = Leon('Simba')
nuevo_animal.tipoAnimal()

nuevo_animal = perro('Firulais')
nuevo_animal.tipoAnimal()