from random import choice
import art
from os import system
from time import sleep

lista_de_cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cartas_jogador = []
cartas_computador = []

#essa função vai distribuir 2 cartas para ambos os jogadores no início
def distribuir_cartas_inicio():
    while True:
        if len(cartas_computador) <2:
            cartas_computador.append(choice(lista_de_cartas))
            continue
        if len(cartas_jogador) == 2:
            break
        else:
            cartas_jogador.append(choice(lista_de_cartas))

#essa função vai calcular os valores dos jogadores.
def calcular_score(lista):
    if len(lista) == 2 and sum(lista) == 21:
        return 21
    
    return sum(lista)

def determinar_vencedor(lista_1 , lista_2):
    score_computador = calcular_score(lista_2)
    score_jogador = calcular_score(lista_1)
    print(f'mão_final_do_jogador: {lista_1} Score: {score_jogador}')
    print(f'mão_final_do_computador: {lista_2} Score: {score_computador}')
    if score_computador == 21:
       print('Computer win')
    elif score_jogador == 21:
       print('Jogador win')
    elif score_computador > 21 and score_jogador > 21:
        print('Draw')
    elif score_jogador > 21:
        print('computador win')
    elif score_computador > 21:
        print('Jogador win')
    elif score_jogador > score_computador:
       print('Jogador win')
    elif score_computador > score_jogador:
       print('computador win')
    else:
       print('Draw')

def pedir_carta(lista):
    carta_sorteada = choice(lista_de_cartas)
    if carta_sorteada == 11 and calcular_score(lista) >10:
        carta_sorteada = 1
    lista.append(carta_sorteada)


def computador_jogar(lista):
    while True:
        if calcular_score(lista) <=16: 
            pedir_carta(lista)
        else:
            break
def limpar_console():
    system('cls')
      
def jogar():
    limpar_console()
    cartas_jogador.clear()
    cartas_computador.clear()
    print(art.logo)
    sleep(3)
    distribuir_cartas_inicio()
    while True:  
        print(f'Suas cartas: {cartas_jogador}, score:{calcular_score(cartas_jogador)}')
        print(f'Primeira carta do computador: {cartas_computador[0]}')
        escolha_1 = input('digite s(sim) para obter uma nova carta ou\
 n(não) para passar: ').lower()
        if(escolha_1 == 's'):
            pedir_carta(cartas_jogador)   
            if sum(cartas_jogador) >21:
                limpar_console()
                computador_jogar(cartas_computador)
                determinar_vencedor(cartas_jogador, cartas_computador)
                break

        else:
            limpar_console()
            computador_jogar(cartas_computador)
            determinar_vencedor(cartas_jogador, cartas_computador)
            break





