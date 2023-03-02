import art
import produtos
from random import choice
from time import sleep
from os import system

produto_leiloado = choice(produtos.produtos)
lances = []
vencedor = ''
maior_lance = 0

#Função que adiciona os lances na lista
def adicionar_lances(nome, valor):
    lances.append({'Nome': nome, 'Valor': valor})

#tela
print('Bem vindo ao nosso leilão virtual')
print(art.logo)
sleep(2)
print(f'O item leiloado hoje será {produto_leiloado}\n')

while True:
    nome = input("Qual é o seu nome?: ")
    preco = int(input("Qual é o seu lance? R$: "))
    adicionar_lances(nome = nome, valor = preco)
    continuar = input('Existem outros licitantes? Digite sim ou não? ').lower()
    if(continuar == 'sim'):
        system('cls')
        continue
    elif(continuar == 'não'):
        break
    else:
        print('Escolha uma opção válida(sim/não)')

#resultado
for dados in lances:
    if(dados['Valor'] > maior_lance):
        maior_lance = dados['Valor']
        vencedor = dados['Nome']
        
system('cls')

print(f'O vencedor(a) é {vencedor} com um lance de R$: {maior_lance}, parabéns aproveite \
o item: {produto_leiloado}')


