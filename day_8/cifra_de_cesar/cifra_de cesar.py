from string import ascii_lowercase
import logo
from os import system

#lista de letras minúsculas
alfabeto = list(ascii_lowercase)
print(logo.arte)
#recebimento de dados
while True:
    escolha = input("Digite 'encode' para criptografar, digite 'decode' para descriptografar:\n").lower()
    if(escolha == 'encode' or escolha == 'decode'):
        system('cls')
        break
    else:
        print('Digite uma opção válida')
        system('cls')
        
texto = input("Digite sua mensagem:\n").lower()
while True:
    turnos = int(input("Digite o número do turno:\n"))
    if(turnos > 1 and turnos <26):
        break
    else:
        print('Digite um número de turno que esteja entre 1 e 25')

#Função necessária
#escrevi uma única função mais o ideal seria 2, visto que existe o princípio
#de responsabilidade única
def criptografar_ou_descriptografar(mensagem,turno,opcao):
    novo_texto = ''
    for letra in mensagem:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            if opcao == 'encode':
                novo_texto += alfabeto[posicao + turnos]
            elif opcao == 'decode':
                novo_texto += alfabeto[posicao - turnos]
        else:
            novo_texto += letra
    print(novo_texto)

# resultado
criptografar_ou_descriptografar(mensagem = texto, turno = turnos, opcao = escolha)


        





                