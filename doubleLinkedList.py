
class Node:

    def __init__(self,data):
        self.data = data
        self.prevNode=None
        self.next=None

    
class LinkedList:

    def __init__(self):
        self.head=None
        self.startNode =None
        self.lastNode = None

    def append(self,data):
        if self.head is None:
            self.head=Node(data)
            self.lastNode = self.head

        else:
            newNode = Node(data)
            self.lastNode.next= newNode
            newNode.prevNode = self.lastNode
            newNode.next = None
            self.lastNode = newNode

    def Display(self,symbol):
            if symbol =='LtoR':
                current = self.head
                while(current):
                    print(current.data,end=' ')
                    current = current.next
                print()
            else:
                current = self.lastNode
                while(current):
                    print(current.data,end=' ')
                    current = current.prevNode
                print()


Nodeobj = LinkedList()

Nodeobj.append(1)
Nodeobj.append(2)
Nodeobj.append(3)
Nodeobj.append(4)
Nodeobj.append(5)
Nodeobj.append(6)   
Nodeobj.Display('LtoR')
Nodeobj.Display('fdgd')             




        