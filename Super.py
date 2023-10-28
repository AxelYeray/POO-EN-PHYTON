#Metodo super()

class Mamifero():
    def __init__(self,nombre):
        print(nombre,'Es un animal de sangre caliente')

class Leon(Mamifero):  
    def __init__(self):
        print('El león es un animal de sangre caliente')
        super().__init__('simba') #Llama al constructor de la clase padre

nuevio_leon = Leon()
print(nuevio_leon)