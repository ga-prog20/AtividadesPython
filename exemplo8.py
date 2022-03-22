import math 

num = int(input('Digite um número:'))
if num > 0:
    r = math.sqrt(num) 
    print(f'A raiz quadrada do numero é  {r:.2f}')
else:
    print('Não é possíviel calcular números negativos através de inteiros')