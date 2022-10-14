def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
try:
    a=int(input("Enter a number:"))
    if(a<=0):
        print("INVALID INPUT")
    else:
        print("Factorial of ",a,":",fact(a))
except ValueError:
    print("INVALLID INPUT")
