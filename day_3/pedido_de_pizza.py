'''
Parabéns, você tem um emprego na Python Pizza. Seu primeiro 
trabalho é construir um programa automático de pedidos de pizza.

Com base no pedido de um usuário, calcule sua conta final.

Piza Pequena: $15

Pizza Média: $20

Pizza grande: $25

Calabresa para pizza pequena: +$2

Calabresa para pizza média ou grande: +$3

Queijo extra para pizza de qualquer tamanho: + $1
'''
# 🚨 Não altere o código abaixo 👇
print("Bem-vindo ao Python Pizza Delivery!\n")
size = input("Que tamanho de pizza você quer? S(Small),\
M(Medium) ou L(Large) ")
add_pepperoni = input("Você quer pepperoni? Y ou N ")
extra_cheese = input("Quer queijo extra? Y ou N ")
# 🚨 Não altere o código acima 👆

#Escreva seu código abaixo desta linha 👇
conta_final = 0

if(size.upper() == 'S' ):
    conta_final +=15
elif(size.upper() == 'M' ):
    conta_final += 20
elif(size.upper() == 'L' ):
    conta_final += 25

if(add_pepperoni.upper() == 'Y'):
    if(size.upper() == 'S'):
        conta_final +=2
    else:
        conta_final +=3

if(extra_cheese.upper() == 'Y'):
    conta_final +=1
    
print(f'Your final bill is: ${conta_final}.')