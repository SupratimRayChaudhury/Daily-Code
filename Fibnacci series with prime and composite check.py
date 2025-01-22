# Write a program to print the Fibonacci Series
# and also check its elements are prime or composite.
#   0,1,1,2,3,5,8,13,....
def fibo(n):
    a=0
    b=1
    L=[]
    while a<=n:
        L.append(a)
        a,b=b,a+b
    return L
n=""
while not n.isdigit():
    n=input("Enter the upper limit:")
n=int(n)
print("Fibonacci Series:")
L=fibo(n)
print(L)
for i in range(L[0],n):
    c=0
    for j in range (2,i):
        if i%j==0:
            c+=1
    if i==1 or i==0:
        print(L[i],"is not prime, not composite")
    elif c==0:
        print(L[i],"is prime")
    else:
        print(L[i],"is composite")