pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
from random import randint
from os import system

opcoes = [pedra,papel,tesoura]

escolha = int(input('Digite 1 para Pedra, 2 para Papel, 3 para Tesoura\n'
'Escolha: '))

jogada_do_humano = opcoes[escolha -1]
jogada_da_maquina = opcoes[randint(0, 2)]

#impressão
system('cls')
print(jogada_do_humano)
print('\nComputer chose')
print(jogada_da_maquina)

#Lógica para gerar o resultado
if(jogada_do_humano == tesoura and jogada_da_maquina == papel
   or jogada_do_humano == papel and jogada_da_maquina == pedra
   or jogada_do_humano == pedra and jogada_da_maquina == tesoura):
    print('you is winner')
elif(jogada_do_humano == jogada_da_maquina):
    print('Draw')
else:
    print('you lose')
    
    


