try:
    a=int(input("A="))
    b=int(input("B="))
    #1 with temp variable
    c=a
    a=b
    b=c
    print("After swapping using 3rd variable")
    print("A=",a,"B=",b)
    #2 with out temp variable
    a=a+b
    b=a-b
    a=a-b
    print("After swapping without using 3rd variable")
    print("A=",a,"B=",b)
    #3 using tuple assignment
    (a,b)=(b,a)
    print("After swapping using tuple assignment")
    print("After swapping =",a,",",b)
except ValueError:
    print("Entered input is not number")
