'''
Você vai escrever um programa de lançamento de moeda virtual. 
Ele dirá aleatoriamente ao usuário "Cara" ou "Coroa".

Importante, a primeira letra deve ser maiúscula e escrita 
exatamente como no exemplo, por exemplo, Cara, não cara.
'''

from random import randint

numero_aleatorio = randint(0,1)
escolhas = ['cara','coroa']

print(escolhas[numero_aleatorio].title())
# o método title converte a primeira letra da string para maiúscula.  

