# WAP to input an array and search elements repeatedly 
# using Recursive function of Binary Search Technique.
def search(arr,v,h,l):
        m=(l+h)//2
        if l<=h:
            if arr[m]==v:
                return m
            elif arr[m]>v:
                  return search(arr,v,m-1,l)
            elif arr[m]<v:
                  return search(arr,v,h,m+1)
        else:
            return None

n=int(input("Enter Size:"))
arr=[]
print("Enter element in assending order:")
for i in range(n):
    arr.append(int(input("Element-"+str(i+1)+":")))
print("GIVEN ARRAY:\n",arr)
while True:
    v=""
    while not v.isdigit() and v!="@":
        v=input("Enter the value to Search (@ to exit):")
    if v=="@":
        break
    v=int(v)
    p=search(arr,v,len(arr)-1,0)
    if p==None:
        print("NOT FOUND")
    else:
        print(v,"found at index",p,"position",p+1)