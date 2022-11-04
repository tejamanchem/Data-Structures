

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode

        return

    def RemoveDuplicates(self,head):

        if head is None and head.next is None:
            return

        hash = set()
        current = head
        hash.add(current.data)
        
        while current.next is not None:

            if current.next.data in hash:

                current.next = current.next.next

            else:
                hash.add(current.next.data)
                current = current.next

        return head
    def printLinkedList(self):
        if self.head is None:
            print('No Elements In The Linked List')
            return
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()


l1 = LinkedList()
l1.pushNodes(1)
l1.pushNodes(1)
l1.pushNodes(2)
l1.pushNodes(3)
l1.pushNodes(4)
l1.pushNodes(5)
l1.pushNodes(3)
l1.pushNodes(2)
l1.pushNodes(3)
l1.pushNodes(4)
l1.pushNodes(5)
l1.printLinkedList()
l1.head = l1.RemoveDuplicates(l1.head)
l1.printLinkedList()
