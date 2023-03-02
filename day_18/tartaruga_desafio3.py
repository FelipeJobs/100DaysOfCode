# O objetivo desse desafio em desenhar os poligonos regulares um após o outro
# e no final teremos um desenho de todo um sobrepondo o outro.

from turtle import Turtle
from time import sleep
cores = ['BlueViolet','Sienna1','RoyalBlue','VioletRed','black','gold','DarkGreen','DarkBlue']

tart = Turtle()
for i in range(2,10):
    conta_cores = 9-i
    tart.color(cores[conta_cores])
    contador = i+1
    angulo = 360/contador
    
    for i in range(0,contador):
        tart.forward(80)
        tart.right(angulo)
        sleep(0.3)       
sleep(5)
    