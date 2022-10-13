try:
    b=input("Enter a number :")
    r=0
    a=int(b)
    if(a<0):
        c=b[0]
        d=b[1:]
        e=int(d)
        while(e>0):
            d=e%10
            r=(r*10)+d
            e=e//10
        print("Reverse number :",c,r)
    else:
        while(a>0):
            d=a%10
            r=(r*10)+d
            a=a//10
        print("Reverse number :",r)
except ValueError:
    print("INVLAID INPUT")
