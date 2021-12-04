import random
import time


class Planta():

    def __init__(self, vida, ataque, movimiento):

        self._vida = vida
        self._ataque = ataque
        self._movimiento = movimiento

    def atacar(self):
                
        self._danyo = self._ataque + random.randrange(-1,6)
        return self._danyo

    def restar_vida(self, dato):

        self._vida -= dato

        return self._vida


class Zombie():

    def __init__(self, vida, ataque, movimiento):

        self._vida = vida
        self._ataque = ataque
        self._movimiento = movimiento
    
    def atacar(self):
        
        self._danyo = self._ataque + random.randrange(-1,19)
        return self._danyo

    def restar_vida(self, dato):

        self._vida -= dato

        return self._vida


###########################################################
                        # PROGRAMA #
###########################################################

planta = Planta(30,5,0)
zombie = Zombie(80,5,2)

distancia = 18

while True:
    time.sleep(0)
    danyo_planta = planta.atacar()
    danyo_zombie = zombie.atacar()
    vida_planta = planta._vida
    vida_zombie = zombie._vida
    print("Empieza el turno")
    print()

    if  danyo_planta < 0:
        print()
        print("El ataque de {} ha fallado!".format("PLANTA"))
    else:
        print()
        print("El ataque de {} hace {} de daño".format("PLANTA",danyo_planta))
        vida_zombie = zombie.restar_vida(danyo_planta)
        print("Al ZOMBIE le quedan {} de vida".format(vida_zombie))


    if distancia > 1:
        distancia -= zombie._movimiento
    else:
        print("¡El Zombie ataca a la planta!")
        if  danyo_zombie <= 0:
            print()
            print("El ataque de {} ha fallado!".format("ZOMBIE"))
        else:
            print()
            print("El ataque de {} hace {} de daño".format("ZOMBIE",danyo_zombie))
            vida_planta = planta.restar_vida(danyo_zombie)
                    
    if vida_planta <= 0:
        print()
        print("La PLANTA ha muerto!!!")
        break
    elif vida_zombie <= 0:
        print()
        print("El ZOMBIE ha muerto!!!")
        break



    print("PLANTA - |"+"_"*distancia+"| - ZOMBIE")