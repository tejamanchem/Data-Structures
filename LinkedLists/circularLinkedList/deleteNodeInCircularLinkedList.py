class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None

    def appendNode(self,data):
        
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            newNode = Node(data)
            current = self.head 
            while current.next != self.head:
                current= current.next

            current.next = newNode
            newNode.next = self.head


    def addAtBeginig(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            current = self.head 
            newNode = Node(data)

            while current.next !=self.head:
                current = current.next

            newNode.next = self.head
            current.next = newNode
            self.head = newNode

        
    def addAfter(self,data,prevNode):

        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head

        else:

            newNode= Node(data)
            current = self.head

            while current.next != self.head:
                if current.data == prevNode:
                    newNode.next = current.next
                    current.next = newNode
                current = current.next

    def deleteNode(self,key):

        if self.head is None:
            print('No elements in the linked List')
            return

        temp = self.head
        prevNode= None

        if temp.data == key:
            if temp.next == temp:
                self.head = None
            else:
                while temp.next != self.head:
                    temp = temp.next

                temp.next = self.head.next
                prevNode = self.head
                self.head = prevNode.next

        else:
            temp = self.head.next
            prevNode = self.head
            while temp!= self.head:
                if temp.data == key:

                    prevNode.next = temp.next
                    temp=None
                    prevNode=None
                    break
                prevNode = temp 
                temp = temp.next

            if (temp!=None):
                print('key not present in the linked List')



    def printLinkedList(self):

        if self.head is None:
            print('No Nodes In The Linked List')
            return
        
        current = self.head

        while current:
            print(current.data,end=' ')
            current = current.next
            if current == self.head:
                break
        

c2 = CircularLinkedList()
c2.appendNode(1)
c2.addAtBeginig(8)
c2.appendNode(2)
c2.appendNode(3)
c2.appendNode(4)
c2.appendNode(5)
c2.appendNode(6)
c2.addAfter(7,5)
c2.addAtBeginig(0)
c2.appendNode(9)
c2.deleteNode(8)
c2.printLinkedList()