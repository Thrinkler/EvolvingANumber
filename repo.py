limiteMayor = 10000
from random import randint
import random
from hijos import Hijo, HijoSexual


def parabola(x,val,raizMayor=limiteMayor): #función de aptitud
    if(x < val):
        x = val + (val - x)
    return -1*(x-(2*val-raizMayor))*(x-raizMayor)

def posibilidad_pasar(val, individuos): #probabilidad de pasar a la siguiente generacion segun funcion de aptitud
    maximo = max([item.val for item in individuos])
    maxVal = parabola(val, val, maximo)
    if maxVal == 0:
        for item in individuos:
            item.probPasar = 0
        return individuos
    for item in individuos:
        item.probPasar =  max(0, parabola(item.val, val, maximo))/maxVal
    return individuos

def crear_hijos(padres): #crear hijos segun probabilidad de pasar de los padres
    hijos = []
    for padre in padres:
        if(randint(400,1000)/1000 < padre.probPasar):
            if padre.probPasar > 0.8:
                hijos.extend([Hijo(padre)]*int(randint(1,3)))
            elif padre.probPasar > 0.5:
                hijos.extend([Hijo(padre)]*int(randint(0,3)))
            elif padre.probPasar > 0.2:
                hijos.extend([Hijo(padre)]*int(randint(0,2)))
            else:
                hijos.extend([Hijo(padre)]*int(randint(0,1)))
    return hijos

def ganadores_a_reproduccion(padres):
    padres_ordenados = sorted(padres, key=lambda p: p.probPasar, reverse=True)
    return padres_ordenados[:2]

MUESTRA = 5000
def reproduccion_sexual(padres): #crear hijos segun probabilidad de pasar de los padres
    hijos = []
    random.shuffle(padres)
    participantes = padres.copy()
    while len(participantes) >= 10 + len(participantes)//2:
        MUESTRA = len(participantes)//2
        ganadores = ganadores_a_reproduccion(participantes[0:MUESTRA])
        padre = ganadores[0]
        madre = ganadores[1]
        participantes.remove(padre)
        participantes.remove(madre)

        if(randint(400,1000)/1000 < (padre.probPasar + madre.probPasar)/2):
            if (padre.probPasar + madre.probPasar)/2 > 0.8:
                hijos.extend([HijoSexual(padre, madre)]*int(randint(1,3)))
            elif (padre.probPasar + madre.probPasar)/2 > 0.5:
                hijos.extend([HijoSexual(padre, madre)]*int(randint(0,3)))
            elif (padre.probPasar + madre.probPasar)/2 > 0.2:
                hijos.extend([HijoSexual(padre, madre)]*int(randint(0,2)))
            else:
                hijos.extend([HijoSexual(padre, madre)]*int(randint(0,1)))
    return hijos