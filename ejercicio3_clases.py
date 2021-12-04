"""
Crearemos una supeclase llamada Electrodomestico con las siguientes características:

Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso. Indica que se podrán heredar.
Por defecto, el color sera blanco, el consumo energético sera F, el precioBase es de 100 € y el peso de 5 kg. Usa constantes para ello.
Los colores disponibles son blanco, negro, rojo, azul y gris. No importa si el nombre esta en mayúsculas o en minúsculas.
Los constructores que se implementaran serán
Un constructor por defecto.
Un constructor con el precio y peso. El resto por defecto.
Un constructor con todos los atributos.
Los métodos que implementara serán:
Métodos get de todos los atributos.
comprobarConsumoEnergetico(char letra): comprueba que la letra es correcta, sino es correcta usara la letra por defecto. Se invocara al crear el objeto y no sera visible.
comprobarColor(String color): comprueba que el color es correcto, sino lo es usa el color por defecto. Se invocara al crear el objeto y no sera visible.
precioFinal(): según el consumo energético, aumentara su precio, y según su tamaño, también. Esta es la lista de precios:
                               
                               
                                LETRA	PRECIO
                                    A	100 €
                                    B	80 €
                                    C	60 €
                                    D	50 €
                                    E	30 €
                                    F	10 €


TAMAÑO	PRECIO
Entre 0 y 19 kg	10 €
Entre 20 y 49 kg	50 €
Entre 50 y 79 kg	80 €
Mayor que 80 kg	100 €Crearemos una subclase llamada Lavadora con las siguientes características:
Su atributo es carga, ademas de los atributos heredados.
Por defecto, la carga es de 5 kg. Usa una constante para ello.
Los constructores que se implementaran serán:
Un constructor por defecto.
Un constructor con el precio y peso. El resto por defecto.
Un constructor con la carga y el resto de atributos heredados. Recuerda que debes llamar al constructor de la clase padre.
Los métodos que se implementara serán:
Método get de carga.
precioFinal():, si tiene una carga mayor de 30 kg, aumentara el precio 50 €, sino es así no se incrementara el precio. Llama al método padre y añade el código necesario. Recuerda que las condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio.
Crearemos una subclase llamada Television con las siguientes características:

Sus atributos son resolución (en pulgadas) y sintonizador TDT (booleano), ademas de los atributos heredados.
Por defecto, la resolución sera de 20 pulgadas y el sintonizador sera false.
Los constructores que se implementaran serán:
Un constructor por defecto.
Un constructor con el precio y peso. El resto por defecto.
Un constructor con la resolución, sintonizador TDT y el resto de atributos heredados. Recuerda que debes llamar al constructor de la clase padre.
Los métodos que se implementara serán:
Método get de resolución y sintonizador TDT.
precioFinal(): si tiene una resolución mayor de 40 pulgadas, se incrementara el precio un 30% y si tiene un sintonizador TDT incorporado, aumentara 50 €. Recuerda que las condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio.
Ahora crea una clase ejecutable que realice lo siguiente:

Crea un array de Electrodomesticos de 10 posiciones.
Asigna a cada posición un objeto de las clases anteriores con los valores que desees.
Ahora, recorre este array y ejecuta el método precioFinal().
Deberás mostrar el precio de cada clase, es decir, el precio de todas las televisiones por un lado, el de las lavadoras por otro y la suma de los Electrodomesticos (puedes crear objetos Electrodomestico, pero recuerda que Television y Lavadora también son electrodomésticos). Recuerda el uso operador instanceof.
Por ejemplo, si tenemos un Electrodomestico con un precio final de 300, una lavadora de 200 y una televisión de 500, el resultado final sera de 1000 (300+200+500) para electrodomésticos, 200 para lavadora y 500 para televisión.
"""

class Electrodomestico():


    def __init__(self, color="Blanco", consumoEnergetico="f", precioBase=100, peso=5):

        CONSUMO = "ABCDEF".lower()
        COLORES = ["blanco","negro","rojo","azul","gris"]

        if consumoEnergetico not in CONSUMO:
            self._consumoEnergetico = "f".upper()
        else:
            self._consumoEnergetico = consumoEnergetico.upper()
        
        if color not in COLORES:
            self._color = "Blanco".capitalize()
        else:
            self._color = color.capitalize()

        self._precioBase = precioBase
        self._peso = peso

    def __str__(self):
        return "\n##########| Características |##########\n\n· Color: {}\n· Consumo Energético: {}\n· Precio base: {} €\n· Peso: {} Kg".format(self._color,self._consumoEnergetico,self._precioBase,self._peso)

    
######## Metodos GET ##########

    def getColor(self):
        return self._color
    

    def getConsumo(self):
        return self._consumoEnergetico
    

    def getPeso(self):
        return self._peso


    def setPeso(self):
        return self._peso


