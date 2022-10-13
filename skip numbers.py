a=[]
print("1. Start value,2. End value,3. Skip value")
for i in range(3):
    b=int(input())
    a.append(b)
c=a[0]
d=a[1]
e=a[2]
if(d>c):
    if(e>0):
        for i in range(c,d,e+1):
            print(i)
    else:
        print("INVLAID INPUT")
else:
    print("INVALID INPUT")
    
    
