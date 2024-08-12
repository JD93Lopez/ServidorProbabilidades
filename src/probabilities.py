from randomizer import indiceAleatorio, generarRandom
import random

#Arreglo de estadisticas de golpe por tipo y subtipo de heroe
hitStatsPerType = [
    {
        'type': 'GUERRERO',
        'subtype': 'TANQUE',
        'minDamage': 1,
        'maxDamage': 4,
        'damageProb': 40,
        'criticalProb': 0,
        'evadeProb': 5,
        'resistProb': 0,
        'escapeProb': 5,
    }
]

def calculateDamage( hero ):

    #Iterar las estadisticas en busca del tipo y subtipo de heroe que golpea
    for hitStats in hitStatsPerType:
        if( (hitStats['type'] == hero['type']) & 
        (hitStats['subtype'] == hero['subtype']) ):
            #Calcular el daño aleatorio del héroe que golpea
            hero['damage'] = random.randint(hitStats['minDamage'], hitStats['maxDamage']) + hero.get('damageBoost', 0)
    
    percentageMatrix = []
    cnt = 0

    #rellena las casillas de daño normal es decir 100%
    probability = hitStats['damageProb']
    rows = 80000 * (probability/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(100)
        cnt+=1

    #rellena las casillas de critico adicionando el boots de critico y hace de 120% a 180%
    probability = hitStats['criticalProb']
    rows = 80000 * ((probability+hero['criticalBoost'])/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(random.randint(120,180))
        cnt+=1

    #rellena las casillas de daño cuando evaden es decir 80%
    probability = hitStats['evadeProb']
    rows = 80000 * (probability/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(80)
        cnt+=1

    #rellena las casillas de daño cuando resisten es decir 60%
    probability = hitStats['resistProb']
    rows = 80000 * (probability/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(60)
        cnt+=1

    #rellena las casillas de daño cuando escapan es decir 20%
    probability = hitStats['escapeProb']
    rows = 80000 * (probability/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(20)
        cnt+=1

    #rellena las casillas sobrantes con ceros (No causa daño)
    while(cnt<=80000):
        percentageMatrix.append(0)
        cnt+=1

    #se selecciona un porcentaje en una posición al azar
    damagePercentage = percentageMatrix[generarRandom()]
    finalDamage = hero['damage'] * (damagePercentage/100)

    return finalDamage

#prueba
hero = {
    'criticalBoost': 0,
    'damageBoost':1,
    'type': 'GUERRERO',
    'subtype': 'TANQUE',
}
calculateDamage( hero )