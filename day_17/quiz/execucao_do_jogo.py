from funcionalidades import FuncionalidadeQuiz
from os import system
from time import sleep
import art
import perguntas

lista_perguntas = perguntas.question_data
funcionalidades = FuncionalidadeQuiz()

# lógica para unir todas as partes e fazer o jogo funcionar
def executar_jogo(lista = lista_perguntas):
    print('Bem vindo ao nosso Jogo')
    print(art.logo)
    sleep(3)
    while True:
        system('cls')
        resposta = input(f'Pergunta {funcionalidades.indice_pergunta+1}: {funcionalidades.escolher_pergunta(lista_perguntas)}\
(True or False): ').title()
        # impede que o usuário digite uma resposta inválida
        if(resposta != "True" and resposta != "False"):
            print('Digite apenas True Ou False')
            funcionalidades.indice_pergunta -=1
            sleep(4)
            continue
        
        resposta_da_questão = funcionalidades.verificar_resposta(lista_perguntas)
    
        comparacao = funcionalidades.comparar_resposta(resposta, resposta_da_questão)
    
        # garante que o jogo terminará se o jogador acertar todas as questões
        if (funcionalidades.indice_pergunta == len(lista)):
            print(f'Incrível você acertou todas as {len(lista)} perguntas')
            break
        
        elif(comparacao == 'True'):
            print('Você acertou !!!!')
            funcionalidades.pontuar()
            print(f'Por enquanto você acertou {funcionalidades.pontos} pergunta(s)')
       
        # finaliza o jogo se o jogador errar alguma questão
        else:
            print(f'Desculpa você errou, a resposta correta era: {resposta_da_questão}')
            print(f'Total de acertos: {funcionalidades.pontos}')
            break
        sleep(5)

        






    
    

    
       
        




    


