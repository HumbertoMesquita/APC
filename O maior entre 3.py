def max2(a,b):
    if a>b:
        return a
    else:
        return b


def max3(a, b, c):

    valor = max2(a, b)
    if valor >= c:
       return valor

    else:
        return c

print(max3(-1,-2,-3))


