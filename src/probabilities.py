from randomizer import indiceAleatorio, generarRandom
import random

#Arreglo de estadisticas de golpe por tipo y subtipo de heroe
hitStatsPerType = [
    {
        'tipo-heroe': 'GUERRERO',
        'subtipo-heroe': 'TANQUE',
        'dano-minimo': 1,
        'dano-maximo': 4,
        'dano-prob': 40,
        'dano-crit-prob': 0,
        'evadir-golpe-prob': 5,
        'resistir-prob': 0,
        'escapar-prob': 5,
    },    
    {
        'tipo-heroe': 'GUERRERO',
        'subtipo-heroe': 'ARMAS',
        'dano-minimo': 1,
        'dano-maximo': 4,
        'dano-prob': 60,
        'dano-crit-prob': 5,
        'evadir-golpe-prob': 3,
        'resistir-prob': 0,
        'escapar-prob': 2,
    },    
    {
        'tipo-heroe': 'MAGO',
        'subtipo-heroe': 'FUEGO',
        'dano-minimo': 1,
        'dano-maximo': 4,
        'dano-prob': 70,
        'dano-crit-prob': 5,
        'evadir-golpe-prob': 0,
        'resistir-prob': 5,
        'escapar-prob': 0,
    },   
    {
        'tipo-heroe': 'MAGO',
        'subtipo-heroe': 'HIELO',
        'dano-minimo': 1,
        'dano-maximo': 4,
        'dano-prob': 70,
        'dano-crit-prob': 6,
        'evadir-golpe-prob': 0,
        'resistir-prob': 4,
        'escapar-prob': 0,
    },  
    {
        'tipo-heroe': 'PICARO',
        'subtipo-heroe': 'VENENO',
        'dano-minimo': 1,
        'dano-maximo': 4,
        'dano-prob': 55,
        'dano-crit-prob': 10,
        'evadir-golpe-prob': 0,
        'resistir-prob': 0,
        'escapar-prob': 0,
    },  
    {
        'tipo-heroe': 'PICARO',
        'subtipo-heroe': 'MACHETE',
        'dano-minimo': 1,
        'dano-maximo': 4,
        'dano-prob': 60,
        'dano-crit-prob': 8,
        'evadir-golpe-prob': 0,
        'resistir-prob': 0,
        'escapar-prob': 2,
    },  
]

def calculateDamage( hero ):

    if( hero.get('tipo-heroe', "error") == "error" ):
        return -1
    if( hero.get('subtipo-heroe', "error") == "error" ):
        return -1

    #Iterar las estadisticas en busca del tipo y subtipo de heroe que golpea
    for hitStats in hitStatsPerType:
        if( (hitStats['tipo-heroe'] == hero['tipo-heroe']) & 
        (hitStats['subtipo-heroe'] == hero['subtipo-heroe']) ):
            #Calcular el daño aleatorio del héroe que golpea
            hero['damage'] = random.randint(hitStats['dano-minimo'], hitStats['dano-maximo']) + hero.get('dano', 0)
    
    percentageMatrix = []
    cnt = 0

    #rellena las casillas de daño normal es decir 100%
    probability = hitStats['dano-prob']
    rows = 80000 * (probability/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(100)
        cnt+=1

    #rellena las casillas de critico adicionando el boots de critico y hace de 120% a 180%
    probability = hitStats['dano-crit-prob']
    rows = 80000 * ((probability+ hero.get('critico',0) )/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(random.randint(120,180))
        cnt+=1

    #rellena las casillas de daño cuando evaden es decir 80%
    probability = hitStats['evadir-golpe-prob']
    rows = 80000 * (probability/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(80)
        cnt+=1

    #rellena las casillas de daño cuando resisten es decir 60%
    probability = hitStats['resistir-prob']
    rows = 80000 * (probability/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(60)
        cnt+=1

    #rellena las casillas de daño cuando escapan es decir 20%
    probability = hitStats['escapar-prob']
    rows = 80000 * (probability/100)
    actual = cnt
    while( cnt < (rows + actual) ):
        percentageMatrix.append(20)
        cnt+=1

    #rellena las casillas sobrantes con ceros (No causa daño)
    while(cnt<80000):
        percentageMatrix.append(0)
        cnt+=1

    #se selecciona un porcentaje en una posición al azar
    damagePercentage = percentageMatrix[generarRandom()]
    finalDamage = hero['damage'] * (damagePercentage/100)

    return finalDamage

#prueba
# hero = {
#     'critico': 1,
#     'dano':1,
#     'tipo-heroe': 'GUERRERO',
#     'subtipo-heroe': 'TANQUE',
# }
# print(calculateDamage( hero ))
#{ "critico": 1, "dano":1, "tipo-heroe": "GUERRERO", "subtipo-heroe": "TANQUE" }