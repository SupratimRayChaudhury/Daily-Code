# Print Fibonacci Series (Using No. of Terms):
#   0,1,1,2,3,5,8,13,....

n=""
while not n.isdigit():
    n=input("Enter number of terms to print:")
n=int(n)
a=0
b=1
print("Fibonacci Series:")
for i in range(n):
    print(a,end=",")
    a,b=b,a+b