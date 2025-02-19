def enqueue(deque,front,rear):
    a=input("1.Enqueue in the Rear\n2.Enqueue in the front\n")
    if a=='1':
        deque,front,rear=enqueue_rear(deque,front,rear)
    elif a=='2':
        deque,front,rear=enqueue_front(deque,front,rear)
    else:
        print("Invalid Input:")
    return deque,front,rear
    
def enqueue_rear(deque,front,rear):
    if rear==s-1:
        print("Enqueue is not possible in rear side.")
    else:
        rear+=1
        if front==-1:
            front+=1
        deque[rear]=input("Enter a value:")
    return deque,front,rear
    
def enqueue_front(deque,front,rear):
    if front==0:
        print("Enqueue is not possible in front.")
    else:
        if front==-1:
            front+=1
            rear+=1
        else:
            front-=1
        deque[front]=input("Enter a value:")
    return deque,front,rear

def dequeue(deque,front,rear):
    b=input("1.Deque in the front\n2.Deque in the rear")
    if b=='1':
        deque,front,rear=dequeue_rear(deque,front,rear)
    elif b=='2':
        deque,front,rear=dequeue_front(deque,front,rear)
    else:
        print("Invalid input")
    return deque,front,rear

def dequeue_rear(deque,front,rear):
        if rear==-1:
            print("Queue is empty:")
        else:
            deque[rear]=""
        if front==rear:
            front=-1
            rear=-1
        else:
            rear-=1
        return deque,front,rear
        
def dequeue_front(deque,front,rear):
    if front==-1:
        print("Queue is empty.")
    else:
        deque[front]=""
    if front==rear:
        front=-1
        rear=-1
    else:
        front+=1
    return(deque,front,rear)

deque=[]
s=int(input("Enter the size:"))
for i in range(s):
    deque.append("")
front=-1
rear=-1
while True:
    n=input("1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n")
    if n=='1':
        deque,front,rear=enqueue(deque,front,rear)
    elif n=='2':
        deque,front,rear=dequeue(deque,front,rear)
    elif n=='3':
        print(deque)
    elif n=='4':
        break
    else:
        print("Invalid Input")