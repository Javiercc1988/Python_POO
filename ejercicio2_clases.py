from random import randint
"""
Haz una clase llamada Password que siga las siguientes condiciones:

Que tenga los atributos longitud y contraseña . Por defecto, la longitud sera de 8.


Un constructor con la longitud que nosotros le pasemos. Generara una contraseña aleatoria con esa longitud.
Los métodos que implementa serán:
esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener mas de 2 mayúsculas, mas de 1 minúscula y mas de 5 números.
generarPassword():  genera la contraseña del objeto con la longitud que tenga.
Método get para contraseña y longitud.
Método set para longitud.
Ahora, crea una clase clase ejecutable:

Crea un array de Passwords con el tamaño que tu le indiques por teclado.
Crea un bucle que cree un objeto para cada posición del array.
Indica también por teclado la longitud de los Passwords (antes de bucle).
Crea otro array de booleanos donde se almacene si el password del array de Password es o no fuerte (usa el bucle anterior).
Al final, muestra la contraseña y si es o no fuerte (usa el bucle anterior). Usa este simple formato:

contraseña1 valor_booleano1
contraseña2 valor_bololeano2
"""


class Password():


    def __init__(self, contrasenya, longitud=8):
        self.longitud = longitud
        self.contrasenya = contrasenya


    def __str__(self):
        return "{}".format(self.contrasenya)


    def getPassword(self):
        return [self.longitud, self.contrasenya]


    def setPassword(self, longitud):
       
        abecedario = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, V, W, X, Y, Z, 1, 2, 3, 4, 5, 6, 7, 8, 9, *, -, +, /, $, %, &".split(",")

        nueva_contrasenya = ""

        for i in range(longitud):
            nueva_contrasenya += abecedario[randint(0, len(abecedario)-1)]

        self.longitud = longitud
        self.contrasenya = nueva_contrasenya
      
        return self.contrasenya


    def esFuerte(self):

        mayuscula = 0
        minuscula = 0
        numeros = 0

        for i in self.contrasenya:
            if i.isupper():
                mayuscula += 1

            elif i.islower():
                minuscula += 1

            elif i.isdigit():
                numeros += 1

        return (mayuscula > 1 and minuscula > 1 and numeros > 1)
        

    def generarPassword(self):
        abecedario = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, V, W, X, Y, Z, 1, 2, 3, 4, 5, 6, 7, 8, 9, *, -, +, /, $, %, &".split(",")

        nueva_contrasenya = ""

        for i in range(self.longitud):
            nueva_contrasenya += abecedario[randint(0, len(abecedario)-1)]

        self.contrasenya = nueva_contrasenya
        
        return self.contrasenya



####################################| PRUEBA DE OBJETOS |####################################|

contraseña1 = Password("ABCac12356",10)
print("Generamos un password indicandole la longitud que queramos:")
print(contraseña1.setPassword(23))
print("\nComprobamos si es fuerte:")
print(contraseña1.esFuerte())
print("\nGeneramos un password random con la longitud establecida.")
print(contraseña1.generarPassword())
print("\nComprobamos si es fuerte el nuevo password generado random:")
print(contraseña1.esFuerte())
print()
print("#####################################################################################")

passwords_fuertes = []

cantidad_de_passwords = int(input("Introduce la cantidad de password que quieres generar: "))
longitud_de_passwords = int(input("Introduce la longitud de las contraseñas: "))
contraseña = [i for i in range (cantidad_de_passwords)]


for i in range((cantidad_de_passwords)-1):
    contraseña[i] = Password("12345",longitud_de_passwords)
    contraseña[i].generarPassword()
    passwords_fuertes.append(contraseña[i].esFuerte())
    print("La contraseña es: ",contraseña[i],"\n¿Es fuerte?:",passwords_fuertes[i])