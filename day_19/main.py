from turtle import Turtle,Screen

tart= Turtle()  
tela = Screen()

def mover_forward():
    tart.forward(10)

tela.listen()#esse método serve para capturar eventos, se ele não for chamado os
# eventos não serão capturados e consequentemente não serão ativados

tela.onkey(mover_forward,'space')#esse método ativa uma função quando a tecla 
# estipulada for pressionada, lembrando que passo a função como input, ou seja
# sem utilizar os parênteses pq seu utilizar eu estarei chamando a função.

tela.exitonclick()
