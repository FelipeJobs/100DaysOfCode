'''
Você está pintando uma parede. As instruções na lata de tinta dizem que 1 lata 
de tinta pode cobrir 5 metros quadrados de parede. Dada uma altura e largura 
aleatórias de parede, calcule quantas latas de tinta você precisará comprar.
'''

#Write your code below this line 👇
import math
def tinta_necessaria (altura,comprimento,rendimento):
    
    resultado = int(math.ceil((altura * comprimento)/rendimento))
    print(f'Você vai precisar de {resultado} latas de tinta(s)')
#math.ceil retorna o menor inteiro que é maior ou igual ao valor de entrada. 
# Essa função trata a entrada como um float, seu quiser um int eu preciso converter.

#Write your code above this line 👆
# Define a function called tinta_necessaria () so that the code below works.   

# 🚨 Don't change the code below 👇
altura = int(input("A altura da parade é: "))
comprimento = int(input("O comprimento da parede é: "))
rendimento_por_metro_quadrado = 5
tinta_necessaria (altura=altura, comprimento=comprimento, rendimento=rendimento_por_metro_quadrado)