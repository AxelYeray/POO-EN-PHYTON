#Clase y estático

class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes
        self.tamaño = tamaño 

    def __repr__(self):
        return (f'Pastel({self.ingredientes}, 'f'{self.tamaño})')
    
    def area(self):
        return self.tamaño_area(self.tamaño)
    
    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi
    
nuevo_pastel = Pastel(['harina','leche','azucar','crema'],4)
print(nuevo_pastel.ingredientes)
        

  