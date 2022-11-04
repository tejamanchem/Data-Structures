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

        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = newNode

        return

    def getIntersectionPoint(self,head1,head2):

        if head1 is None:
            return head2
        if head2 is None:
            return head1

        hs = set()

        
        while head1 != None:
            hs.add(head1)
            head1 = head1.next
        
        while head2  != None:
            if head2 in hs :
                return head2.data
            head2 = head2.next

        

    def printLinkedList(self):

        if self.head is None:
            print('No Elements In The Linked List')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

        print()


l3 = LinkedList()
l3.pushNode(7)
l3.pushNode(8)
l3.pushNode(9)

l1 = LinkedList()
l1.pushNode(1)
l1.pushNode(2)
l1.pushNode(3)
l1.pushNode(4)
l1.pushNode(5)
l1.pushNode(6)
l1.head.next.next.next.next.next.next = l3.head
l1.printLinkedList()




l2 = LinkedList()
l2.pushNode(8)
l2.pushNode(9)
l2.pushNode(10)
l2.pushNode(4)
l2.pushNode(5)
l2.pushNode(6)
l2.head.next.next.next.next.next.next = l3.head
l2.printLinkedList()
print(l1.getIntersectionPoint(l1.head,l2.head))