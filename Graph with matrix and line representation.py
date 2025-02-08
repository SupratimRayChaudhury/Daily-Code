# input a graph with weights and print List Representation and Adjancency Matrix.
n=int(input("enter the number of Vertices (1 to 20):"))
d=dict()
for i in range(65,65+n):
   d.update({chr(i):set()})
print("VERTICES:",end='')
for i in d.keys():
   print(i,end=',')
print('')
s=input("Please enter edges and weights:\n[e.g: AB5, AC27 etc]")
a=s.upper().split(',')
for i in a:
   if len(i)>=3:
      w=i[2:len(i)]
      if i[0] in d.keys() and i[1] in d.keys() and w.isdigit():
         s=d.get(i[0])
         s.add(i[1]+'/'+w)
         d.update({i[0]:s})
         
         s=d.get(i[1])
         s.add(i[0]+'/'+w)
         d.update({i[1]:s})
print(d)
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
        c=0
        for k in d.get(i):
            w=k[2:len(k)]
            if j==k[0]:
                print(w+'\t',end='')
                c+=1
        if c==0:
            print('-\t',end='')