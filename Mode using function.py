# WAP to input n numbers and find the Mode using function.
def mode(L):
    D={}
    for i in L:
        if str(i)in D.keys():
            x=D.get(str(i))
            x+=1
            D.update({str(i):x})
        else:
            D.update({str(i):1})
    ##########################
    print("KEYS \t FREQUENCY")
    for i in D.items():
        print(i[0],"\t",i[1])
    ##########################
    x=[]
    for i in D.items():
        if i[1]==max(D.values()):
            x.append(i[0])
    return x

n=int(input("Enter Size:"))
L=[]
for i in range(n):
    L.append(input("Element-"+str(i+1)+":"))
print("GIVEN DATA:",L,"\n")
y=mode(L)
print("\nMode:",y)