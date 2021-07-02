
# Factorizador de numeros reales:

import math 

def factorizacion(n): 
    while n % 2 == 0: 
        if len(str(n)) == 3:
            print(int(n),"|",2) 
            n = n / 2
        elif len(str(n)) == 2:
            print(int(n)," |",2) 
            n = n / 2
        
    for i in range(3, int(math.sqrt(n))+1, 2): 
        while n % i == 0: 
            if len(str(int(n))) == 3:
                print(int(n),"|",i) 
                n = n / i 
            elif len(str(int(n))) == 2:
                print(int(n)," |",i) 
                n = n / i    
            else:
                print(int(n),"  |",i) 
                n = n / i 
       
    if n > 2: 
        print(int(n)," |",int(n))
        print("1 (final)")

numero = input("\n\t--> Input the number to factorize: ")
factorizacion(int(numero))
