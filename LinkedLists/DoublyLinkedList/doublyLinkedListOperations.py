
class Node:

    def __init__(self,data=None,prev = None,next= None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self):
        self.head = None


    def pushNode(self,data):

        newNode = Node(data=data)
        
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode

    def appendNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
        newNode.prev = last
        return

    def addAfter(self,data,prevNode):

        if prevNode is None:
            print('Çannot insert Without previous Node')
            return

        newNode = Node(data=data)

        newNode.next = prevNode.next

        prevNode.next = newNode

        newNode.prev = prevNode

        if newNode.next :
            newNode.next.prev = newNode

        return

    def printLinkedList(self):

        if self.head is None:
            print('No Elements In The Linked list')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp= temp.next

        print()

d1 = DoublyLinkedList()
d1.pushNode(1)
d1.appendNode(2)
d1.appendNode(3)
d1.appendNode(4)
d1.appendNode(5)
d1.printLinkedList()
d1.addAfter(0,d1.head.next.next)
d1.printLinkedList()



    

        
