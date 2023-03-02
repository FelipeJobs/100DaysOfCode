from turtle import Turtle,Screen
from random import randint

tela = Screen()
altura = 500
largura = 800
tela.setup(width= largura, height = altura)
resultado = tela.textinput('Aposta', 'Qual a cor da nova_tartarugaatuga que você vai apostar')
começou_corrida = False
contador = 0
all_tartarugas = []
tela.bgpic('C:\\Users\Lipe\\Documents\\100 Days of Code The Complete Python Pro Bootcamp for 2023\day_19\\corrida\\day_19.gif')



cores = ['green','red','blue','yellow','orange','purple']

#mudar forma das nova_tartarugaarugas e cor


for tartaruga in range(6):
    nova_tartaruga = Turtle(shape= 'turtle') # com esse código eu vou criando um novo objeto cada vez que roda um laço
    nova_tartaruga.color(cores[tartaruga])
    nova_tartaruga.penup()
    nova_tartaruga.goto(x = 15 - largura/2,y = contador )
    contador +=35
    all_tartarugas.append(nova_tartaruga)
        
if(resultado != ''):
    começou_corrida = True
    
while começou_corrida:
    for tartaruga in all_tartarugas:
        if tartaruga.xcor() >=largura/2-20:
            começou_corrida = False
            cor_vencedora = tartaruga.pencolor()
            if cor_vencedora == resultado:
                print(f'Você ganhou a tartaruga {cor_vencedora} ganhou a corrida ')
            else:
                print(f'Você perdeu a tartaruga {cor_vencedora} ganhou a corrida e não\
 a {resultado}')
        distancia = randint(0, 10)
        tartaruga.forward(distancia)

tela.exitonclick()



    