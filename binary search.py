# WAP to input an array and search an element using
# Binary Search Technique.
n=int(input("Enter Size:"))
print("Enter",n,"Elements in Ascending Order.")
a=[]
for i in range(n):
    a.append(int(input("Enter Item-"+str(i+1)+":")))
print(a)
Key=int(input("Enter the value to search:"))
L=0
U=n-1
found=False
while L<=U:
    M=(L+U)//2
    if a[M]==Key:
        print(Key,"found at position",M+1,"(Index =",M,")")
        found=True
        break
    elif a[M]>Key:
        U=M-1
    elif a[M]<Key:
        L=M+1
if not found:
    print("Not Found!")