# nessa classe temos todas as funções que serão necessárias para gerir o
# funcionamento do jogo

class FuncionalidadeQuiz:
    
    def __init__(self):
        self.indice_pergunta = 0
        self.pontos = 0
        
    # verifica se a resposta do jogador e da pergunta são a mesma
    def comparar_resposta(self,resposta_do_jogador,resposta_da_pergunta):
        if resposta_do_jogador == resposta_da_pergunta:
            return 'True'
        return 'False'

    # pega uma das perguntas do banco de dados de questões  
    def escolher_pergunta(self,lista):
        texto = lista[self.indice_pergunta]['texto']
        self.indice_pergunta +=1
        return texto

    # retorna a resposta da questão escolhida
    def verificar_resposta(self,lista ):
        return lista[self.indice_pergunta -1]['resposta']

    # controla a pontuação do jogador
    def pontuar(self):
        self.pontos +=1










    
    

    
       
        




    


