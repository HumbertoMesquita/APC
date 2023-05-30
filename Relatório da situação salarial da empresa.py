tam = int(input())
media = 0
ultimo = 0
nome_maior = ''
salario_maior = 0

menor = 100000000000000000000000000000
nome_menor = ''
salario_menor = 0


if tam == 0:
    print('Não tem média')
    print('Não tem')
    print('Não tem')
    
else:
    for i in range(1,tam+1):
        nome, salario = input().split(',')
        salario = float(salario)
        
        media += salario
        
        if salario > ultimo:
            nome_maior = nome
            salario_maior = salario
            ultimo = salario
            
        if salario < menor:
            nome_menor = nome
            salario_menor = salario
            menor = salario
            
    print(f'{media/tam:.2f}')
    print(f'{nome_maior} {salario_maior:.2f}')
    print(f'{nome_menor} {salario_menor:.2f}')
   
            
            