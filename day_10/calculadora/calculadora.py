from os import system
from time import sleep
import art

#Funções
def imprimindo_operacoes():
    for operaçao in operacoes:
        print(operaçao)

def atrasar():
    return sleep(2)

def somar(n1, n2):
  return n1 + n2
 
def subtrair(n1, n2):
  return n1 - n2
 
def multiplicar(n1, n2):
  return n1 * n2
 
def dividir(n1, n2):
  return n1 / n2

#dicionário com as operações, utilizamos ele para executar a função de acordo 
#com a operação escolhida. 
operacoes = {
    '+':somar,
    '-':subtrair,
    '/':dividir,
    '*':multiplicar
}
 
#lógica para receber os valores e realizar a operação e da tela
print(art.logo)
atrasar()
try:
    numero_1 = float(input('Digite o primeiro número: '))

    while True:
        imprimindo_operacoes()
        operacao_escolhida = input('Qual operação você deseja realizar: ')
        if operacao_escolhida not in operacoes:
            print('Digite uma operação válida\n')
            continue
        proximo_numero = float(input('Digite o próximo número: '))
        resultado = operacoes[operacao_escolhida](numero_1,proximo_numero)
        numero_1 = resultado

        print(f'{numero_1} {operacao_escolhida} {proximo_numero} = {resultado}\n')
        print(f'Você deseja utilizar o número {resultado} para realizar outra operação\n')
        atrasar()
        escolha = input('y(sim) ou no(não): ').lower()
        system('cls')
        print(f'O valor registrado é: {resultado}')
        
        if(escolha == 'no'):
            break
    
except ValueError:
    print('Você digitou um valor que não é numérico por isso o programa foi \
finalizado.')