a=float(input("Enter number of rows :"))
if(a<=0 or int(a)!=a):
    print("INVALID NUMBER OF ROWS")
else:
    b=int(a)
    for i in range(1,b+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
