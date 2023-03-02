from turtle import Turtle

class Placar(Turtle):
    
    def __init__(self):
        super().__init__()
        self.caminho = "jogo\\texto.txt"
        with open(self.caminho,'r') as pontuacao:
            self.high_score = int(pontuacao.read())
        self.score = 0
        self.goto(0,265)
        self.color('white')
        self.hideturtle()
        self.atualizar_placar()
       
        
    def aumentar_score(self):
        self.score +=1
        self.atualizar_placar()

    #com esse método eu acumulo a maior pontuação 
    def resetar(self):
        if(self.score > self.high_score):
            with open(self.caminho,'w') as salvar:
                salvar.write(str(self.score))
            self.high_score = self.score
                
        self.score = 0
        self.atualizar_placar()
    
    def atualizar_placar(self):
        self.clear()
        self.write(f'Score: {self.score}  High Score: {self.high_score}', align= 'center', font= ('arial', 18 , 'normal'))
        