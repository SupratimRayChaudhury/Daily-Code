# WAP to Implement Circular Queue

n=int(input("Enter Size:"))
queue=[]
for i in range(n):
    queue.append('')
front=-1
rear=-1
while(True):
    c=input("1. ENQUEUE()\n2. DEQUEUE()\n3. Display\n4. Exit\n")
    if c=='1':
        if (rear+1)%n==front:
            print("Circular Queue is Full. Can't Enqueue.")
        else:
            rear=(rear+1)%n
            if front==-1:
                front=0
            queue[rear]=input("Enter Value to Enqueue:")
    elif c=='2':
        if front==-1:
            print("Circular Queue is Empty. Can't Dequeue.")
        else:
            queue[front]=''
            if front==rear:
                front=-1
                rear=-1
            else:
                front=(front+1)%n
    elif c=='3':
        for i in range(n):
            if i==front==rear:
                print("[",queue[i],"]","<-Front, Rear")
            elif i==front:
                print("[",queue[i],"]","<-Front")
            elif i==rear:
                print("[",queue[i],"]","<-Rear")
            else:
                print("[",queue[i],"]")
    elif c=='4':
        break
    else:
        print("Invalid Input!")