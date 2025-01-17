# WAP to input n numbers and find the Mode.
n=int(input("Enter Size:"))
L=[]
for i in range(n):
    L.append(input("Element-"+str(i+1)+":"))
print(L)
D={}
for i in L:
    if str(i)in D.keys():
        x=D.get(str(i))
        x+=1
        D.update({str(i):x})
    else:
        D.update({str(i):1})
print(D)  
print("Mode: ")
for i in D.items():
    if i[1]==max(D.values()):
        print(i[0],end=",")