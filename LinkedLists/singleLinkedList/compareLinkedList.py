from traceback import print_tb
from pyparsing import one_of


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def pushNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head

        self.head = newNode

    def printList(self):

        if self.head is None:
            print('no elements in the linked list')
            return

        temp = self.head
        while temp:
            print(temp.data,end='')
            temp = temp.next
        print('')

    def compareLinkedList(self,list1,list2):

        if list1 is None:
            return 1 if list2 is None else 0
        if list2 is None:
            return 0
        if list1.data != list2.data:
            return 1
        else:
            self.compareLinkedList(list1.next,list2.next)

        
l1 = LinkedList()
l2 = LinkedList()

l1.pushNode(4)
l1.pushNode(3)
l1.pushNode(2)
l1.pushNode(1)


l2.pushNode(3)
l2.pushNode(2)
l2.pushNode(1)

print('linked list are')
l1.printList()
l2.printList()

a=l1.compareLinkedList
if a==1:
    print('linked list matched')
else:
    print('not matched')





        