print('fofo')
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
    print(f"    JOGADOR - {nome_pais_jogador:20}{'           COMPUTADOR - ' + nome_pais_computador:20}")
    print("   " + "  ".join([ALFABETO[i] for i in range(N)]), end="    ")
    print("       ", end="")
    print("   " + "  ".join([ALFABETO[i] for i in range(N)]))
    for i in range(N):
        print(f"{i+1:2} ", end="")
        for j in range(N):
            if mapa_jogador[i][j] == ' ':
                print(CORES['cyan'] + mapa_jogador[i][j] + CORES['reset'], end="  ")
            elif mapa_jogador[i][j] == 'X':
                print(CORES['blue'] + mapa_jogador[i][j] + CORES['reset'], end="  ")
            else:
                print(CORES['yellow'] + mapa_jogador[i][j] + CORES['reset'], end="  ")
        print(f" {i+1}", end="")
        print("      ", end="")
        print(f"{i+1:2} ", end="")
        for j in range(N):
            if mapa_computador[i][j] == ' ' or mapa_computador[i][j] == 'N':
                print(CORES['cyan'] + ' ' + CORES['reset'], end="  ")
            else:
                print(CORES['cyan'] + mapa_computador[i][j] + CORES['reset'], end="  ")
        print(f" {i+1}")
    print("   " + "  ".join([ALFABETO[i] for i in range(N)]), end="    ")
    print("       ", end="")
    print("   " + "  ".join([ALFABETO[i] for i in range(N)]))

    
    def aloca_navios_jogador(mapa_jogador, mapa_computador, nome_pais_jogador, nome_pais_computador):
        print(f"Você escolheu a nação {nome_pais_jogador}")
        print("Agora é a sua vez de alocar seus navios de guerra!")
        imprime_mapa(mapa_jogador, mapa_computador, nome_pais_jogador, nome_pais_computador)
        tipo_navio_index = 0
        tipos_navios = list(PAISES[nome_pais_jogador].items())  # Transforma o dicionário em uma lista de tuplas para iteração
        while tipo_navio_index < len(tipos_navios):
            tipo_navio, quantidade = tipos_navios[tipo_navio_index]
            print(f"\nAloque os navios do tipo {tipo_navio}:")
            tipo_navio_bloco = CONFIGURACAO[tipo_navio]
            i = 0
            while i < quantidade:
                sucesso = False
                while not sucesso:
                    print(f"\nAlocação do {i+1}º {tipo_navio}\n")
                    imprime_mapa(mapa_jogador, mapa_computador, nome_pais_jogador, nome_pais_computador)
                    linha = input("\nDigite o número da linha (1 a 10): ")
                    if not linha.isdigit() or int(linha) < 1 or int(linha) > 10:
                        print("Linha inválida, tente novamente.")
                        continue
                    linha = int(linha) - 1
                    coluna = input("Digite a letra da coluna (A a J): ").upper()
                    if coluna not in ALFABETO:
                        print("Coluna inválida, tente novamente.")
                        continue
                    coluna = ALFABETO.index(coluna)
                    orientacao = input("Digite a orientação do navio (v para vertical, h para horizontal): ").lower()
                    if posicao_suporta(mapa_jogador, tipo_navio_bloco, linha, coluna, orientacao):
                        if orientacao == 'v':
                            j = linha
                            while j < linha + tipo_navio_bloco:
                                mapa_jogador[j][coluna] = 'N'
                                j += 1
                        else:
                            j = coluna
                            while j < coluna + tipo_navio_bloco:
                                mapa_jogador[linha][j] = 'N'
                                j += 1
                        sucesso = True
                    else:
                        print("Posição inválida, tente novamente.")
                i += 1
            tipo_navio_index += 1
            print()
                

def ataque_jogador(mapa_jogador, mapa_computador, nome_pais_jogador, nome_pais_computador):
    sucesso = False
    while not sucesso:
        imprime_mapa(mapa_jogador, mapa_computador, nome_pais_jogador, nome_pais_computador)
        print("\nAtaque:")

        linha_valida = False
        while not linha_valida:
            linha = input("Digite o número da linha (1 a 10): ")
            if linha.isdigit() and 1 <= int(linha) <= 10:
                linha = int(linha) - 1
                linha_valida = True
            else:
                print("Linha inválida, tente novamente.")

        coluna_valida = False
        while not coluna_valida:
            coluna = input("Digite a letra da coluna (A a J): ").upper()
            if coluna in ALFABETO:
                coluna = ALFABETO.index(coluna)
                if 0 <= coluna < 10:
                    coluna_valida = True
                else:
                    print("Coluna fora do alcance, tente novamente.")
            else:
                print("Coluna inválida, tente novamente.")

        if mapa_computador[linha][coluna] == ' ':  
            print("Água!")
            mapa_computador[linha][coluna] = 'O'
            sucesso = True
        elif mapa_jogador[linha][coluna] == 'N':
            print("Acertou um navio!")
            mapa_computador[linha][coluna] = 'X'
            sucesso = True
        else:
            print("Já atacou essa posição, tente novamente.")
