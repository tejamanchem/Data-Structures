from multiprocessing import set_forkserver_preload


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None


    def addBeging(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            newNode = Node(data)
            current = self.head 

            while current.next != self.head:
                current = current.next

            newNode.next = self.head
            current.next = newNode
            self.head = newNode


    def appendNode(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            newNode = Node(data)

            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = newNode
            newNode.next = self.head

        
    def addAfter(self,data,prevNode):

        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head

        else:

            newNode = Node(data)
            current = self.head 
            while current.next != self.head:
                if current.data == prevNode:
                    newNode.next = current.next
                    current.next = newNode
                current = current.next


    def reverseCircularLinkedList(self):
        if self.head is None:
            print('No elements in the linked List')
            return
        else:
            current = self.head
            prevNode = None

            newData = current.next
            current.next = prevNode
            prevNode = current
            current = newData
            while current != self.head:
             
                newData = current.next
                current.next = prevNode
                prevNode = current
                current = newData

            self.head.next = prevNode
            self.head = prevNode



    def printCircularLinkedList(self):
        if self.head is None:
            print('No elements in the linked list')
            return

        current = self.head
        while current:
            print(current.data,end='->')
            current = current.next

            if current == self.head:
                break

c4 = CircularLinkedList()
c4.addBeging(4)
c4.addBeging(3)
c4.addBeging(2)
c4.addBeging(1)
c4.appendNode(5)
c4.addBeging(0)
c4.addAfter(8,3)
c4.printCircularLinkedList()
c4.reverseCircularLinkedList()
print('')
c4.printCircularLinkedList()           
