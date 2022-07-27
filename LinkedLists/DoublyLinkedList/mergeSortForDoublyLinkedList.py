from platform import node
from re import T


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
        return
    def mergeLinkedLists(self,node1,node2):

        if node1 is None:
            return node2
        if node2 is None:
            return node1

        if node1.data < node2.data:
            node1.next = self.mergeLinkedLists(node1.next,node2)
            node1.next.prev = node1
            node1.prev = None
            return node1

        else:
            node2.next = self.mergeLinkedLists(node1,node2.next)
            node2.next.prev = node2
            node2.prev = None
            return node2

    def partition(self,tempHead):
        fast = slow = tempHead

        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None

        return temp

    def mergesort(self,tempHead):

        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead

        second = self.partition(tempHead)

        tempHead = self.mergesort(tempHead)

        second = self.mergesort(second)

        return self.mergeLinkedLists(tempHead,second)


    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return

        temp =self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()



dl1 = DoublyLinkedList()
dl1.printLinkedList()
dl1.pushNode(1)
dl1.pushNode(2)
dl1.pushNode(3)
dl1.pushNode(4)
dl1.pushNode(5)
dl1.pushNode(6)
dl1.printLinkedList()
dl1.head = dl1.mergesort(dl1.head)
dl1.printLinkedList()
dl1.pushNode(8)
dl1.printLinkedList()
dl1.head = dl1.mergesort(dl1.head)
dl1.printLinkedList()
