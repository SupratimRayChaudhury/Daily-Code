# print J
n=10
for i in range(n):
    for j in range(-n,n+1):
        if((j==0 and i!=n-1) or i==0 or (j==-1 and i==n-1) or (j==-2 and i==n-2)):
            print("*",end="")
        else:
            print(" ",end="")   
    print("")