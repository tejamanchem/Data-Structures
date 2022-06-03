#class forr queue operation
class Queue:

    #constructor for creating the queue
    def __init__(self):
        self.queue=[]

    #enqueuing the element to the queue
    def enqueue(self,item):
        self.queue.append(item)

    #dequeing the element from the queue
    def dequeue(self):
        if len(self.queue) <1:
            return None
        return self.queue.pop(0)

    #size of the queue
    def size(self):
        return len(self.queue)

    #displaying the elements in the queue
    def display(self):
        print(self.queue)
newqueueobj = Queue()
def userinput():
    print("enter your choice :")
    print("1.enqueue\n2.dequeue\n3.display\n4.size")
    userinn = int(input())
    if(userinn==1):
        print("enter item :")
        item = input()
        newqueueobj.enqueue(item)
        userinput()
    elif(userinn==2):
        newqueueobj.dequeue()
        userinput()

    elif(userinn==3):
        newqueueobj.display()
        userinput()
    else:
        newqueueobj.size()
        userinput
    
userinput()