
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head=None

    def printLinkedList(self):
        temp=self.head

        while temp:
            print(temp.data,end=' ')
            temp=temp.next


linkedList1  = LinkedList()

linkedList1.head=Node(1)

node2 = Node(3)

node3 = Node(4)

linkedList1.head.next=node2
node2.next=node3

linkedList1.printLinkedList()

