import string
from random import choice

#gera listas com todos os caracteres possíveis
letras_minusculas = list(string.ascii_lowercase)#gera letras Minúsculas
letras_maiusculas = list(string.ascii_uppercase)#gera letras Maiúsculas
numeros = list(string.digits)#gera digitos numéricos
caracters = list(string.punctuation)# gera símbolos


total_de_letras = int(input('Quantas letras a senha deve ter? '))
numero_de_letras_maiusculas = int(input('Quantas letras maiúsculas a senha deve ter? '))
quantidade_de_numeros = int(input('Quantos números deve ter? '))
quantidade_de_simbolos = int(input('Quantos caracteres especiais deve ter? '))
numero_de_digitos = total_de_letras  + quantidade_de_numeros + quantidade_de_simbolos

senha = ''
armazena_valores = list(senha)#armazena os digitos da senha

#gerando os valores da senha
while True:
        for i in range(0,numero_de_letras_maiusculas):
                        armazena_valores.append(choice(letras_maiusculas))
                        
        for i in range(0,quantidade_de_simbolos):
                        armazena_valores.append(choice(caracters))
                        
        for i in range(0,quantidade_de_numeros):
                       armazena_valores.append(choice(numeros))
                        
        for i in range(0,(total_de_letras - numero_de_letras_maiusculas)):
                        armazena_valores.append(choice(letras_minusculas))
        
        if len(armazena_valores) == numero_de_digitos:
                break
   
# emabaralhando valores
for i in range(0,len(armazena_valores)):
       senha += choice(armazena_valores)
       armazena_valores.remove(senha[i])

#resultado final
print(f'A senha gerada foi: \n{senha}')
#seu quisesse poderia utilizar o método shuffle do modulo rando