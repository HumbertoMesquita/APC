a, b, a1, b1 = map(float, input().split())

final_a = a*a1
final_b = b*b1
cont = 0

while True:
    
    final_a = a*a1
    final_b = b*b1
    cont += 1
    
    if final_a+a >= final_b+b:
        print(f'Vai alcancar em {cont} ano(s).')
        exit()
        
    elif cont >= 1000:
        print('Mais de um milenio.')
        exit()
        
    
    
    
    
    
    