'''
Você tem acesso a um banco de dados de no formato de um dicionário. 
As chaves são os nomes dos alunos e os valores são suas pontuações no exame.
student_scoresstudent_scores

Escreva um programa que converta suas pontuações em notas. No final do seu
programa, você deve ter um novo dicionário chamado que deve conter nomes de 
alunos para chaves e suas notas para valores. Aversão final do dicionário será 
verificada.student_grades

Critérios de pontuação:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"
'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = {}

for estudante in student_scores:
    score = student_scores[estudante]
    
    if score >= 91 and score <= 100:
        student_grades[estudante] = "Outstanding"
    elif score >=81 and score <=90:
        student_grades[estudante] = "Exceeds Expectations"
    elif score >=71 and score <=80:
        student_grades[estudante] = "Acceptable"
    else:
        student_grades[estudante] = "Fail"
        
# 🚨 Don't change the code below 👇
print(student_grades)