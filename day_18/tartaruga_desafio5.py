# Nesse desafio eu preciso fazer o desenho de um Espirógrafo

from turtle import Turtle,Screen
from random import randint

tart = Turtle()
tela = Screen()
tela.colormode(255)
tart.speed(20)

def cor_aleatoria ():
    a = randint(0,255)
    b = randint(0,255)
    c = randint(0,255)
    return (a,b,c)

def desenhar_espirografo(tamanho):
    for i in range (80):
        cores = (cor_aleatoria())
        tart.pencolor(cores)
        tart.circle(100)
        tart.setheading(tart.heading() + tamanho)
    tela.exitonclick()

desenhar_espirografo(20)

# O heading() começa em zero e sempre vai acumulando o valor
# anteior até chegar em 360, quando isso ocorre ele volta a ser zero
# dessa forma utilizei ele para ir mudando a direção do meu desenho