x=int(input("Enter x value :"))
y=int(input("Enter N value :"))
print("1.Pow (A,B),2.Add (A,B),3.Sub (A,B),4.Mul (A,B),5.Div (A,B)")
c=int(input("Enter your choice :"))
if(c==1):
    print("Pow (X,N)=",x**y)
elif(c==2):
    print("Add (X,N)=",x+y)
elif(c==3):
    print("Sub (X,N)=",x-y)
elif(c==4):
    print("Mul (X,N)=",x*y)
elif(c==5):
    if(y==0):
        print("Denominator cant be zero ")
    else:
        print("Div (X,N)=",x/y)
    

