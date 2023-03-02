import funcoes_necessarias

while True:
     escolha = input('Você quer jogar uma partida de Blackjack? Digite s(sim) ou n(nao): ').lower()
     
     if(escolha == 's'):
        funcoes_necessarias.jogar()
     else:
        funcoes_necessarias.limpar_console()
        print('Obrigado por visitar o nosso jogo')
        break