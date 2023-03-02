# O objetivo é desenhar um caminho aleatório e colorido
from random import choice,randint
from turtle import Turtle,Screen

direcoes = [0,90,180,270] # com esses valores de angulos eu consigo mover nas 4 direções
tela = Screen()
tart = Turtle()
tart.speed(20) #aumenta a velocidade 
tart.pensize(10) #aumenta o tamanho dos traços
tela.colormode(255) #permite que eu use o rgb para gerar as cores

# com essa função eu preencho o rgb para gerar um cor aleatória
def cor_aleatoria ():
    a = randint(0,255)
    b = randint(0,255)
    c = randint(0,255)
    return (a,b,c)

def desenhar_caminho():   
    for i in range(0,250):
        tup = cor_aleatoria()
        tart.pencolor(tup)
        tart.shape('turtle')
        tart.setheading(choice(direcoes))
        tart.forward(35)
    tela.exitonclick()

desenhar_caminho()
    
