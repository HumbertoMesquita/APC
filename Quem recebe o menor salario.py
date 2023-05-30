ultimo = 100000000000000000000000
funcio = ''
while True:
    nome, salario = input().split(',')
    salario = float(salario)
    
    if nome == 'Fim' and ultimo != 100000000000000000000000:
        print(f'{funcio}')
        exit()
        
    elif nome == 'Fim':
        print('Não tem')
        exit()
        
    else:
        if salario <= ultimo and nome != 'Fim':
            ultimo = salario
            funcio = nome
            
        else:
            pass
            