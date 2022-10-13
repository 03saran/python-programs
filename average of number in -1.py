print("Enter -1 to exit")
b=[]
while(1):
    a=int(input("Enter a number :"))
    if(a==-1):
        break
    else:
        b.append(a)
e,o,f,q=0,0,0,0
for i in b:
    if(i<0):
        e+=1
        f+=i
    else:
        o+=1
        q+=i
print("Average of negative number :",f/e)
print("Average of positive number :",q/o)
