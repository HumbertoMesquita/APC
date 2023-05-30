def mdc(a, b):
    r = a%b
    if a%b > 0 and b > 0:
         return mdc(b, r)
        
        
    else:
        return b



print(mdc(105,60))
