'''
Crie um programa usando matemática e f-Strings que nos diga quantos
dias, semanas, meses nos restam se vivermos até os 90 anos de idade.

Você tem x dias, y semanas e z meses restantes.

Onde x, y e z são substituídos pelos números reais calculados.

Exemplo de entrada
56 

Exemplo de saída
You have 12410 days, 1768 weeks, and 408 months left.
'''

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇 
idade_maxima = 90
age = int(age)
idade_restante = idade_maxima - age

dias = (idade_restante * 365)
semanas = (idade_restante * int(365/7))
meses = (idade_restante *12)

print(f"You have {dias} days, {semanas} weeks, and {meses} months left.")