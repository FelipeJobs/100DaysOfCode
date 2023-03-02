from turtle import Turtle
from random import randint

class Comida(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.color('blue')
        self.penup()
        self.speed('fastest')
        self.atualizar_posicao()
    
    def atualizar_posicao(self):
        x = randint(0,380)
        y = randint(0,280)
        self.goto(x,y)
    