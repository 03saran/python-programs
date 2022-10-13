try:
    a=int(input("Enter first number"),2)
    b=int(input("Enter second number"),2)
    c=a+b
    print("ADD=",bin(c))
except ValueError:
    print("Invalid input")
