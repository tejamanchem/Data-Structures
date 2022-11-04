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

    def printReverse(self,head1):

        if head1:
            self.printReverse(head1.next)
            print(head1.data,end=' ')
        else:
            return

        


    def setReverseLinkedList(self,head2):

        prev=None
        current = head2

        while current is not None:

            nextNode,current.next = current.next,prev
            prev,current = current,nextNode

        head2 = prev

        return head2

r1 = LinkedList()
r1.pushNode(4)
r1.pushNode(3)
r1.pushNode(2)
r1.pushNode(1)
r1.printLinkedList()
r1.printReverse(r1.head)
print()
r1.printLinkedList()
r1.head = r1.setReverseLinkedList(r1.head)
r1.printLinkedList()