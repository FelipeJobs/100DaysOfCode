from turtle import Turtle,Screen
from cobrinha import Snake
from time import sleep
from comida import Comida
from placar import Placar
from os import system

tela = Screen()
tela.setup(width= 800, height= 600)
tela.bgcolor('Black') #muda a cor do plano de fundo da janela
tela.title('Jogo da cobrinha') #Coloca um nome na janela criada
tela.tracer(0) #com esse comando eu desativo a animação até chemar o método update
# corpo da cobra

cobra = Snake()
food = Comida()
score = Placar()

#Com esse laço eu crio os objetos e armazeno eles na lista segmentos
def fechar():
    return False
tela.listen()
tela.onkey(cobra.cima, 'Up')
tela.onkey(cobra.baixo, 'Down')
tela.onkey(cobra.direita, 'Left')
tela.onkey(cobra.esquerda, 'Right')
tela.onkey(tela.bye,'f') #fecha o game quando apertar a tecla 'f'

try:
    while True:
        tela.update()#faz toda a animação ser reconstruída depois da cobra estar formada
        #Com esse laço eu faço que cada quadrado da cobra assuma a posição do seu sucessor
        #dessa forma, quando eu movimentar uma parte todas as outras serão movimentadas
        # deixando todo o corpo da cobra junto. 
        sleep(0.1)
        cobra.snake_move()
        
        if(cobra.cabeca.distance(food) < 15):
            food.atualizar_posicao()
            score.aumentar_score()
            cobra.aumentar_cobra()
            
        #reinicia o game caso a cobra colida com a parede
        if(cobra.cabeca.xcor() > 390 or cobra.cabeca.xcor() <- 390 or 
        cobra.cabeca.ycor() >300 or cobra.cabeca.ycor() <-300 ):
            score.resetar()
            cobra.resetar_cobra()
            
        
        #reinicia o game caso a cobra colida com alguma parte de si mesma
        for segmento in cobra.segmentos[1:]:
        #eu usei o conceito de fatiamento de lista para evitar que a cabeça seja 
        # comparada com ela mesma porque se isso acontecesse o jogo terminaria.
            if(cobra.cabeca.distance(segmento) < 10):
                score.resetar()
                cobra.resetar_cobra()
except:
    print('Volte quando quiser')
    
