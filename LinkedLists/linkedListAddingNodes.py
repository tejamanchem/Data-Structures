

class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

    
class LinkedList:

    def __init__(self):
        self.head = None

    def addingFirst(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head=newNode
            return

        temp = self.head

        self.head = newNode

        newNode.next = temp

    

    def addedAfter(self,data,prevNode):

        newNode = Node(data)

        if prevNode is None:
            print('prev node mist be in the linked list')
            return

        newNode.next = prevNode.next

        prevNode.next = newNode

       

    def appendNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while(last.next):
            last=last.next

        last.next = newNode


    def printLinkedList(self):

        temp = self.head
        if self.head is None:
            print('linked list is empty')
            return

        while(temp):
            print(temp.data,end=' ')
            temp=temp.next

linkedList1= LinkedList()
linkedList1.addingFirst(1)
linkedList1.appendNode(2)
linkedList1.appendNode(3)
linkedList1.addingFirst(4)
linkedList1.addedAfter(5,linkedList1.head.next.next)
linkedList1.printLinkedList()

    

