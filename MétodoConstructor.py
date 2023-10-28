# Metodo constructor
# Modificar un atributo de una clase
class Email:
    def __init__(self):
        self.enviado = False

    def enviar_correo(self):
        self.enviado = True


mail = Email()
print(mail.enviado)
mail.enviar_correo()
print(mail.enviado)
