'''
Você vai escrever um programa que calcula a pontuação mais alta 
de uma lista de pontuações.
Importante que você não tem permissão para usar as funções max ou 
min.
'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maior_valor = 0

for notas in student_scores:
    if(notas > maior_valor):
        maior_valor = notas

print(f'The highest score in the class is: {maior_valor}')
    



