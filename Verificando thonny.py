frase = input().split()
stop = 0

for i in frase:
    for v in i:
        if v == ',':
            print('passed')
            stop += 1

if stop == 0:
    print('failed')