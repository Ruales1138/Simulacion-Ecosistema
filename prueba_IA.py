import random

class Depredador:
    def __init__(self):
        self.energia: int = 5
        self.sin_comer = 0
    
    def __repr__(self):
        return 'Depre'
    
class Presa:
    def __init__(self):
        self.energia: int = 5

    def __repr__(self):
        return 'Presa'
    
class Planta:
    def __init__(self):
        self.energia: int = 5

    def __repr__(self):
        return 'Plant'
    

def generar_matriz(n: int, i: int = 0, j: int = 0, matriz: list[list[int]] = [], fila: list[int] = []) -> list[list[int]]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return generar_matriz(n, i+1, 0, matriz, [])
    
    elemento = random.choice([Depredador(), Presa(), Planta(), '   '])
    fila.append(elemento)
    return generar_matriz(n, i, j+1, matriz, fila)

def buscar_presa(matriz, x, y, n, paso=1):
    if paso >= n:
        return None
    
    # Buscar en la fila
    if y + paso < n and isinstance(matriz[x][y + paso], Presa):
        return (x, y + paso)
    if y - paso >= 0 and isinstance(matriz[x][y - paso], Presa):
        return (x, y - paso)
    
    # Buscar en la columna
    if x + paso < n and isinstance(matriz[x + paso][y], Presa):
        return (x + paso, y)
    if x - paso >= 0 and isinstance(matriz[x - paso][y], Presa):
        return (x - paso, y)
    
    return buscar_presa(matriz, x, y, n, paso + 1)

def mover_depredador(matriz, x, y, n):
    presa = buscar_presa(matriz, x, y, n)
    if presa:
        px, py = presa
        matriz[px][py] = Depredador()
        matriz[x][y] = '   '
    return matriz

def mover_presa(matriz, x, y, n):
    direcciones = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    direcciones = [(nx, ny) for nx, ny in direcciones if 0 <= nx < n and 0 <= ny < n and matriz[nx][ny] == '   ']
    if direcciones:
        nx, ny = random.choice(direcciones)
        matriz[nx][ny] = Presa()
        matriz[x][y] = '   '
    return matriz

def actualizar_ecosistema(matriz, n, i=0, j=0):
    if i == n:
        return matriz
    if j == n:
        return actualizar_ecosistema(matriz, n, i + 1, 0)
    if isinstance(matriz[i][j], Depredador):
        matriz = mover_depredador(matriz, i, j, n)
    elif isinstance(matriz[i][j], Presa):
        matriz = mover_presa(matriz, i, j, n)
    return actualizar_ecosistema(matriz, n, i, j + 1)

def ciclos(ecosistema: list[list[str]], idx: int = 0, limite: int = 5) -> None:
    if idx == limite:
        return 'Fin del ciclo'
    else:
        print(*ecosistema, sep="\n")
        print('-----------------------------------')
        ecosistema = actualizar_ecosistema(ecosistema, len(ecosistema))
        return ciclos(ecosistema, idx+1)

ecosistema = generar_matriz(5)
print(ciclos(ecosistema))