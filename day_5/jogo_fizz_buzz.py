'''
Você vai escrever um programa que imprime automaticamente a 
solução para o jogo FizzBuzz.

Seu programa deve imprimir cada número de 1 a 100.

Quando o número é divisível por 3, em vez de imprimir 
o número, ele deve imprimir "Fizz".

Quando o número é divisível por 5, então, em vez de imprimir o
número, ele deve imprimir "Buzz".'

E se o número é divisível por 3 e 5, por exemplo, 15, em vez do 
número, ele deve imprimir "FizzBuzz"
'''
for n in range(1,101):
    if(n% 3 == 0 and n% 5 == 0):
        print('FizzBuzz')
        
    elif(n % 3 == 0):
        print('Fizz')
        
    elif(n% 5 == 0):
        print('Buzz')
    else:
        print(n)
  
   