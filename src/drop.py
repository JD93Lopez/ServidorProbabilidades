#rellenar estadística en matriz
def fillMatrixProductId( percentageMatrix, probability, value ):
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
        percentageMatrix.append(-1)
        filledRows+=1
    return percentageMatrix

#rellenar matriz de probabilidades
def fillProbsDropMatrix( products ):
    percentageMatrix = []

    # Iterar sobre el array y obtener el valor de 'dropChance'
    for product in products:
        drop_chance = product.get('dropChance', 0)
        product_id = product.get('idProducto', -2)
        #rellena las casillas de cada producto con su probabilidad de drop
        percentageMatrix = fillMatrixProductId( percentageMatrix, drop_chance, product_id )


    #rellena las casillas sobrantes con -1 (No se dropea producto)
    percentageMatrix = completeMatrix( percentageMatrix )

    return percentageMatrix