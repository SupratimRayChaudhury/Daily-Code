#WAP to Implement Queue using Enqueue(), Dequeue(), Display() functions.

def enqueue(queue,front,rear):
    if rear==(len(queue)-1):
        print("Queue is Full. Can't Enqueue.")
    else:
        rear=rear+1
    if front==-1:
        front=front+1
    queue[rear]=input("Enter Value to Enqueue:")
    return queue,front,rear

def dequeue(queue,front,rear):
    if front==-1:
        print("Queue is Empty. Can't Dequeue.")
    else:
        queue[front]=''
    if front==rear:
        front=-1
        rear=-1
    else:
        front=front+1
    return queue,front,rear

def display(queue,front,rear):
    for i in range(len(queue)):
        if i==front==rear:
            print("[",queue[i],"]","<-Front, Rear")
        elif i==front:
            print("[",queue[i],"]","<-Front")
        elif i==rear:
            print("[",queue[i],"]","<-Rear")
        else:
            print("[",queue[i],"]")

n=int(input("Enter Size:"))
queue=[]
for i in range(n):
    queue.append('')
front=-1
rear=-1
while(True):
    c=int(input(" 1.ENQUEUE\n 2.DEQUEUE\n 3.DISPLAY\n 4.EXIT\n"))
    if c==1:
        queue,front,rear=enqueue(queue,front,rear)
    elif c==2:
        queue,front,rear=dequeue(queue,front,rear)
    elif c==3:
        display(queue,front,rear)
    elif c==4:
        break
    else:
        print("invalid input")