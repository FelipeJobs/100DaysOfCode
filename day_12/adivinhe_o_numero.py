import art
from random import randint

numero_gerado = randint(1, 100)
#essa função compara o valor digitado com o valor pensado
def comparar_valores(numeroj,numerog):
    if numerog < numeroj :
        return 'O número que estou pensando é menor que o valor digitado'
    elif  numerog > numeroj :
        return 'O número que estou pensando é maior que o valor digitado'
    else:
        return 0
# essa função controla o número de tentativas de acordo com o nível escolhido. 
def nivel(n):
    if n == 'facil':
        return 10
    elif n == 'dificil':
        return 5
    
#tela do jogo 
print(art.logo)
print('Bem-vindo ao jogo de adivinhação de números!\n')
nivel_escolhido = input('Escolha uma dificuldade. Digite facil ou hard: ').lower()
print('Estou pensando em um número entre 1 e 100.')
tentativas = nivel(n= nivel_escolhido)
print(tentativas)

# esse laço vai rodar de acordo com o número de tentativas, mas se o usuário
#acertar o número ele será finalizado.
for i in range(tentativas,0,-1):
    print(f'Você tem {i} tentativa(s)\n')
    numero_jogador = int(input('Qual é o número que estou pensando? '))
    comparacao = (comparar_valores(numerog = numero_gerado, numeroj = numero_jogador))
    
    if i == 1:
        print(f'\nInfelizmente você perdeu, o número que eu estava pensando era: {numero_gerado}')
    
    elif comparacao == 0:
        print('\nParabéns você acertou o valor que eu estava pensando.')
        break
    
    else:
        print(f'\n{comparacao}')