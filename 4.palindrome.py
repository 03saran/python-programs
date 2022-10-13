try:
    a=int(input("Enter a number :"))
    if(a==0):
        print("Output: False")
        print("Explanation: Its a single value we cant check its palindrome or not ")
    else:
         temp=a
         rev=0
         while(a>0):
             d=a%10
             rev=rev*10+d
             a=a//10
         if(temp==rev):
             print("Output : True")
             print("Its a palindrome")
         else:
             print("Output : False")
             print(" It is not a palindrome")
except ValueError:
             print("Enter a positive integer")
