import random

class Depredador:
    def __init__(self, vida: int = 5):
        self.vida: int = vida
    
    def __repr__(self):
        return '🦁 '
    
class Presa:
    def __init__(self, vida: int = 5):
        self.vida: int = vida

    def __repr__(self):
        return '🦓 '
    
class Planta:
    def __init__(self):
        self.vida: int = 5

    def __repr__(self):
        return '🌾 '
    

def generar_matriz(n: int, i: int = 0, j: int = 0, matriz: list[list[int]] = [], fila: list[int] = []) -> list[list[int]]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return generar_matriz(n, i+1, 0, matriz, [])
    
    elemento = random.choice([Depredador(), Presa(), Planta()])
    fila.append(random.choice([elemento, ' ']))
    return generar_matriz(n, i, j+1, matriz, fila)


ecosistema = generar_matriz(5)

print(*ecosistema, sep="\n")


def buscar_presa(ecosistema, fila, columna, paso=1):
    if paso >= len(ecosistema):
        return (-1, -1)
    
    if fila + paso < len(ecosistema) and isinstance(ecosistema[fila + paso][columna], Presa):
        return (fila + paso, columna)
    if fila - paso >= 0 and isinstance(ecosistema[fila - paso][columna], Presa):
        return (fila - paso, columna) 
    
    if columna + paso < len(ecosistema) and isinstance(ecosistema[fila][columna + paso], Presa):
        return (fila, columna + paso)
    if columna - paso >=0 and isinstance(ecosistema[fila][columna - paso], Presa):
        return (fila, columna - paso)
    
    return buscar_presa(ecosistema, fila, columna, paso+1) 


def mover_aleatorio_d(ecosistema, fila, columna):
    fila_o_columna = random.randint(0,1)
    vida = ecosistema[fila][columna].vida

    if fila_o_columna == 0:
        fila_a = random.randint(0, len(ecosistema)-1)
        if ecosistema[fila_a][columna] == ' ':
            ecosistema[fila_a][columna] = Depredador(vida)
            ecosistema[fila][columna] = ' '
            print(f'Nueva posicion:  D{fila_a, columna} Vida: {ecosistema[fila_a][columna].vida}')
        else:
            return mover_aleatorio_d(ecosistema, fila, columna)

    if fila_o_columna == 1:
        columna_a = random.randint(0, len(ecosistema)-1)
        if ecosistema[fila][columna_a] == ' ':
            ecosistema[fila][columna_a] = Depredador(vida)
            ecosistema[fila][columna] = ' '
            print(f'Nueva posicion:  D{fila, columna_a} Vida: {ecosistema[fila][columna_a].vida}')
        else:
            return mover_aleatorio_d(ecosistema, fila, columna)

    return ecosistema


def mover_depredador(ecosistema, fila, columna):
    presa = buscar_presa(ecosistema, fila, columna)
    vida = ecosistema[fila][columna].vida

    if presa != (-1, -1):
        fila_p, columna_p = presa
        ecosistema[fila_p][columna_p] = Depredador(vida + 5)
        ecosistema[fila][columna] = ' '
        print(f'Nueva posicion:  D{fila_p, columna_p} Vida: {ecosistema[fila_p][columna_p].vida}')

    if presa == (-1, -1):
        ecosistema = mover_aleatorio_d(ecosistema, fila, columna)

    return ecosistema


def buscar_planta(ecosistema, fila, columna):
    
    if fila + 1 < len(ecosistema) and isinstance(ecosistema[fila + 1][columna], Planta):
        return (fila + 1, columna)
    if fila - 1 >= 0 and isinstance(ecosistema[fila - 1][columna], Planta):
        return (fila - 1, columna) 
    
    if columna + 1 < len(ecosistema) and isinstance(ecosistema[fila][columna + 1], Planta):
        return (fila, columna + 1)
    if columna - 1 >= 0 and isinstance(ecosistema[fila][columna - 1], Planta):
        return (fila, columna - 1)
    
    if fila + 1 < len(ecosistema) and columna + 1 < len(ecosistema) and isinstance(ecosistema[fila + 1][columna + 1], Planta):
        return (fila + 1, columna + 1)
    if fila + 1 < len(ecosistema) and columna - 1 >= 0 and isinstance(ecosistema[fila + 1][columna - 1], Planta):
        return (fila + 1, columna - 1)
    
    if fila - 1 >= 0 and columna - 1 >= 0 and isinstance(ecosistema[fila - 1][columna - 1], Planta):
        return (fila - 1, columna - 1)
    if fila - 1 >= 0 and columna + 1 < len(ecosistema) and isinstance(ecosistema[fila - 1][columna + 1], Planta):
        return (fila - 1, columna + 1)
    
    return (-1, -1)


