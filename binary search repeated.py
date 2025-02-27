# WAP to input an array and search elements repeatedly 
# using Binary Search Technique.
n=''
while not n.isdigit():
    n=input("Enter Size:")
n=int(n)
print("Enter",n,"Elements in Ascending Order.")
a=[]
for i in range(n):
    v=''
    while not v.isdigit():
        v=input("Enter Item-"+str(i+1)+":")
    a.append(int(v))
# ** SEARCHING CODE BELLOW **
while True:
    print("Given Array: ",a)
    Key=''
    while not Key.isdigit() and Key!='@':
        Key=input("Enter the value to search (@ to Exit):")
    if Key=='@':
        break
    Key=int(Key)
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