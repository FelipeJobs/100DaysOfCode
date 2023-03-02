import random
from time import sleep
from imports import imagens
from imports import palavras

#salva as palavras importadas em uma lista interna

palavras = palavras.palavras

# vai imprimir de acordo com a quantidade de erros.
estagios = imagens.estagios

#As três linhas abaixo selecionam o dicionário da lista e armazena a dica 
#e a palavras em uma variável.
selecionando_dicionario = random.choice(palavras)
dica = selecionando_dicionario['Dica'].upper()
indice_lista_externa = random.randint(0,len(palavras)) -1
palavra_secret =  random.choice(palavras[indice_lista_externa]['Palavra']).upper()
palavra_escondida = list('#'*len(palavra_secret))
letras_erros = []
quantidade_de_erros = 0

#tela do jogo

print(imagens.tela)
sleep(3)

while True:
    print(f'Dica: {dica}')
    print('Adivinhe a palavra: ', *palavra_escondida ,'\n') 
    letra_digitada = input('Digite uma letra: ').upper()
    
    if letra_digitada in palavra_secret:
        for i in range(0,len(palavra_secret)):
            if letra_digitada == palavra_secret[i]:
                palavra_escondida[i] = letra_digitada
    else:
        quantidade_de_erros -=1
        letras_erros.append(letra_digitada)
        print(estagios[quantidade_de_erros])   
     
    #Finalizando o laço
    if '#' not in palavra_escondida:
        print('Parabéns você adivinhou a palavra')
        break
    elif quantidade_de_erros == -7:
        print(f'Infelizmente você não acertou a palavra que era: {palavra_secret}')
        break
    elif quantidade_de_erros <0:
        print(f'Letras erradas: {letras_erros}')






