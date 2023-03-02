import paleta_de_cores
from random import choice
from turtle import Turtle,Screen

tart = Turtle()
tela = Screen()
paleta = paleta_de_cores.rgb_cores
tart.speed(15)
tela.colormode(255)
tart.hideturtle() #deixa o cursor invisível

# posiciona o cursor antes de começar o desenho
def posicionar_tartaruga():
    tart.penup()
    tart.right(180)
    tart.forward(200)
    tart.left(90)
    tart.forward(300)
    tart.left(90)
    tart.pendown()
# Escolhe uma das cores da lista
def escolher_cor():
    return choice(paleta)

def desenhar_quadro(linhas, colunas):
    posicionar_tartaruga()
    # Esse laço contra o número de linhas da pintura
    for l in range(1,(linhas+1)):
    #Esse segundo laço controla a quantidade de colunas da pintura
        for c in range(colunas):
            cor = escolher_cor()
            tart.dot(15,cor) #faz com que seja desenhado pontos
            tart.penup()
            tart.forward(20)
        # Esse laço condicional e o else faz o cursor entrar na posição correta
        # para continuar desenhando acima na posição correta.
        if l % 2 == 0 and l != 0:
            tart.right(90)
            tart.forward(30)
            tart.right(90)
            tart.forward(20)
        
        else:
            tart.left(90)
            tart.forward(30)
            tart.left(90)
            tart.forward(20) 
    # Faz com que assim que acabe o laço eu feche a janela com um click 
    if(l == linhas):
        tela.exitonclick()

desenhar_quadro(10, 10)




