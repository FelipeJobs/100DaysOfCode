from turtle import Turtle,Screen
from time import sleep

# O objetivo desse desafio é criar um programa que desenha todos os polígonos
# regulares

def desenhar_poligono(lados):
    tartaruga = Turtle()
    tela = Screen()
    angulo = 360/lados
    
    if(lados <= 10 and lados >=3):
        for lado in range(0,lados):
            sleep(1)
            tartaruga.color('blue')
            tartaruga.shape('turtle')
            tartaruga.forward(80)
            tartaruga.left(angulo)
        sleep(3)
    else:
        print('O número de lados pode varia de 3 a 10, digite uma numeração válida')
    
desenhar_poligono(3)

