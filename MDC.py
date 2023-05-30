def mdc(a, b):
    if a%b == 0 and b > 0:
        r = a%b

        mdc(b, r)
        
    elif b == 0:
        return a



print(mdc(105,60))

