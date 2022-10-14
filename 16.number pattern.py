b=1
a=int(input("Enter number of rows :"))
if(a<=0):
    print("INVALID NUMBER OF ROWS")
else:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(b,end=" ")
            b+=1
        print()
