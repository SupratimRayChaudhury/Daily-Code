# input a list and check prime or composite
n=""
while not n.isdigit():
    n=input("Enter the size:")
n=int(n)
arr=[] 
for i in range(n):
    t=""
    while not t.isdigit():
        t=input("Enter item no."+ str(i+1)+":")
    arr.append(int(t))
print("\nThe Given Array is:\n\t",arr)
for i in arr:
    c=0
    for j in range (2,i):
        if i%j==0:
            c+=1
    if i==1:
        print(i,"is not prime, not composite")
    elif c==0:
        print(i,"is prime")
    else:
        print(i,"is composite")