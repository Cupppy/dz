count = 0
def STRING(n):
    global count
    count += 1
    k=(len(n),n.upper(),n.lower())
    return(k)
def ISC(n,m):
    global count
    count += 1
    l=[]
    for i in range(len(m)):
        p = m[i]
        p=p.lower()
        if n == p:
            return True
    return False


a='pop'
b=['POr','kok','son','POp']
STRING(a)
STRING(a)
STRING(a)
STRING(a)
ISC(a,b)
ISC(a,b)
ISC(a,b)
print(STRING(a),ISC(a,b),count)
