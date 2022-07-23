
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def pushNode(self,data):
        
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            return

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
            return

        current = self.head
        newNode = Node(data)
        while current.next != self.head:
            current = current.next

        newNode.next = current.next
        current.next = newNode


    def addAfter(self,data,prevNode):

        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            return

        current = self.head
        newNode = Node(data)
        while current.next != self.head:
            if current.data == prevNode:
                newNode.next = current.next
                current.next = newNode
                return
            current = current.next

        if current.next == self.head:
            newNode.next = current.next
            current.next = newNode
  

    def sortCircularLinkedList(self,newNode):
        current = self.head

        if self.head is None:
            newNode.next = newNode
            self.head  = newNode
            
        
        elif(current.data >= newNode.data):
            
            while current.next != self.head:
                current = current.next

            current.next = newNode
            newNode.next = self.head
            self.head = newNode

        else:

            while current.next != self.head and current.next.data < newNode.data:
                current = current.next       

            newNode.next = current.next
            current.next = newNode


    def printLinkedList(self):
        if self.head is None:
            print('No elements in the linked List')
            return
                                                                            
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

            if temp == self.head:
                break

        print()



c1 = CircularLinkedList()
c1.pushNode(5)
c1.pushNode(4)
c1.pushNode(3)
c1.pushNode(3)
c1.pushNode(2)
c1.pushNode(1)
c1.printLinkedList()

c2 = CircularLinkedList()
print('For Sorted Linked List How Many Elements Need:')
size = int(input())

for  i in range(size):
    print('Enter Element Want To Add To Linked List')
    temp = Node(int(input()))
    c2.sortCircularLinkedList(temp)

print('Circular linked List After Sorting')
c2.printLinkedList()

c3 = CircularLinkedList()
c3.addAfter(1,0)
c3.addAfter(2,1)
c3.addAfter(3,2)
c3.printLinkedList()

