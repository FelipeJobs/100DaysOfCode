from time import sleep
from os import system

print('welcome to')
sleep(4)

print('''
      ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
      \n''')

sleep(3)
print("Bem-vindo a ilha do tesouro a sua missão é encontrar o tesouro")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
direcao = input('você quer ir pela esquerda ou direita? ').lower()

if(direcao == 'direita' or direcao != 'esquerda'):
    print('Você caiu em um buraco e perdeu o jogo')
else:
    nadar_ou_esperar = input('Você chegou em um lago, você quer esperar um barco(e) ou ir nadando(n? ').upper()
    if(nadar_ou_esperar == 'N' or nadar_ou_esperar != 'E') :
        print('Você foi atacado por uma truta, tente novamente')
    else:
        print('Você chegou em um local com uma porta vermelha, azul e outra amarela')
        porta_escolhida = input('Você quer entrar na porta V(vermelha), Az(azul) ou na AM(amarela)? ').upper()
        if(porta_escolhida == 'V'):
            system('cls')
            print('Você foi queimado pelo fogo')
            print('''
                                                (  .      )
                                )           (              )
                                        .  '   .   '  .  '  .
                                (    , )       (.   )  (   ',    )
                                .' ) ( . )    ,  ( ,     )   ( .
                            ). , ( .   (  ) ( , ')  .' (  ,    )
                            (_,) . ), ) _) _,')  (, ) '. )  ,. (' )

                                        ''')
        elif(porta_escolhida == 'AZ'):
            system('cls')
            print('Você foi comido pela besta')
            print('''
                  
                                                
                                                    ,--,  ,.-.
                        ,                   \,       '-,-`,'-.' | ._
                    /|           \    ,   |\         }  )/  / `-,',
                    [ '          |\  /|   | |        /  \|  |/`  ,`
                    | |       ,.`  `,` `, | |  _,...(   (      _',
                    \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                        \  \_\,``,   ` , ,  /  |         )         _,/
                        \  '  `  ,_ _`_,-,<._.<        /         /
                        ', `>.,`  `  `   ,., |_      |         /
                            \/`  `,   `   ,`  | /__,.-`    _,   `\
                        -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                        \_,,.) /\    ` /  / ) (-,, ``    ,        |
                        ,` )  | \_\       '-`  |  `(               \
                    /  /```(   , --, ,' \   |`<`    ,            |
                    /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
                ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
            (-, \           ) \ ('_.-._)/ /,`    /
            | /  `          `/ \\ V   V, /`     /
            ,--\(        ,     <_/`\\     ||      /
        (   ,``-     \/|         \-A.A-`|     /
        ,>,_ )_,..(    )\          -,,_-`  _--`
        (_ \|`   _,/_  /  \_            ,--`
        \( `   <.,../`     `-.._   _,-`
        `                      ```
                  ''')
        elif(porta_escolhida == 'AM'):
            system('cls')
            print('Parabéns você encontrou o tesouro')
            
            print('''
                                ____...------------...____
                    _.-"` /o/__ ____ __ __  __ \o\_`"-._
                    .'     / /                    \ \     '.
                    |=====/o/======================\o\=====|
                    |____/_/________..____..________\_\____|
                    /   _/ \_     <_o#\__/#o_>     _/ \_   \
                    \_________\####/_________/
                    |===\!/========================\!/===|
                    |   |=|          .---.         |=|   |
                    |===|o|=========/     \========|o|===|
                    |   | |         \() ()/        | |   |
                    |===|o|======{'-.) A (.-'}=====|o|===|
                    | __/ \__     '-.uuu/.-'    __/ \__ |
                    |==== .'.'^'.'.====|
                    |  _\o/   __  {.' __  '.} _   _\o/  _|
                    `""""-""""""""""""""""""""""""""-""""`
                  ''')
        else:
            system('cls')
            print('Você perdeu o jogo')
        

