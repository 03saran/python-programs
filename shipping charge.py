def charge(a):
    c=a*200
    return c+750
a=int(input("Enter no of items :"))
if(a<=0):
    print("Invalid input")
else:
    print("Shipping charge :",charge(a-1))
