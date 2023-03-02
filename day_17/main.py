class Main:
    def __init__(self, nome, idade, sexo):
        self.name = nome
        self.age = idade
        self.sexo = sexo
    
    def imprimir (self):
        print(self.name)
        print(self.age)
        print(self.sexo)

p1 = Main('Lipe',25,'M')

p1.imprimir()

