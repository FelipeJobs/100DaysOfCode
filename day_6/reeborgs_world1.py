'''
link do desafio
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

Código: 
'''
def direita():
    turn_left()
    turn_left()
    turn_left()
   
def pular():
    #esse laçõ serve só para o ínício
   while front_is_clear():
    move()
turn_left()
    #Com esse laço abaixo eu vou encaminhando o boneco para a direita
    #já que o goal fica sempre na direita
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
pular()

#esse código funciona do hardie one até o hardie four e no maze.