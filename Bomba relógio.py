def contador(tempo, recorde):
    if tempo != 5 and tempo != 1 and tempo > 0:
        print(f'Atenção faltam {tempo} segundos...')
        contador(tempo-1, recorde)
        
    elif tempo == 5:
        print('Seu tempo está acabando!')
        contador(tempo-1, recorde)
        
    elif tempo == 1 and  recorde < tempo:
        print('Seja rápido. Falta 1 segundo')        
        
        
        
    

tempo= int(input())
recorde = int(input())
contador(tempo, recorde)

if recorde >= tempo and tempo != 0:
    print('Bomba desativada automaticamente!')
   
elif tempo == 0:
    print('Cabum!!!! Explodiu')

else:
    if tempo == 1 and  recorde < tempo:
        print('Seja rápido. Falta 1 segundo')
        
    else:
        
        print('Seja rápido. Falta 1 segundo')
        print('Cabum!!!! Explodiu')

