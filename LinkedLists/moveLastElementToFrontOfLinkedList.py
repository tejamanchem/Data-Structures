from platform import node
from traceback import print_tb


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def appendNodes(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode
        return

    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return

        temp= self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()

    def lastToFirst(self,head1):

        current = head1
        prev = head1
        while current.next:
            prev = current
            current=current.next

        
        current.next = head1
        head1= current
        prev.next = None
        return head1
        

       


l1 = LinkedList()
l1.appendNodes(1)
l1.appendNodes(2)
l1.appendNodes(3)
l1.appendNodes(4)
l1.appendNodes(5)
l1.printLinkedList()
l1.head=l1.lastToFirst(l1.head)
l1.printLinkedList()
