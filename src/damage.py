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
        'dano-crit-prob': 0,
        'evadir-golpe-prob': 3,
        'resistir-prob': 0,
        'escapar-prob': 2,
    },    
    {
        'tipo-heroe': 'MAGO',
        'subtipo-heroe': 'FUEGO',
        'dano-minimo': 1,
        'dano-maximo': 6,
        'dano-prob': 70,
        'dano-crit-prob': 0,
        'evadir-golpe-prob': 0,
        'resistir-prob': 5,
        'escapar-prob': 0,
    },   
    {
        'tipo-heroe': 'MAGO',
        'subtipo-heroe': 'HIELO',
        'dano-minimo': 1,
        'dano-maximo': 6,
        'dano-prob': 70,
        'dano-crit-prob': 0,
        'evadir-golpe-prob': 0,
        'resistir-prob': 4,
        'escapar-prob': 0,
    },  
    {
        'tipo-heroe': 'PICARO',
        'subtipo-heroe': 'VENENO',
        'dano-minimo': 1,
        'dano-maximo': 8,
        'dano-prob': 55,
        'dano-crit-prob': 0,
        'evadir-golpe-prob': 0,
        'resistir-prob': 0,
        'escapar-prob': 0,
    },  
    {
        'tipo-heroe': 'PICARO',
        'subtipo-heroe': 'MACHETE',
        'dano-minimo': 1,
        'dano-maximo': 8,
        'dano-prob': 60,
        'dano-crit-prob': 0,
        'evadir-golpe-prob': 0,
        'resistir-prob': 0,
        'escapar-prob': 2,
    },  
]

#Calcular el daño aleatorio del héroe que golpea
def calculateBaseDamage( hero, hitStats ):
    return random.randint(hitStats['dano-minimo'], hitStats['dano-maximo']) + hero.get('dano', 0)

#Iterar las estadisticas en busca del tipo y subtipo de heroe que golpea
def searchHeroStats( hero ):
    for hitStats in hitStatsPerType:
        if( (hitStats['tipo-heroe'] == hero['tipo-heroe']) & 
        (hitStats['subtipo-heroe'] == hero['subtipo-heroe']) ):
            #Calcular el daño aleatorio del héroe que golpea
            hero['damage'] = calculateBaseDamage( hero, hitStats )
            return hero, hitStats
    return hero, {
        'tipo-heroe': 'NONE',
        'subtipo-heroe': 'NONE',
        'dano-minimo': 0,
        'dano-maximo': 0,
        'dano-prob': 0,
        'dano-crit-prob': 0,
        'evadir-golpe-prob': 0,
        'resistir-prob': 0,
        'escapar-prob': 0,
    }

#rellenar críticos en matriz
def fillMatrixCrit( percentageMatrix, hitStats, hero ):
    #obtener filas llenadas hasta ahora
    filledRows = len(percentageMatrix)
    probability = hitStats['dano-crit-prob']
    #calcular filas a rellenar
    rows = 80000 * ((probability + hero.get('critico',0) )/100)
    filledBefore = filledRows
    #rellenar hasta que las filas alcancen el valor de las filas que llevaba + las nuevas
    while( filledRows < (rows + filledBefore) ):
        #insertar valor porcentaje de daño
        percentageMatrix.append(random.randint(120,180))
        filledRows+=1

    return percentageMatrix

#rellenar estadística en matriz
def fillMatrixStat( percentageMatrix, probability, value ):
    #obtener filas llenadas hasta ahora
    filledRows = len(percentageMatrix)
    if( filledRows >= 80000 ):
        return percentageMatrix
    #calcular filas a rellenar
    rows = 80000 * (probability/100)
    filledBefore = filledRows
    #rellenar hasta que las filas alcancen el valor de las filas que llevaba + las nuevas
    while( filledRows < (rows + filledBefore) ):
        #insertar valor porcentaje de daño
        percentageMatrix.append(value)
        filledRows+=1
    return percentageMatrix

#rellena la matriz de ceros hasta que tenga 80000 filas
def completeMatrix(percentageMatrix):
    filledRows = len(percentageMatrix)
    while(filledRows<80000):
        percentageMatrix.append(0)
        filledRows+=1
    return percentageMatrix

#rellenar matriz de probabilidades
def fillProbsDamageMatrix( hitStats, hero ):
    percentageMatrix = []
    #rellena las casillas de critico adicionando el boots de critico y hace de 120% a 180%
    percentageMatrix = fillMatrixCrit( percentageMatrix, hitStats, hero )

    #rellena las casillas de daño normal es decir 100%
    percentageMatrix = fillMatrixStat( percentageMatrix, hitStats['dano-prob'], 100 )

    #rellena las casillas de daño cuando evaden es decir 80%
    percentageMatrix = fillMatrixStat( percentageMatrix, hitStats['evadir-golpe-prob'], 80 )

    #rellena las casillas de daño cuando resisten es decir 60%
    percentageMatrix = fillMatrixStat( percentageMatrix, hitStats['resistir-prob'], 60 )

    #rellena las casillas de daño cuando escapan es decir 20%
    percentageMatrix = fillMatrixStat( percentageMatrix, hitStats['escapar-prob'], 20 )

    #rellena las casillas sobrantes con ceros (No causa daño)
    percentageMatrix = completeMatrix( percentageMatrix )

    return percentageMatrix