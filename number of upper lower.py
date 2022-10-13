print("Enter * to exit")
b=[]
e,f,g,h=0,0,0,0
while(1):
    a=input("Enter any character :")
    if(a=='*'):
        break
    else:
        b.append(a)
for i in b:
    if(i.isupper()):
        e+=1
    elif(i.islower()):
        f+=1
    elif(i.isnumeric()):
        g+=1
    else:
        h+=1
print("Total count of lowercase :",f)
print("Total count of uppercase :",e)
print("Total count of number :",g)
print("Total count of special character :",h)
