b=[]
b1=[]
c=[]
a=int(input("Enter length of list1 :"))
for i in range(a):
    d=int(input("Enter number :"))
    b.append(d)
a1=int(input("Enter length of list2 :"))
for i in range(a1):
    d1=int(input("Enter number :"))
    b1.append(d1)
c=b+b1
c.sort()
print(c)


