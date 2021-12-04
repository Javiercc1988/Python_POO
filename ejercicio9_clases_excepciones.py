class HamburguesaError(Exception):

    def __init__(self, hamburguesa, mensaje):
        super().__init__(mensaje)
        self.hamburguesa = hamburguesa


class Demasiadoquesoerror(HamburguesaError):
    def __init__(self, queso, hamburguesa, mensaje):
        super().__init__(hamburguesa, mensaje)
        self.queso = queso


class SehaquemadoError(HamburguesaError):

    def __init__(self, temperatura, hamburguesa, mensaje):
        super().__init__(hamburguesa, mensaje)
        self.temperatura = temperatura


class TipodepanError(HamburguesaError):

    def __init__(self, tipodepan, hamburguesa, mensaje):
        super().__init__(hamburguesa, mensaje)
        self.tipodepan = tipodepan


def crea_hamburguesa(hamburguesa, temperatura, queso, tipodepan):
    if hamburguesa not in ["cheeseburguer","baconburguer","soloburguer"]:
        raise HamburguesaError(hamburguesa,"No existe esa hamburguesa")
    if queso > 100:
        raise Demasiadoquesoerror(hamburguesa, queso,"TIENE DEMASIADO QUESO")
    if temperatura > 100:
        raise SehaquemadoError(hamburguesa, temperatura, "Se ha quemado la hamburguesa")
    if tipodepan not in ["centeno","semillas","integral"]:
        raise TipodepanError(hamburguesa, tipodepan, "Este tipo de pan no existe")
    print("La hamburguesa está lista")



#########################################################

for nombre,temp,ch,pan in [("cheeseburguer",50,90,"centeno"),("sdfdsf",100,50,"integral"),("baconburguer",98,50,"normal"),("cheeseburguer",50,101,"centeno"),("cheeseburguer",105,90,"centeno")]:
    try:
        crea_hamburguesa(nombre,temp,ch,pan)
    except Demasiadoquesoerror as cheese:
        print(cheese,":",cheese.queso)
    except SehaquemadoError as quemao:
        print(quemao,":",quemao.temperatura)
    except TipodepanError as pan:
        print(pan,":",pan.tipodepan)
    except HamburguesaError as burguer:
        print(burguer,":",burguer.hamburguesa)