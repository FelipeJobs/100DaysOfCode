POSICOES_INICIAIS = [(0,0),(-20,0),(-40,0)] #Defini as coordenadas iniciais dos quadrados
DISTANCIA_PERCORRIDA = 20
CIMA = 90
BAIXO = 270
DIREITA = 180
ESQUERDA = 0

from turtle import Turtle
class Snake:
    
    def __init__(self):
        self.segmentos = [] # essa lista vai servir para armazenar os obj criados pelo laço abaixo.
        self.criar_cobra()
        self.cabeca = self.segmentos[0]

    def criar_cobra(self):
        for posicao in POSICOES_INICIAIS:
            square = Turtle(shape='square')
            square.color('Aquamarine')
            square.penup()
            square.goto(posicao)
            self.segmentos.append(square)
            
    
    def snake_move(self):
        for segm in range(len(self.segmentos)-1, 0, -1):
            novo_x = self.segmentos[segm -1].xcor()
            novo_y = self.segmentos[segm -1].ycor()
            self.segmentos[segm].goto(novo_x,novo_y)
        self.segmentos[0].forward(DISTANCIA_PERCORRIDA)
        
    def aumentar_cobra(self):
        square = Turtle(shape='square')
        square.color('Aquamarine')
        square.penup()
        self.segmentos.append(square)
    
    #com essas funções eu controlo o direcionamento da cobra
    
    
    def cima(self):
        if self.cabeca.heading() != BAIXO:
            self.cabeca.setheading(CIMA)

    def baixo(self):
        if self.cabeca.heading() != CIMA:
            self.cabeca.setheading(BAIXO)

    def direita(self):
        if self.cabeca.heading() != ESQUERDA:
            self.cabeca.setheading(DIREITA)

    def esquerda(self):
        if self.cabeca.heading() != DIREITA:
            self.cabeca.setheading(ESQUERDA)
    
       
#os laçoes condicionais das funções impedem que a cobra va para a direção contrária
# se o jogador apenas apertar a tecla, isso é, não pode estar indo para cima e 
# inverter o movimento para baixo do nada.
    
    #esse método reseta a cobra 
    def resetar_cobra(self):
        for seg in self.segmentos:
            seg.goto(1000,1000)
        self.segmentos.clear()
        self.criar_cobra()
        self.cabeca = self.segmentos[0]

        
        

        
        
        
        
        
