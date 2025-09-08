from random import randint
import random
class Hijo:
    probPasar = 0 
    def __init__(self, padre):
        self.padre = padre
        self.val = padre.val*randint(90, 110)/100 if randint(0,100)/100 > 0.9 else padre.val

class HijoSexual(Hijo):
    def __init__(self, padre1, padre2):
        self.padre1 = padre1
        self.padre2 = padre2

        adn_padre1 = format(round(padre1.val), f'0{14}b')
        adn_padre2 = format(round(padre2.val), f'0{14}b')
        punto_de_corte = random.randint(1, 13)
        adn_hijo = adn_padre1[:punto_de_corte] + adn_padre2[punto_de_corte:]

        valor_cruzado = int(adn_hijo, 2)

        self.mutacion = randint(90, 110)/100 if randint(0,100)/100 > 0.9 else 1
        self.val = valor_cruzado * self.mutacion
        #self.val = (padre1.val + padre2.val)/2 * self.mutacion