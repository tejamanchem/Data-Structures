class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head =  None

    def appendNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp=self.head 
        while temp.next:
            temp=temp.next
        temp.next = newNode

        return

    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return

        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()

    def reverseOnGroupSize(self,k=1):

        if self.head is None:
            return

        current=self.head
        prev = None
        newStack=[]

        while current:
            val=0

            while current is not None and val<k:
                newStack.append(current.data)
                current=current.next
                val+=1

            while newStack:
                if prev is None:
                    prev = Node(newStack.pop())
                    self.head = prev

                else:
                    prev.next = Node(newStack.pop())
                    prev = prev.next
        prev.next = None
        return self.head



r1 = LinkedList()
r1.appendNode(1)
r1.appendNode(2)
r1.appendNode(3)
r1.appendNode(4)
r1.appendNode(5)
r1.appendNode(6)
r1.appendNode(7)
r1.appendNode(8)
r1.appendNode(9)

r1.printLinkedList()

r1.head=r1.reverseOnGroupSize()

r1.printLinkedList()




