class Nave():

    def __init__(self, piloto, velocidad=0):

        self._piloto = (input("Introduce un nombre de piloto: "), int(input("Introduce la habilidad de piloto: ")))


    def accelerar(self):

        while True:
            self._velocidad = int(input("Introduce la velocidad inicial entre 0 y 100: "))
            if self._velocidad > 0 and self._velocidad < 100:
                break

        acceleracion = int(input("Introduce un porcentaje de acceleración: "))

        if self._velocidad == 0 and acceleracion > 0:
            self._velocidad += 1
            self._velocidad += (int(self._velocidad) * acceleracion) /100
        elif acceleracion < 0:
            self._velocidad = self._velocidad
        
        return self._velocidad


    def frenar(self):

        frenar = int(input("Introduce el porcentaje de frenada: "))

        self._velocidad -= (int(self._velocidad) * frenar)/100

        return self._velocidad


    def velocidad_en_combate(self):

        self._velocidad = self._velocidad * self._piloto[1]
    
        return self._velocidad



class Flota():


    def __init__(self, flota=[]):

        cantidad_naves = int(input("Introduce la cantidad de naves a crear: "))

        for i in range(cantidad_naves):
            flota.append(Nave(()))
        
        self._flota = flota
            
            

########################| C O N T R U C T O R |########################
equipo1 = Flota()

equipo1._flota[0].accelerar()
equipo1._flota[0].frenar()
print(equipo1._flota[0]._velocidad)









