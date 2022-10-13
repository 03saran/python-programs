print("Enter * to exit")
a=[]
while(1):
    b=input("Enter a string :")
    if(b=='*'):
        break
    else:
        a.append(b)
a.sort()
c=input("Order(A/D):")
if(c=='A' or c=='a'):
    for i in a:
        print(i)
elif(c=='D' or c=='d'):
    c=[]
    c=a[::-1]
    for i in a:
        print(i)
else:
    print("Enter order is wrong")
    
