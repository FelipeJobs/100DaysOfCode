from os import system
import art
import funcionalidades

maquina_dados = [funcionalidades.menu.resources]
while True:
    try:
        print('Bem vindo a nossa cafeteria digital')
        print(art.logo)
        funcionalidades.encerrar_pedindo()
        print('O que você gostaria:')
        funcionalidades.mostrar_produtos()
        qual_cafe = input('Escolha: ').lower()
        
        
        if qual_cafe == 'cadastrar':
            nome_p = input('Qual o nome do produto? ')
            agua_u = int(input('Qual a quantidade de água utilizado para produzí-lo? '))
            cafe_u =int(input('Qual a quantidade de café utilizado para produzí-lo? '))
            leite_u = int(input('Qual a quantidade de leite utilizado para produzí-lo? '))
            preco = int(input('Qual o preço desse produto? '))
            funcionalidades.cadastrar_produto(nome_p, agua_u,cafe_u,leite_u,preco)
            funcionalidades.encerrar_pedindo()
            continue
        
        if qual_cafe == 'relatorio':
            funcionalidades.imprimir_relatorio(maquina_dados, funcionalidades.lucro_total)
            funcionalidades.encerrar_pedindo()
            continue
        
        if qual_cafe == 'reabastecer':
            item_escolhido = int(input(f'Que item você quer reabastecer{funcionalidades.mostrar_produtos(maquina_dados)}\nEscolha: '))
            funcionalidades.mostrar_produtos(maquina_dados)
            quantidade_do_item = int(input('Qual quantidade você vai inserir: '))
            funcionalidades.reabastecer_maquina(item_escolhido, quantidade_do_item, maquina_dados)
            funcionalidades.encerrar_pedindo()
            continue 
        
        if qual_cafe == 'off':
            break
        
        if funcionalidades.vericar_insumos(maquina_dados, qual_cafe) == 0:
            print('Desculpe, não há insumos suficientes')
            break
        
        else:
            funcionalidades.mostrar_Preco(qual_cafe)
            print('\nsó aceitamos notas de R$2, R$5 ou R$10\n')
            dinheiro = int(input('Que nota você irá inserir? '))
            quantidade_de_notas = int(input('Quantas notas você inseriu?  '))
            dinheiro_total = dinheiro * quantidade_de_notas
            dinheiro_suficiente = funcionalidades.contar_dinheiro(qual_cafe, dinheiro_total )
            if dinheiro_suficiente == 0:
                break
            
            else:
                system('cls')
                print(f'Aproveite o seu {qual_cafe}')
                print(f'Aqui está seu troco R$: {funcionalidades.devolver_troco(qual_cafe, dinheiro_total):,.2f}')
                funcionalidades.consumir_insumos(maquina_dados, qual_cafe)
                funcionalidades.encerrar_pedindo()
    
    except KeyError:
        print('Desculpa você escolheu uma opção inválida tente novamente')
        funcionalidades.encerrar_pedindo()
        
    except ValueError:
        print('Essa opção só aceita valores numéricos')
        funcionalidades.encerrar_pedindo()     
   
        
    
      




    
