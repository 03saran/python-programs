def matches(a,b):
    c=len(a)
    d=len(b)
    e=0
    for i in range(max(c,d)):
        if(i<c):
            if(i<d):
                if(a[i]==b[i]):
                    e+=1
    return e
a=input("Enter 1st string :")
b=input("Enter 2nd string :")
print("Matches :",matches(a,b))
