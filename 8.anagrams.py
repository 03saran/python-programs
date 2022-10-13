def anag(a):
    g={}
    for w in a:
        d=''.join(sorted(w))
        if d not in g:
            g[d]=[w]
        else:
            g[d]+=[w]
    for i in g:
        f.append(g[i])
    return f
try:
    b=int(input("Enter no of srings in a list:"))
    a=[]
    f=[]
    for i in range(0,b):
        c=input("Enter Strings:")
        a.append(c)
    print("Output:",anag(a))
except ValueError:
    print("INVALID")
