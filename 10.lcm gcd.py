from math import gcd
print("1.LCM and GCD of 2 digit numbers ")
print("2.LCM and GCD of 3 digit numbers ")
h=int(input("Enter your choice :"))
if (h==2):
    def lcm(x, y, z):
        a=gcd(x, y, z)
        num = x
        num2 = y * z // a
        LCM = num * num2 // a
        return LCM
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
    z = int(input("Number 3: "))
    print("The LCM Of " + str(x) + "," + str(y) + "," + str(z) +"=" + str(lcm(x, y, z)))
    print("The GCD Of " + str(x) + "," + str(y) + "," + str(z) +"=" + str(gcd(x, y, z)))
elif (h==1):
    def lcm(x, y):
        a=gcd(x, y)
        num=x
        num2=y
        LCM=num * num2 // a
        return LCM
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
    print("The LCM Of " + str(x) + "," + str(y) + "=" + str(lcm(x,y)))
    print("The GCD Of " + str(x) + "," + str(y) + "=" + str(gcd(x,y)))
else:
    print("INVALID INPUT")
