class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head= None

    def addBegining(self,data):

        newNode = Node(data)
        current =  self.head
        newNode.next = self.head

        if  self.head is None:
            newNode.next = newNode
        else:
            while current.next != self.head:
                current = current.next

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

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
            if temp == self.head:
                break


c1 = CircularLinkedList()
c1.addBegining(4)
c1.addBegining(3)
c1.addBegining(2)
c1.addBegining(1)
c1.appendNode(5)
c1.appendNode(7)
c1.addAfter(6,5)
c1.addBegining(0)

c1.printLinkedList()