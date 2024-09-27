from src.randomizer import generarRandom
from src.damage import searchHeroStats, fillProbsDamageMatrix
from src.drop import fillProbsDropMatrix

#organiza todas las estadisticas del heroe para calcular el de daño aplicado
def calculateDamage( hero ):

    #comprobar que los campos necesarios existan
    if( hero.get('tipo-heroe', "error") == "error" ):
        return -1
    if( hero.get('subtipo-heroe', "error") == "error" ):
        return -1

    #Iterar las estadisticas en busca del tipo y subtipo de heroe que golpea
    hero, hitStats = searchHeroStats( hero )

    #rellenar matriz de probabilidades
    percentageMatrix = fillProbsDamageMatrix( hitStats, hero )

    #se selecciona un porcentaje en una posición al azar
    damagePercentage = percentageMatrix[generarRandom()]
    finalDamage = hero['damage'] * (damagePercentage/100)

    return finalDamage

#organiza todas las estadisticas de los productos para calcular producto dropeado
def calculateDrop( products ):

    #rellenar matriz de probabilidades
    percentageMatrix = fillProbsDropMatrix( products )

    #se selecciona un porcentaje en una posición al azar
    droppedProductId = percentageMatrix[generarRandom()]

    return droppedProductId

# prueba damage
# hero = {
#     'critico': 0,
#     'dano':0,
#     'tipo-heroe': 'GUERRERO',
#     'subtipo-heroe': 'TANQUE',
# }
# print(calculateDamage( hero ))
# { "critico": 1, "dano":1, "tipo-heroe": "GUERRERO", "subtipo-heroe": "TANQUE" }

# contador de campos repetidos en matriz
# counter = {}
# for e in percentageMatrix:
#     if(counter.get(e,"no esta")=="no esta"):
#         counter[e] = 1
#     else:
#         counter[e] += 1
# print(counter)
# print(len(percentageMatrix))

# prueba drop
# products = [
#     {'idProducto': 1, 'dropChance': 20},
#     {'idProducto': 2, 'dropChance': 30},
#     {'idProducto': 3, 'dropChance': 50},
# ]
# print(calculateDrop( products ))