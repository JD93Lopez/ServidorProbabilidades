from src.drop import fillMatrixProductId, completeMatrix, fillProbsDropMatrix
import pytest

@pytest.mark.parametrize(
    "products",
    [
        ([{'idProducto': 1, 'dropChance': 20},{'idProducto': 2, 'dropChance': 30},{'idProducto': 3, 'dropChance': 50}]),
        ([{'idProducto': 1, 'dropChance': 10},{'idProducto': 2, 'dropChance': 10}]),
        ([{'idProducto': 1, 'dropChance': 100}]),
    ]
)
def text_fillProbsDropMatrix( products ):
    percentageMatrix = fillProbsDropMatrix( products )

    counter = {'crit': 0}
    for e in percentageMatrix:
        if( 120 <= e <= 180 ):
            counter['crit'] += 1
        else:
            if(counter.get(e,"no esta")=="no esta"):
                counter[e] = 1
            else:
                counter[e] += 1

    for product in products:
        drop_chance = product.get('dropChance', 0)
        product_id = product.get('idProducto', -2)
        assert ( counter.get(product_id, 0) == ( 80000 * (drop_chance / 100) ) )