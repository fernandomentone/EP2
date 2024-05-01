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