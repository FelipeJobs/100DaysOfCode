import menu
from time import sleep
from os import system
from prettytable import PrettyTable

tabela = PrettyTable()
lucro_total = 0
def mostrar_Preco(escolha):
    print(f'O preço do expresso é R$: {menu.MENU[escolha]["Preco"]}')
   

# com essa função vou contablizar os insumos consumidos 
def consumir_insumos(lista, escolha ):
        lista[0]['Agua'] =  lista[0]['Agua'] - menu.MENU[escolha]['Ingredientes']['Agua']
        lista[0]['Cafe']= lista[0]['Cafe'] - menu.MENU[escolha]['Ingredientes']['Cafe']
        lista[0]['Leite']= lista[0]['Leite'] - menu.MENU[escolha]['Ingredientes']['Leite']

# essa função vai impedir uma nova compra caso não tenha insumo suficiente
def vericar_insumos(lista, escolha ):
    agua_maquina = lista[0]['Agua'] - menu.MENU[escolha]['Ingredientes']['Agua']
    cafe_maquina = lista[0]['Cafe'] - menu.MENU[escolha]['Ingredientes']['Cafe']
    leite_maquina = lista[0]['Leite'] - menu.MENU[escolha]['Ingredientes']['Leite']
    if(agua_maquina > 0 and cafe_maquina > 0 and leite_maquina > 0):
        return
    else:
        return 0

# verifica se tem dinheiro suficiente para comprar o produto
def contar_dinheiro(escolha , dinheiro):
    if dinheiro >=  menu.MENU[escolha]["Preco"]:
        global lucro_total
        lucro_total +=menu.MENU[escolha]["Preco"]
    else:
        print('Desculpe, não há dinheiro suficiente. Dinheiro devolvido.')
        return 0

#função responsável pelo troco
def devolver_troco(escolha, dinheiro):
    Preco_do_produto = menu.MENU[f'{escolha}']["Preco"]
    troco = dinheiro - Preco_do_produto
    return troco

def imprimir_relatorio(lista , lucro):
    tabela.clear()
    tabela.field_names = ['Item','Quantidadade']
    tabela.add_row(['Água',f'{lista[0]["Agua"]} ML'])
    tabela.add_row(['Café',f'{lista[0]["Cafe"]} G'])
    tabela.add_row(['Leite',f'{lista[0]["Leite"]} ML'])
    tabela.add_row(['Lucro',f'{lucro:,.2f}'])
    print(tabela)
    
#As 3 funções abaixo serve para reabastecer os insumos da máquia de café
def reabastecer_maquina(item,quantidade,lista):
    if item == 1:
        lista[0]['Agua'] = lista[0]['Agua'] + quantidade
    elif item == 2:
        lista[0]['Cafe'] = lista[0]['Cafe'] + quantidade
    elif item == 3:
        lista[0]['Leite'] = lista[0]['Leite'] + quantidade

def encerrar_pedindo():
    sleep(5)
    system('cls')

def cadastrar_produto(nome,agua,cafe,leite,valor):
    menu.MENU[nome] = {
        "Ingredientes": {
            "Agua": agua,
            "Leite": cafe,
            "Cafe": leite,
        },
        "Preco": valor,
    }
    
def mostrar_produtos(dados = menu.MENU):
    for p in dados.keys():
        print(p)
    print()
    

    