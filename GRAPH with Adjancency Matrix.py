# input a graph and print List Representation and Adjancency Matrix.
n=int(input("enter the number of Vertices (1 to 20):"))
d=dict()
for i in range(65,65+n):
   d.update({chr(i):set()})
print("VERTICES:",end='')
for i in d.keys():
   print(i,end=',')
print('')
s=input("Please enter edges:\n[e.g: AB, AC etc]")
a=s.upper().split(',')
for i in a:
   if len(i)>=2:
      if i[0] in d.keys() and i[1] in d.keys():
         s=d.get(i[0])
         s.add(i[1])
         d.update({i[0]:s})
         
         s=d.get(i[1])
         s.add(i[0])
         d.update({i[1]:s})

print('\n** GRAPH **')
for i in d.keys():
   if len(d[i])==0:
      print(i,'->','{ }')
   else:
      print(i,'->',d[i])
print('\n** ADJACENCY MATRIX **')
for i in d.keys():
    print('\t',i,end='',sep='')
for i in d.keys():
    print('\n',i,'\t',end='')
    for j in d.keys():
        if j in d.get(i):
            print('1\t',end='')
        else:
            print('0\t',end='')