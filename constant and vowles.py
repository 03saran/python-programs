a=input("Enter a string :")
v,c=[],[]
for i in range(len(a)):
    if(a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O'or a[i]=='U' or a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
        v.append(a[i])
    else:
        c.append(a[i])
print("vowles :",*v)
print("Constant :",*c)
