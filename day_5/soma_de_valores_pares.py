'''
Você vai escrever um programa que calcula a soma de todos os 
números pares de 1 a 100.

Importante, deve haver apenas 1 instrução de impressão na saída 
do console. Ele deve apenas imprimir o total final e não todas as 
etapas do cálculo.
'''
#Write your code below this row 👇
soma_dos_valores_pares = 0

for i in range(0,101):
    if(i % 2 == 0):
        soma_dos_valores_pares += i
        
print(soma_dos_valores_pares)
    
