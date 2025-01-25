# draw the following pattern using only one for loop.
#          *
#        * *
#      * * *
#    * * * *

b=False
n=int(input("Enter range:"))
for i in range(1,n*n+1):
    if(i%(n-1)==1 and i!=1):
        b=True
    if(b):
        print(" * ",end="")
    else:
        print("   ",end="")
    if(i%n==0):
        print("")
        b=False