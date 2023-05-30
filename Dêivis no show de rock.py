total_ingressos, valor_ingressos = map(int, input().split())

valor_total = 0

for vez in range(1,total_ingressos+1):
    amigo = int(input())
    valor_total += amigo
    
media = int(valor_total/total_ingressos)
print(f'media: {media}')

if media >= valor_ingressos:
    print('o rock reinara mais uma vez')
    
else:
    print('rockeiros trabalhando ja')
    
