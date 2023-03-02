'''
Você vai escrever um programa que testa a compatibilidade entre 
duas pessoas.

Para calcular a pontuação de amor entre duas pessoas:

Pegue os nomes de ambas as pessoas e verifique o número de vezes 
que as letras na palavra TRUE ocorrem.

Em seguida, verifique o número de vezes que as letras na palavra 
AMOR ocorrem.

Em seguida, combine esses números para criar um número de 2 
dígitos.
'''

# 🚨 Não altere o código abaixo 👇
print("Bem-vindo à Calculadora do Amor!")
name1 = input("Qual é o seu nome? \n")
name2 = input("Qual é o nome dele(a)? \n")
# 🚨 Não altere o código acima 👆

#Escreva seu código abaixo desta linha 👇
novo_nome = (name1 + name2).lower()

t = novo_nome.count('t')
r = novo_nome.count('r')
u = novo_nome.count('u')
e = novo_nome.count('e')

l = novo_nome.count('l')
o = novo_nome.count('o')
v = novo_nome.count('v')

contador_true = str(t+ r +u +e)
contador_love = str(l+o+v+e)
final_number = int(contador_true + contador_love)


if (final_number < 10) or (final_number > 90):
  print(f"Sua pontuação é {final_number}, vocês combinam como coca e mentos.")

elif (final_number >= 40) and (final_number <= 50):
    
  print(f"Sua pontuação é {final_number}, vocês estão bem juntos.")
else:
  print(f"Sua pontuação é {final_number}.")

