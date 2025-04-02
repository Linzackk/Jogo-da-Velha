# computador que joga aleatório
# computador só pode jogar nos lugares onde não tem jogadas
# cada parte na matriz vai ser composto por um número (1 a 9)
# as jogadas vão ser contabilizadas em uma lista []
from random import randint
from time import sleep
import os

def condicoes(jogo):
    linha1 = jogo["9"] + jogo["8"] + jogo["7"]
    linha2 = jogo["4"] + jogo["5"] + jogo["6"]
    linha3 = jogo["1"] + jogo["2"] + jogo["3"]

    coluna1 = jogo["7"] + jogo["4"] + jogo["1"]
    coluna2 = jogo["8"] + jogo["5"] + jogo["2"]
    coluna3 = jogo["9"] + jogo["6"] + jogo["3"]

    diag1 = jogo["7"] + jogo["5"] + jogo["3"]
    diag2 = jogo["9"] + jogo["5"] + jogo["1"]
    condicts = {linha1, linha2, linha3, coluna1, coluna2, coluna3, diag1, diag2}
    for c in condicts:
        if c == 'XXX':
            vitoria = 'JG'
            break
        elif c == 'OOO':
            vitoria = 'PC'
            break
        else:
            vitoria = ''
    return vitoria

linha = '-' * 19
vitoria = ''

def mostrar_jogo(lst):
    for c in range(7,10):
        c = str(c)
        print(f'|  {lst[c]:3}', end='')
    print('|')
    for d in range(4,7):
        d = str(d)
        print(f'|  {lst[d]:3}', end='')
    print('|')
    for e in range(1,4):
        e = str(e)
        print(f'|  {lst[e]:3}', end='')
    print('|')

def jogada():
    jogada = 0
    while jogada < 1 or jogada > 9:
        jogada = int(input('Insira sua Jogada (1 - 9) '))
    return jogada

def jogada_player(lst):
    while True:
        esc = jogada()
        if lst[str(esc)] != '':
            print('Opção já escolhida!')
        else:
            break
    lst[str(esc)] = 'X'
    return(lst)

def jogada_comp(lst):
    while True:
        esc = randint(1,9)
        if lst[str(esc)] == '':
            break
    lst[str(esc)] = 'O'
    #return lst

def jogo_velha():
    jogo = {
        "9": '',
        "8": '',
        "7": '',
        "6": '',
        "5": '',
        "4": '',
        "3": '',
        "2": '',
        "1": ''
    }
    jogadas = 1
    vitoria = ''
    while jogadas <= 9:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(linha)
        mostrar_jogo(jogo)
        if jogadas % 2 == 0:
            jogada_comp(jogo)
        else:
            print(linha)
            jogada_player(jogo)
        vitoria = condicoes(jogo)
        if vitoria != '':
            break
        jogadas += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(linha)
    mostrar_jogo(jogo)
    print(linha)
    if vitoria == '':
        print('Deu Velha!')
    else:
        print('O Ganhador foi: ')
        sleep(1)
    if vitoria == 'PC':
        print('O COMPUTADOR !!!')
    elif vitoria == 'JG':
        print('VOCÊ !!!')

jogo_velha()







