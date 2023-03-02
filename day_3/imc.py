'''
Escreva um programa que interprete o Índice de Massa Corporal 
(IMC) com base no peso e altura de um usuário.

Deve dizer-lhes a interpretação do seu IMC com base no valor do 
IMC.
'''
# 🚨 Não altere o código abaixo 👇
height = float(input("digite sua altura em m: "))#altura
weight = float(input("digite seu peso em kg: "))#peso
# 🚨 Não altere o código acima 👆

#Escreva seu código abaixo desta linha 
valor_imc = round(weight/(height ** 2))

#abaixo do peso
if(valor_imc <18.5):
     print(f"Your BMI is {valor_imc}, you are underweight.")
#peso normal     
elif(valor_imc <25):
    print(f"Your BMI is {valor_imc}, you have a normal weight.")
#acima do peso   
elif(valor_imc <30):
    print(f"Your BMI is {valor_imc}, you are slightly overweight.")
#obesos    
elif(valor_imc <35):
     print(f"Your BMI is {valor_imc}, you are obese.")
#muito obesos    
else:
    print(f"Your BMI is {valor_imc}, you are clinically obese.")