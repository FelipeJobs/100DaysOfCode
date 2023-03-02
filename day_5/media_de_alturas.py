#Você vai escrever um programa que calcula a altura média do 
# aluno a partir de uma lista de alturas.
#obs: não pode utilizar as funções len ou sum

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = float(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
soma_das_alturas = 0
contador = 0

for a in student_heights:
    soma_das_alturas += a
    contador += 1

media_das_alturas = round(soma_das_alturas/contador)

print(media_das_alturas)


    





