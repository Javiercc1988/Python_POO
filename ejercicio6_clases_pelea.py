import random
from playsound import playsound
import time

class Guerrero():


    def __init__(self, nombre, vida, fuerza, precision, velocidad, defensa):

        self._nombre = nombre
        self._vida = vida
        self._fuerza = fuerza
        self._precision = precision
        self._velocidad = velocidad
        self._defensa = defensa

    def __str__(self):
        return "· Nombre: {}\n· Vida: {}\n· Fuerza: {}\n· Precision: {}\n· Velocidad: {}\n· Defensa: {}\n".format(self._nombre, self._vida, self._fuerza, self._precision, self._velocidad, self._defensa)

    
    def golpear(self, g):

        if (0) <= (self._precision - g._velocidad) / 100:
            daño = max(self._fuerza - g._defensa + random.randrange(-10,11),1)
            print("El luchador {} hace {} de daño!".format(self._nombre, daño))
            print("A {} le quedan {} puntos de vida.".format(g._nombre,g._vida))
            print()
            g._vida -= daño
        else:
            print("El luchador {} ha esquivado el golpe.".format(g._nombre))


goku = Guerrero("Goku",100,10,12,9,0)
superman = Guerrero("SupermaN",100,12,10,10,0)
Cnorrys = Guerrero("Chuck Norrys",100,12,10,12,9)
Thor = Guerrero("Chuck Norrys",100,12,10,12,9)

dicc = {"Goku":Guerrero("Goku",100,10,12,9,0),"superman":Guerrero("SupermaN",100,10,12,3,0),"Thor":Guerrero("Thor",100,10,12,5,0)}

# for i in range (3,0,-1):
#     print(i)
#     playsound(str(i)+".mp3")
#     time.sleep(0.7)

# playsound("double_dragon_arcade_1987_titile.mp3", False)

luchador1 = dicc[random.choice(list(dicc.keys()))]
print(luchador1._velocidad)
luchador2 = dicc[random.choice(list(dicc.keys()))]

while True:
    time.sleep(2)

    if luchador1._velocidad < luchador2._velocidad:
        print("golpe1")

        luchador1.golpear(luchador2)
        luchador2.golpear(luchador1)
        
        print("golpe1")

    elif luchador1._velocidad > luchador2._velocidad:
        print("golpe2")

        luchador2.golpear(luchador1)
        luchador1.golpear(luchador2)

        print("golpe2")
    # if goku._velocidad < superman._velocidad:
    #     time.sleep(2)
    #     goku.golpear(superman)
    #     superman.golpear(goku)

    # if goku._vida < 0 or superman._vida < 0:
    #     if goku._vida <= 0:
    #         print("************************************")
    #         print("Superman gana la pelea, Goku pierde!")
    #         print("************************************")

    #     elif superman._vida <= 0:
    #         print("*************************************")
    #         print("Goku gana la pelea!, SupermaN pierde!")
    #         print("*************************************")
    #     break
    # else:
    #     continue