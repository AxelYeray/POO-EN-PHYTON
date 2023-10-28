#f-strins
#format %

class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __repr__(self):
        return f'{self.nombre} {self.apellido} {self.edad}'
    
nuevo_estudiante = Estudiante('Juan', 'Perez', 20)
print(f"{nuevo_estudiante !r}")