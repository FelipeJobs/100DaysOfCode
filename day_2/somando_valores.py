'''
Escreva um programa que adicione os dígitos em um número de 2 
dígitos. por exemplo, se a entrada foi 35, então a saída deve ser
3 + 5 = 8

Aviso. Não altere o código nas linhas 1-3. Seu programa deve 
funcionar para diferentes entradas. por exemplo, qualquer número 
de dois dígitos.
'''

two_digit_number = input("Type a two digit number: ")

resultado =int(two_digit_number[0]) + int(two_digit_number[1])

print(resultado)