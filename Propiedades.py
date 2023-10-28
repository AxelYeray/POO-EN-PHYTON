#propiedades()
class Empleado:
  def __init__(self,nombre,salario):
    self.__nombre = nombre
    self.__salario = salario

    def __getNombre(self):
      return self.__nombre
    
    def __getSalario(self):
        return self.__salario
    
    def __setNombre(self,nombre):
        self.__nombre = nombre

    def __setSalario(self,salario):
        self.__salario = salario

    def __delNombre(self):
        del self.__nombre

    def __delSalario(self):
        del self.__salario

    nombre = property(fget=__getNombre,
                      fset =__setNombre,
                      fdel=__delNombre,
                      doc="Soy la propiedad 'nombre'")

    salario = property(fget=__getSalario)

empleado_uno = Empleado('Juan',1000)
empleado_uno.nombre = 'Juan Carlos'
print(empleado_uno.nombre,empleado_uno.salario)
help(empleado_uno)
