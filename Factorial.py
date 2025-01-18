# 5*4*3*2*1=120
def fact(n):
    if n>=1:
        if n==1:
            print(n,end="")
        else:
            print(n,end="*")
        return n*fact(n-1)
    else:
        return 1

n=int(input("Enter a number"))
f=fact(n)
print("=",f)