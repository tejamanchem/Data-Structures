class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            return
        
        temp = self.head
        newNode = Node(data)
        while temp.next != self.head:
            temp=temp.next

        newNode.next = self.head
        temp.next = newNode
        self.head = newNode

    def appendNodes(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            return
        
        temp = self.head
        newNode = Node(data)
        while temp.next != self.head:
            temp = temp.next


        newNode.next = temp.next
        temp.next = newNode

    def addAfter(self,data,prevNode):

        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            return

        newNode = Node(data)
        temp = self.head

        while temp.next != self.head:
            if temp.data == prevNode:
                newNode.next = temp.next
                temp.next = newNode
                return

            temp = temp.next

        if temp.next == self.head:                  
            newNode.next = temp.next 
            temp.next =newNode


        
    def splitLinkedLists(self,head1,head2):

        if self.head is None:
            return

        fastPtr = self.head
        slowPtr = self.head

        while fastPtr.next != self.head and fastPtr.next.next != self.head:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

        if fastPtr.next.next == self.head:
            fastPtr = fastPtr.next

        head1.head = self.head

        if self.head.next !=self.head:
            head2.head = slowPtr.next

        fastPtr.next = slowPtr.next
        slowPtr.next = self.head
    def printCircularLinkedList(self):
        if self.head is None:
            print('No elements in the Linked List')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
            if temp == self.head:
                break


c5 = CircularLinkedList()
head1 = CircularLinkedList()
head2 = CircularLinkedList()
c5.pushNodes(6)
c5.pushNodes(5)
c5.pushNodes(4)
c5.pushNodes(3)
c5.pushNodes(2)
c5.pushNodes(1)
c5.addAfter(7,6)
c5.addAfter(9,7)
c5.appendNodes(10)
c5.addAfter(8,7)
c5.addAfter(0,5)
c5.printCircularLinkedList()
c5.splitLinkedLists(head1,head2)
print('\nFirst Half')
head1.printCircularLinkedList()
print('\nsecond Half')
head2.printCircularLinkedList()

        