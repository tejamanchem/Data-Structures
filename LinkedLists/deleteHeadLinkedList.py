class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def appendNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
            
        last = self.head      
        while(last.next):
            last = last.next

        last.next = newNode

    def deleteHead(self):

        if self.head is None:
            print('no elements in the linked list ')
            return

        temp = self.head
        self.head = temp.next
    
    def printLinkedList(self):
        if self.head is None:
            print('No nodes in the linked list')
            return

        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next

list4 = LinkedList()
list4.appendNode(1)
list4.appendNode(2)
list4.appendNode(3)
list4.appendNode(4)
list4.appendNode(5)
list4.appendNode(6)
list4.appendNode(7)
list4.appendNode(8)
list4.appendNode(9)
list4.deleteHead()
list4.printLinkedList()
list4.deleteHead()
print("")
list4.printLinkedList()