def mover_aleatorio_p(ecosistema, fila, columna):
    n1 = random.randint(-1, 1)
    n2 = random.randint(-1, 1)
    n_max = len(ecosistema)
    vida = ecosistema[fila][columna].vida

    if 0 <= (fila + n1) < n_max and 0 <= (columna + n2) < n_max and not isinstance(ecosistema[fila + n1][columna + n2], Presa):
        if isinstance(ecosistema[fila + n1][columna + n2], Depredador):
            vida = ecosistema[fila  + n1][columna + n2].vida
            ecosistema[fila + n1][columna + n2] = Depredador(vida + 5)
            ecosistema[fila][columna] = ' '
            print(f'Nueva posicion:  P{fila + n1, columna + n2} Vida: {0}')
        else:
            ecosistema[fila + n1][columna + n2] = Presa(vida)
            ecosistema[fila][columna] = ' '
            print(f'Nueva posicion:  P{fila + n1, columna + n2} Vida: {ecosistema[fila + n1][columna + n2].vida}')
    else:
        return mover_aleatorio_p(ecosistema, fila, columna)

    return ecosistema


def mover_presa(ecosistema, fila, columna):
    planta = buscar_planta(ecosistema, fila, columna)
    vida = ecosistema[fila][columna].vida

    if planta != (-1, -1):
        fila_pl, columna_pl = planta
        ecosistema[fila_pl][columna_pl] = Presa(vida + 5)
        ecosistema[fila][columna] = ' '
        print(f'Nueva posicion:  P{fila_pl, columna_pl} Vida: {ecosistema[fila_pl][columna_pl].vida}')

    if planta == (-1, -1):
        ecosistema = mover_aleatorio_p(ecosistema, fila, columna)

    return ecosistema


def actualizar_ecosistema(ecosistema: list[list[object]], fila: int = 0, columna: int = 0) -> tuple:
    if fila == len(ecosistema):
        return 'Fin'
    
    if columna == len(ecosistema):
        return actualizar_ecosistema(ecosistema, fila+1, 0)
    
    if isinstance(ecosistema[fila][columna], Depredador):
        print(f'Posicion actual: D{fila, columna} Vida: {ecosistema[fila][columna].vida}')
        ecosistema = mover_depredador(ecosistema, fila, columna)
        print(*ecosistema, sep="\n")

    if isinstance(ecosistema[fila][columna], Presa):
        print(f'Posicion actual: P{fila, columna} Vida: {ecosistema[fila][columna].vida}')
        ecosistema = mover_presa(ecosistema, fila, columna)
        print(*ecosistema, sep="\n")

    return actualizar_ecosistema(ecosistema, fila, columna+1)


def cambio_de_dia(ecosistema, fila = 0, columna = 0):
    if fila == len(ecosistema):
        print(*ecosistema, sep="\n")
        return ecosistema

    if columna == len(ecosistema):
        return cambio_de_dia(ecosistema, fila+1, 0)

    if isinstance(ecosistema[fila][columna], Depredador):
        vida = ecosistema[fila][columna].vida
        print(vida)
        if vida - 5 == 0:
            ecosistema[fila][columna] = ' '
        else:
            ecosistema[fila][columna] = Depredador(vida - 5)
            print(ecosistema[fila][columna].vida)

    if isinstance(ecosistema[fila][columna], Presa):
        vida = ecosistema[fila][columna].vida
        print(vida)
        if vida - 5 == 0:
            ecosistema[fila][columna] = ' '
        else:
            ecosistema[fila][columna] = Presa(vida - 5)
            print(ecosistema[fila][columna].vida)

    return cambio_de_dia(ecosistema, fila, columna+1)


def ciclos(ecosistema: list[list[str]], idx: int = 0, dia: int = 1, limite: int = 5) -> None:
    if idx == limite:
        return 'Fin del ciclo'
    else:
        input("Presiona Enter: ")
        print(f'--------------------------------------------------Dia {dia}--------------------------------------------------')
        if dia == 1:
            print(actualizar_ecosistema(ecosistema))
        else:
            ecosistema = cambio_de_dia(ecosistema)
            print(actualizar_ecosistema(ecosistema))
        print(f'------------------------------------------------Fin Dia {dia}------------------------------------------------')
        return ciclos(ecosistema, idx+1, dia+1)


print(ciclos(ecosistema))

