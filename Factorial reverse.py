# 1*2*3*4*5=120
def fact(n):
    if n>=1:
        f=n*fact(n-1)
        if n==1:
            print(n,sep="",end="")
        else:
            print("*",n,sep="",end="")
    else:
        f=1
    return f

n=int(input("Enter a number"))
f=fact(n)
print("=",f,sep="")