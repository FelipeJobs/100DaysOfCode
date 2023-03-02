#Write your code below this line 👇
def prime_checker(number):
    e_primo = True
    #checa se o número é dívisivel somente por ele mesmo, desconsiderando o 1
    for i in range(2, number):
        if number % i == 0:
            e_primo = False
    
    if e_primo:
        print("O número é primo")
        
    else:
        print("O número não é primo")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Qual número você quer checar? : "))
prime_checker(number=n)