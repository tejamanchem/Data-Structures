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

        temp=self.head

        while temp.next:
            temp=temp.next
        temp.next=newNode
        return
    
    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked lists')
            return
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()

    def getNthNode(self,n):
        if self.head is None:
            return

        length=0
        temp=self.head

        while temp:
            length+=1
            temp=temp.next

        if n>length:
            print('location is greater than the length of the linked list')
            return

        curr = self.head
        for i in range(0,length-1):
            curr=curr.next

        return curr.data


l1 = LinkedList()
l1.printLinkedList()
l1.appendNode(1)
l1.appendNode(2)
l1.appendNode(3)
l1.appendNode(4)
l1.appendNode(5)
l1.printLinkedList()
print(l1.getNthNode(1))