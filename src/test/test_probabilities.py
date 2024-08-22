from src.probabilities import calculateBaseDamage, searchHeroStats, fillMatrixCrit, fillMatrixStat, completeMatrix, fillProbsMatrix, calculateDamage
import pytest

@pytest.mark.parametrize(
    "hero, hitStats, min, max",
    [
        ({"dano": 1},{'dano-minimo': 1, 'dano-maximo': 4},2,5),
        ({"dano": 20},{'dano-minimo': 3, 'dano-maximo': 7},23,27),
        ({"dano": 14},{'dano-minimo': 1, 'dano-maximo': 1},15,15),
    ]
)
def test_calculateBaseDamage2( hero, hitStats, min, max ):

    res = calculateBaseDamage( hero, hitStats )

    assert ( res >= min & res <= max )


@pytest.mark.parametrize(
    "hero",
    [
        ({'tipo-heroe': 'GUERRERO', 'subtipo-heroe': 'TANQUE'}),
        ({'tipo-heroe': 'GUERRERO', 'subtipo-heroe': 'ARMAS'}),
        ({'tipo-heroe': 'MAGO', 'subtipo-heroe': 'FUEGO'}),
        ({'tipo-heroe': 'MAGO', 'subtipo-heroe': 'HIELO'}),
        ({'tipo-heroe': 'PICARO', 'subtipo-heroe': 'VENENO'}),
        ({'tipo-heroe': 'PICARO', 'subtipo-heroe': 'MACHETE'}),
    ]
)
def test_searchHeroStats( hero ):
    hero, hitStats = searchHeroStats( hero )
    assert ( (hitStats['tipo-heroe'] == hero['tipo-heroe']) & (hitStats['subtipo-heroe'] == hero['subtipo-heroe']) )


@pytest.mark.parametrize(
    "hitStats, hero, res",
    [
        ({'dano-crit-prob': 0},{'critico': 0},0),
        ({'dano-crit-prob': 50},{'critico': 30},64000),
        ({'dano-crit-prob': 0},{'critico': 30},24000),
        ({'dano-crit-prob': 30},{'critico': 0},24000),
    ]
)
def test_fillMatrixCrit( hitStats, hero, res ):
    percentageMatrix = []
    percentageMatrix = fillMatrixCrit( percentageMatrix, hitStats, hero )
    assert ( len(percentageMatrix) == res )


@pytest.mark.parametrize(
    "probability, value, res",
    [
        (50,101,40000),
        (0,101,0),
        (100,101,80000),
    ]
)
def test_fillMatrixStat( probability, value, res ):
    percentageMatrix = []
    fillMatrixStat( percentageMatrix, probability, value )
    for e in percentageMatrix:
        assert ( e == value )
    assert ( len(percentageMatrix) == res )


@pytest.mark.parametrize(
    "percentageMatrix",
    [
        ([0]*80000),
        ([]),
        ([0,0,0]),
    ]
)
def test_completeMatrix( percentageMatrix ):
    completeMatrix(percentageMatrix)
    assert ( len(percentageMatrix) == 80000 )
    


@pytest.mark.parametrize(
    "hitStats, hero",
    [
        ({'dano-prob': 40, 'dano-crit-prob': 0, 'evadir-golpe-prob': 5, 'resistir-prob': 0, 'escapar-prob': 5},{'critico':0}),
        ({'dano-prob': 0, 'dano-crit-prob': 0, 'evadir-golpe-prob': 0, 'resistir-prob': 0, 'escapar-prob': 0},{'critico':0}),
        ({'dano-prob': 20, 'dano-crit-prob': 10, 'evadir-golpe-prob': 20, 'resistir-prob': 20, 'escapar-prob': 20},{'critico':10}),
    ]
)
def test_fillProbsMatrix( hitStats, hero ):
    percentageMatrix = fillProbsMatrix( hitStats, hero )

    counter = {'crit': 0}
    for e in percentageMatrix:
        if( 120 <= e <= 180 ):
            counter['crit'] += 1
        else:
            if(counter.get(e,"no esta")=="no esta"):
                counter[e] = 1
            else:
                counter[e] += 1

    assert ( counter.get('crit', 0) == ( 80000 * ((hitStats['dano-crit-prob'] + hero.get('critico',0))/ 100)  ) )
    assert ( counter.get(100, 0) == ( 80000 * (hitStats['dano-prob'] / 100) ) )
    assert ( counter.get(80, 0) == ( 80000 * (hitStats['evadir-golpe-prob'] / 100) ) )
    assert ( counter.get(60, 0) == ( 80000 * (hitStats['resistir-prob'] / 100) ) )
    assert ( counter.get(20, 0) == ( 80000 * (hitStats['escapar-prob'] / 100) ) )



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