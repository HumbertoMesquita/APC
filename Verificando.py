frase = input().split()
tam = len(frase)
stop = 0
for i in range(tam):
    if i == ',':
        print('passed')
        stop += 1

if stop == 0:
    print('failed')