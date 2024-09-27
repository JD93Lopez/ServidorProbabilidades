from src.probabilities import calculateDamage, calculateDrop
import pytest

@pytest.mark.parametrize(
    "hero, min, max",
    [
        ({ "critico": 0, "dano":1, "tipo-heroe": "GUERRERO", "subtipo-heroe": "TANQUE" },0,5),
        ({ "critico": 50, "dano":100, "tipo-heroe": "GUERRERO", "subtipo-heroe": "TANQUE" },0.2*100,1.8*105),
        ({ "critico": 100, "dano":1, "tipo-heroe": "GUERRERO", "subtipo-heroe": "TANQUE" },1.2*2,1.8*5),
        ({ "critico": 0, "dano":0, "tipo-heroe": "MAGO", "subtipo-heroe": "FUEGO" },0,1.8*6),
        ({ "critico": 0, "dano":0, "tipo-heroe": "PICARO", "subtipo-heroe": "MACHETE" },0,1.8*8),
    ]
)
def test_calculateDamage( hero, min, max ):
    assert ( min <= calculateDamage( hero ) <= max )


# prueba drop
# products = [
#     {'idProducto': 1, 'dropChance': 20},
#     {'idProducto': 2, 'dropChance': 30},
#     {'idProducto': 3, 'dropChance': 50},
# ]
# print(calculateDrop( products ))
@pytest.mark.parametrize(
    "products, expected",
    [
        ([{'idProducto': 1, 'dropChance': 0},{'idProducto': 2, 'dropChance': 0},{'idProducto': 3, 'dropChance': 100}],3),
        ([{'idProducto': 1, 'dropChance': 0},{'idProducto': 2, 'dropChance': 0}],-1),
        ([{'idProducto': 1, 'dropChance': 100}],1),
    ]
)
def test_calculateDrop( products, expected ):
    assert ( calculateDrop( products ) == expected )