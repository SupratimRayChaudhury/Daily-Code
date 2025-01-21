# Write a function that returns the
# Fibonacci Series as List
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