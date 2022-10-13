def simple(p,y,r):
    s=(p*y*r)/100
    print("Interest =",s)
p=int(input("Enter principal amount :"))
y=int(input("Enter no of years :"))
c=input("Is customer id senior citizen (y/n):")
if(p<=0 or y<=0 ):
    print("INVALID INPUT")
else:
    if(c=='y'):
        simple(p,y,12)
    else:
        simple(p,y,10)
        
