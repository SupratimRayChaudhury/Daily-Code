# WAP to input an array of n elements and search
# an element using a function of linear search.
def ser(v,arr):
    found=False
    for i in range(len(arr)):
        if arr[i]==v:
            print(v,"found at position",(i+1),"(Index =",i,")")
            found=True
    if not found:
        print(v,"not Found")
        
#***main*****
n=int(input("Enter Size:"))

arr=[]
for i in range(n):
    arr.append(int(input("Element-"+str(i+1)+":")))
    
u="0"
while True:
    print("GIVEN ARRAY:\n",arr)
    u=input("Enter the value to Search (@ to exit):")
    if u=="@":
        break
    v=int(u)
    ser(v,arr)