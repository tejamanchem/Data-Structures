
class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next


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

        newNode = Node(data=data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head 
        while temp.next:
            temp = temp.next

        temp.next = newNode
        newNode.prev = temp

        return

    def addAfterNode(self,data,prevNode):

        newNode = Node(data=data)

        if prevNode is None:
            print('Unable add Without previous node in linked list')
            return

        newNode.next = prevNode.next

        prevNode.next = newNode

        newNode.prev = prevNode

        if newNode.next is not None:
            newNode.next.prev = newNode

        return

    def reverseDoublyLinkedList(self):

        if self.head is None:
            print('unable to reverse linked list')
            return

        temp = None
        current = self.head

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
    
        if temp is not None:
            self.head = temp.prev

        return

    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

        print()



d3 = DoublyLinkedList()
d3.pushNode(1)
d3.appendNode(2)
d3.appendNode(5)
d3.printLinkedList()
d3.addAfterNode(3,d3.head.next)
d3.printLinkedList()
d3.addAfterNode(4,d3.head.next.next)
d3.printLinkedList()
d3.reverseDoublyLinkedList()
d3.printLinkedList()
       

