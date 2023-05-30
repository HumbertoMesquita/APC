frase = input().split()
quant = 0

for i in frase:
    for v in i:
        if v.isnumeric() == True:
            quant += 1
        
        
print(quant)
