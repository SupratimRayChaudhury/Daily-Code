n=10
for i in range(-n,n+1):
    for j in range(-n,n+1):
        if(abs(j)+abs(i)<=n-1 or abs(j)==n or abs(i)==n):
            print(" * ",end="")
        else:
            print("   ",end="")   
    print("")