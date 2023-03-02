'''
Você vai escrever um programa que selecionará um nome aleatório de
uma lista de nomes. A pessoa selecionada terá que pagar a conta 
de alimentação de todos.

Importante: Você não tem permissão para usar a função.choice()

A linha 15 divide a cadeia de caracteres em nomes individuais e os 
coloca dentro de uma lista chamada names. Para que isso funcione, 
você deve inserir todos os nomes como nomes seguidos de vírgula e 
espaço. 
'''
# Split string method
names_string = input("Dê-me os nomes de todos, separados por uma \
vírgula ").title()
names = names_string.split(", ")
#o método split além de separar strings transforma os dados em uma
#lista.
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
from random import randint
quem_vai_pagar_a_conta = names[randint(0,len(names))]

print(f'{quem_vai_pagar_a_conta} vai pagar a refeição hoje !!!')