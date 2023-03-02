import game_dados
import art
from random import choice
from os import system

#definindo todos os dados que vou utilizar
lista_de_pessoas = game_dados.data
pessoa_a = choice(lista_de_pessoas)
pessoa_b = choice(lista_de_pessoas)
score = 0

#essa função compara os seguidores e retorna o que tiver maior número de seguidores
def comparar_seguidores(pessoa1,pessoa2):
    seguidores_pessoa1 = pessoa1['follower_count']
    seguidores_pessoa2 = pessoa2['follower_count']
    if seguidores_pessoa1 > seguidores_pessoa2:
        return 'a'
    else:
        return 'b'
# essa função é criada colocar os dados dos famosos junto com as logos
def tela_do_jogo(p1,p2):
    print(art.logo)
    print(f'Pessoa A: {p1["name"]}, {p1["country"]}, {p1["description"]} ') 
    print(art.vs)
    print(f'Pessoa B: {p2["name"]}, {p2["country"]}, {p2["description"]} ') 

#Lógica de execução do jogo.
while True:
    system('cls')
    tela_do_jogo(pessoa_a, pessoa_b)
    resposta_do_jogador = input('Quem tem mais seguidores? A ou B:').lower()
    resultado_da_comparacao = comparar_seguidores(pessoa_a, pessoa_b)
    
    if  resposta_do_jogador != resultado_da_comparacao:
        system('cls')
        print(f'Desculpe, isso está errado. Pontuação final: {score}')
        break
    else:
        score +=1
        pessoa_a = pessoa_b
        pessoa_b = choice(lista_de_pessoas)

