from turtle import Turtle
from time import sleep

# O objetivo desse desafio é desenhar um quadrado pontilhado

tartaruga = Turtle()
tartaruga.shape('turtle')
tartaruga.color('green')
for i in range(4):
    for i in range (10):
        tartaruga.forward(10)
        tartaruga.penup()
        tartaruga.forward(10)
        tartaruga.pendown()
        sleep(0.5)
    tartaruga.left(90)