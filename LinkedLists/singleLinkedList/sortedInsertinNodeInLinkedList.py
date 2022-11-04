
from findMergePointOfTwoLinkedLists import LinkedList1

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
        while last.next:
            last = last.next

        last.next = newNode

    
    def printLinkedList(self):

        if self.head is None:
            print('no elements in the linked list')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

        print('')


    def sortedInsert(self,llist,data):

        newNode = Node(data)

        if llist is None:
            return newNode

        lastNode = llist
        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode

        newNodeList = LinkedList1()
       
        sortedInsertResult = newNodeList.mergeSort(self.head)

        return sortedInsertResult



l1 = LinkedList()

l1.appendNode(1)
l1.appendNode(4)
l1.appendNode(3)
l1.appendNode(10)

print('linked list is')
l1.printLinkedList()

l1.head=l1.sortedInsert(l1.head,5)

print('After inseritng a newNode the linked list is ')

l1.printLinkedList()



