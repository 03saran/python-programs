a=float(input("Enter a year :"))
if(a<=0):
    print("Entered year is invalid")
else:
    if(a!=int(a)):
        print("Year cant be decimal")
    else:
        if(a%4==0 or a%400==0):
            print("The year is leap year")
        else:
            print("The year is not leap year")
            b=int(a)
            while(b>0):
                b=b-1
                if(b%4==0):
                    break
            print("LEAP YEAR =",b)
                
            
            
