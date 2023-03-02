
from turtle import Turtle,Screen

tart = Turtle()
tela = Screen()

tart.shape('turtle')

#Funções necessárias
def mover_frente():
    tart.forward(20)

def mover_atras():
    tart.backward(20)

def mover_horario():
    tart.right(15)

def mover_anti_horario():
    tart.left(15)

def limpar():
    tart.clear()
    tart.penup()
    tart.home()
    tart.pendown()

#executando código
tela.listen()
tela.onkey(mover_frente, 'Right')
tela.onkey(mover_atras, 'Left')
tela.onkey(mover_anti_horario,'Down')
tela.onkey(mover_horario,'Up')
tela.onkey(limpar, 'c')
tela.exitonclick()
    

