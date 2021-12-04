""" 
· Crear una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad (puede tener decimales).
El titular sera obligatorio y la cantidad es opcional. Crea dos constructores que cumpla lo anterior.
Crea sus métodos get, set y str.

Tendrá dos metodos especiales:
· Ingresar(double cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
· Retirar(doble cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0.
"""

class Cuenta():
    

    def __init__(self, nombre_cuenta, titular, cantidad = 0.0):

        self.nombre_cuenta = nombre_cuenta
        self.titular = titular
        self.cantidad = cantidad


    def getCuenta (self):
        return [self.titular, self.cantidad]


    def setCuenta (self, titular, cantidad = None):
        self.titular = titular
        if cantidad != None:
            self.cantidad = cantidad
    

    def datos_cuenta(self):
        return "Esta es la cuenta nº: " + self.nombre_cuenta + "\nNombre del titular: " + self.titular + "\nCantidad actual en la cuenta: " + str(self.cantidad)


    def ingreso(self, cantidad_ingresada):

        if cantidad_ingresada > 0.0:
            self.cantidad += cantidad_ingresada
        else:
            print("La cantidad ingresada es menor o igual a 0, no se realizará ninguna acción.")
        

    def retirada(self, cantidad_retirada):
        
        if self.cantidad - cantidad_retirada >= 0.0:
            self.cantidad -= cantidad_retirada

        else:
            self.cantidad = 0.0
            print("La cantidad a retirar es inferior a 0, no se realizará operacion")




cliente1 = Cuenta("Cuenta1", "DiscoDurodeRoes")
cliente2 = Cuenta("Cuenta2", "Fernando", 300)

## Ingresamos dinero en las cuentas

cliente1.ingreso(300)
cliente2.ingreso(400)

## Retiramos dinero de las cuentas

cliente1.retirada(500)
cliente2.retirada(100)

## Muestro la informacion de las cuentas
print()
print(cliente1.datos_cuenta())
print()
print(cliente2.datos_cuenta())
print()