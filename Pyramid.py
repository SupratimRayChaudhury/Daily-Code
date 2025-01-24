n=10
for i in range(n):
    for j in range(-n,n+1):
        if(abs(j)>=i):
            print("   ",end="")
        else:
            print(" @ ",end="")   
    print("")