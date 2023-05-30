frase = input()
final = ''
    
tam = len(frase)
for i in range(tam):
    if i%2 != 0:
        final += frase[i]
           
            
print(final.replace(" ", ""))
            
        