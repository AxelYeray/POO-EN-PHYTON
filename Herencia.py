#Herencia

class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return "{} es un pokemon de tipo {}".format(self.nombre, self.tipo)

class pikachu (Pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

class charmander (Pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, self.tipo, self.ataque) 
    
    nuevo_pokemon = pikachu('boby', 'electrico')
    print(nuevo_pokemon.descripcion())
    print(nuevo_pokemon.ataque('impactrueno'))
