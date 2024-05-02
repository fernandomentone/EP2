#BATALHA NAVAL

##############################################################################################################################################
#   CONSTANTES  #

CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

ALFABETO = 'ABCDEFGHIJ'

CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

PROXIMOS = {
    'Brasil': {'cruzador': 2, 'destroyer': 1, 'porta-avioes': 1, 'submarino': 2, 'torpedeiro': 1},
    'França': {'cruzador': 2, 'destroyer': 1, 'porta-avioes': 1, 'submarino': 2, 'torpedeiro': 1},
    'Austrália': {'cruzador': 2, 'destroyer': 1, 'porta-avioes': 1, 'submarino': 2, 'torpedeiro': 1},
    'Rússia': {'cruzador': 2, 'destroyer': 1, 'porta-avioes': 1, 'submarino': 2, 'torpedeiro': 1},
    'Japão': {'cruzador': 2, 'destroyer': 1, 'porta-avioes': 1, 'submarino': 2, 'torpedeiro': 1}
}

##############################################################################################################################################

def cria_mapa(n):
    mapa = []
    for c in range(n):
        lista = [' '] * n
        mapa.append(lista)
    return mapa

def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    if orientacao == 'h':
        if coluna + blocos > len(mapa[linha]):
            return False
        for i in range(blocos):
            if mapa[linha][coluna + i] != ' ':
                return False
    if orientacao == 'v':
        if linha + blocos > len(mapa):
            return False
        for i in range(blocos):
            if mapa[linha + i][coluna] != ' ':
                return False
    return True

import random

def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    if orientacao == 'h':
        if coluna + blocos > len(mapa[linha]):
            return False
        for i in range(blocos):
            if mapa[linha][coluna + i] != ' ':
                return False
    if orientacao == 'v':
        if linha + blocos > len(mapa):
            return False
        for i in range(blocos):
            if mapa[linha + i][coluna] != ' ':
                return False
    return True

def aloca_navios(mapa, blocos):
    n = len(mapa)
    for tamanho in blocos:
        while True:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            if posicao_suporta(mapa, tamanho, linha, coluna, orientacao):
                if orientacao == 'h':
                    for i in range(tamanho):
                        mapa[linha][coluna + i] = 'N'
                else:
                    for i in range(tamanho):
                        mapa[linha + i][coluna] = 'N'
                break
    return mapa

def foi_derrotado(mapa):
    for linha in mapa:
        for espaco in linha:
            if espaco == 'N':
                return False
    return True

def imprime_mapa(mapa_jogador, mapa_computador, nome_pais_jogador, nome_pais_computador):
    N = len(mapa_jogador)
    header = f"    JOGADOR - {nome_pais_jogador:20}{'COMPUTADOR - ' + nome_pais_computador:20}"
    indices = "   " + "  ".join(ALFABETO[i] for i in range(N))

    # Imprime cabeçalho com nomes dos jogadores
    print(header)
    print(indices, end="       ")
    print(indices)

    # Imprime os mapas lado a lado
    for i in range(N):
        print(f"{i+1:2} ", end="")
        for j in range(N):
            char = mapa_jogador[i][j]
            if char == ' ':
                print(CORES['cyan'] + char + CORES['reset'], end="  ")
            elif char == 'X':
                print(CORES['red'] + char + CORES['reset'], end="  ")
            else:
                print(CORES['yellow'] + char + CORES['reset'], end="  ")
        print(f" {i+1}", end="      ")

        print(f"{i+1:2} ", end="")
        for j in range(N):
            char = mapa_computador[i][j]
            print(CORES['cyan'] + (' ' if char in (' ', 'N') else char) + CORES['reset'], end="  ")
        print(f" {i+1}")

    # Imprime rodapé com índices novamente
    print(indices, end="       ")
    print(indices)