######## Metodos SET ##########

    def setColor(self, color):

        COLORES = ["blanco","negro","rojo","azul","gris"]

        if color not in COLORES:
            self._color = "blanco"
        else:
            self._color = color
        
        return self._color


    def setConsumo(self, consumoEnergetico):
        
        CONSUMO = "ABCDEF"

        if consumoEnergetico not in CONSUMO:
            self._consumoEnergetico = "F"
        else:
            self._consumoEnergetico = consumoEnergetico

        return self._consumoEnergetico
    

    def setPrecio(self, precio):

        self._precioBase = precio

        return self._precioBase


    def setPeso(self, peso):
        
        self._peso
        return self._peso


######## Mas funcionalidades ##########

    def precioFinal(self):

        preciofinal = {"A":100,"B":80,"C":60,"D":50,"E":30,"F":10}
        tamaño = {20:10,50:50,80:80}

        if self._peso < 20:
            self._precioBase += tamaño[20] + preciofinal[self._consumoEnergetico]
        elif self._peso < 50:
            self._precioBase += tamaño[50] + preciofinal[self._consumoEnergetico]
        elif self._peso < 80:
            self._precioBase += tamaño[80] + preciofinal[self._consumoEnergetico]
        else:
            self._precioBase += 100 + preciofinal[self._consumoEnergetico]

        return self._precioBase

    def características(self):

        print("El color es:",self._color,"\nLa calificación energética es:",self._consumoEnergetico,"\nEl precio base es:",self._precioBase,"€\nEl peso es:",self._peso,"Kg")



################################ SUBCLASE LAVADORA ##################################

class Lavadora(Electrodomestico):

    def __init__(self, carga=5, color="Blanco", consumoEnergetico="f", precioBase=100, peso=5):
        
        super().__init__(color, consumoEnergetico, precioBase, peso)
        
        self._carga = carga
    

    def __str__(self):

        return super().__str__() + "\n· Capacidad de carga: {}".format(self._carga)


######## Metodos GET Subclase Lavadora ##########

    def getCarga(self):
        return self._carga
    

######## Metodos SET Subclase Lavadora ##########

    def setCarga(self, carga=0):

        carga = int(input("Introduce los KG de carga: "))

        self._carga = carga

        return self._carga

    
    def precioFinal(self):

        super().precioFinal()

        if self._carga > 30:
            self._precioBase += 50

        return self._precioBase


    def características(self):

        super().características()

        print("La carga que admite es de:",self._carga,"Kg")



################################ SUBCLASE TELEVISION ##################################

class Television(Electrodomestico):

    def __init__(self, sintonizadorTDT, resolucion="20", color="Blanco", consumoEnergetico="f", precioBase=100, peso=5):
        
        super().__init__(color, consumoEnergetico, precioBase, peso)
        
        self._resolucion = resolucion
        self._sintonizadorTDT = sintonizadorTDT
        

    def __str__(self):

        return super().__str__() + "\n· ¿Tiene sintonizador?: {} \n· Resolucion: {} pulgadas".format(self._sintonizadorTDT, self._resolucion)


######## Metodos GET Subclase Television ##########


    def getResolucion(self):
        return self._resolucion


    def getSintonizadorTDT(self):
        return self._sintonizadorTDT
    

######## Metodos SET Subclase Television ##########


    def setResolucion(self, resolucion):

        self._resolucion = resolucion

        return self._resolucion
    

    def setSintonizadorTDT(self, sintonizador):

        self._sintonizadorTDT = sintonizador

        return self._sintonizadorTDT


    def precioFinal(self):

        super().precioFinal()

        if self._resolucion > 40:

            self._precioBase += ((self._precioBase*30)/100)

        elif self._resolucion > 40 and self._sintonizadorTDT == True:

            self._precioBase += ((self._precioBase*30)/100) + 50

        return self._precioBase


    def características(self):

        super().características()

        print("El Televisor dispone de TDT:",self._sintonizadorTDT,"\nEl tamaño es de:",self._resolucion,"pulgadas.")




####################################| PRUEBA DE OBJETOS |####################################

print("|------------------- Lavadoras -------------------|")

print()
lavadora1 = Lavadora(8,"rojo","a",250,10)
lavadora1.setCarga(31)
lavadora1.características()
print()

print("|------------------- Televisores -------------------|")

print()
television1 = Television(False,42,"negro","b",350,6)
television1.precioFinal()
television1.características()
print()

###############################################################################################

"""
·Crea un array de Electrodomesticos de 10 posiciones.
·Asigna a cada posición un objeto de las clases anteriores con los valores que desees.
·Ahora, recorre este array y ejecuta el método precioFinal().
·Deberás mostrar el precio de cada clase, es decir, el precio de todas las televisiones por un lado, el de las lavadoras por otro y la suma de los Electrodomesticos (puedes crear objetos Electrodomestico, pero recuerda que Television y Lavadora también son electrodomésticos). Recuerda el uso operador instanceof.
"""

lista_electrodomesticos = []

for j in range(5):
    lista_electrodomesticos.append(Television(False,42,"negro","b",350,6))
    lista_electrodomesticos.append(Lavadora(8,"rojo","a",250,10))


print(lista_electrodomesticos[1])
print(lista_electrodomesticos[2])

