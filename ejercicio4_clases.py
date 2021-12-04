"""
Escribe una clase Estudiante que incluya atributos para dni, nombre, grupo y notas. El atributo notas será un diccionario en el que las claves son los nombres de las asignaturas y los valores listas con las notas de esa asignatura. Concretamente:

a- Escribe un constructor que reciba el dni, nombre y grupo, e inicialice los atributos correspondientemente con esos valores. Las notas debenrán inicializarse a un diccionario vacío.
"""


class Estudiante():
    
    def __init__(self, dni, nombre, grupo):

        self._dni = dni
        self._nombre = nombre
        self._grupo = grupo
        self._notas = {}
    

    def __str__(self):
        return "· Nombre: {}\n· DNI: {}\n· Grupo: {}\n· Notas: {}".format(self._nombre, self._dni, self._grupo, self._notas)


######## Metodos SET ##########

    def setMatricula(self, asignatura):

        if asignatura in self._notas:
            return False
        else:
            self._notas[asignatura] = []
            return True
    

######## Mas funcionalidades ##########

    def ponerNota(self):

        nom_asig = input("Introduce el nombre de la asignatura: ").upper()
        nota_asig = float(input("Introduce la nota de la asignatura: "))

        if nom_asig in self._notas:
            self._notas[nom_asig].append(nota_asig)
            return True

        else:
            self._notas[nom_asig] = [nota_asig]
            return False


    def notaMedia(self, asignatura):
        print(self._notas[asignatura])

        if asignatura in self._notas and len(self._notas[asignatura]) > 0:
            suma = sum(self._notas[asignatura])/len(self._notas[asignatura])
            return "La nota media de {} es: {}".format(asignatura,suma)
        else:
            return None
    
    def Asignatura(self,nombre_asig):

        self._nombre_asig = nombre_asig
        

    


####################################| PRUEBA DE OBJETOS |####################################

jose = Estudiante("29211482-x", "jose manuel", "b")

jose.setMatricula("bbdd")
jose.setMatricula("eedd")
jose.ponerNota()
jose.ponerNota()
jose.ponerNota()
jose.ponerNota()

print(jose.notaMedia("BBDD"))

###############################################################################################
