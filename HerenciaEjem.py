#Herencia ejemeplo practico

class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [ 0 for i in range(numero)]

    def ingresarDato(self):
        self.datos = [ int(input('ingresar datos ' + str(i+1)+ '= ')) for i in range(self.n)] 


class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
     a,b, = self.datos
     s = a+b
     print('el resultado es: ', s)  

    def resta(self):
     a,b, = self.datos
     s = a-b
     print('el resultado es: ', s) 



class raiz(Calculadora):
   def __init__(self):
        Calculadora.__init__(self,1)

   def cuadrada(self):
      import math
      a, = self.datos
      print('el resultado es: ', math.sqrt(a))


objeto = Op_basicas()
print(isinstance(objeto,Op_basicas))
     