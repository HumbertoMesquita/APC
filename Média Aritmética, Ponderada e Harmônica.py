n1, n2, n3 = map(int, input().split())
modo = input()

if modo == "A":
    print('Aritmetica')
    print(f'{(n1+n2+n3)/3:.2f}')
    
elif modo == "P":
    p1, p2, p3 = map(int, input().split())
    print('Ponderada')
    print(f'{(n1*p1+n2*p2+n3*p3)/(p1+p2+p3):.2f}')
    
    
elif modo == "H":
    print('Harmonica')
    print(f'{3/(1/n1+1/n2+1/n3):.2f}')
    
else:
    print('Operacao inexistente')
    