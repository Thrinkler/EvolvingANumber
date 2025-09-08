from random import randint
import hijos
import padre    
import repo

limiteMayor = 10000

val = int(input("Ingrese el valor a encontrar (1-"+str(limiteMayor)+"): "))
limiteMayor = limiteMayor if val <= limiteMayor else val+1000
# val = 192 #valor a encontrar

padres = [padre.Padre(limiteMayor) for _ in range(10000)] #poblacion inicial aleatoria

perfectos = 0

for generacion in range(40):
    print("Generacion", generacion)
    padres = repo.posibilidad_pasar(val, padres)
    padres.sort(key=lambda x: x.probPasar, reverse=True)
    i = 0
    for padre in padres:
        if round(padre.val,2) != round(padres[0].val,2):
            break
        i += 1

    for padre in padres:
        if round(padre.val,2) == val:
            ##padres.pop(padres.index(padre))
            perfectos += 1
        else: 
            break
    print("Cantidad de padres: ", len(padres))
    print("Cantidad de padres perfectos encontrados hasta ahora: ", perfectos)
    if(len(padres) <= 100):
        print([padre.val for padre in padres])
    print("valor esperado: ", val)
    print("mejor padre: ", padres[0].val, " con probabilidad de pasar: ", round(padres[0].probPasar,2))
    print("cantidad de mejores padres: ", i)
    print("peor padre: ", padres[-1].val, " con probabilidad de pasar: ", round(padres[-1].probPasar,2))
    print("promedio padres: ", sum([padre.val for padre in padres])/len(padres))
    
    hijos = repo.reproduccion_sexual(padres) #repo.crear_hijos(padres)

    if len(padres) == i:
        print("todos son iguales. Se produjo incesto genetico")
        break
    if len(hijos) == 0:
        print("No hay hijos. Se produjo extincion")
        break
    print("Cantidad de hijos: ", len(hijos))
    padres = hijos
    print("--------------------------------------------------")

print("Cantidad de padres perfectos encontrados: ", perfectos)
##print([padre.val for padre in padres])
