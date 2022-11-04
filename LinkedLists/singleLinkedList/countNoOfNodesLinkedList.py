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

        current = self.head
        while current.next:
            current = current.next

        current.next = newNode

        return

    def printLinkedList(self):

        if self.head is None:
            print('No Elemenst In the Linked List')
            return

        temp =self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

        print()

    def countAllElements(self,head1):

        if head1 is None:
            print('Linked List is Empty')
            return

        count =0
        temp = head1
        while temp:
            count = count+1
            temp = temp.next

        return count

    def countSpecifiedKey(self,head1,key):

        if head1 is None:
            return
        if key is None:
            print('Key must be Exists')
            return

        count =0
        temp=head1

        while temp:
            if temp.data == key.data:
                count = count+1
            temp=temp.next
        
        return count


md1 = LinkedList()
md1.appendNodes(1)
md1.appendNodes(2)
md1.appendNodes(3)
md1.appendNodes(4)
md1.appendNodes(5)
md1.appendNodes(3)
md1.printLinkedList()
print(md1.countAllElements(md1.head))            
print(md1.countSpecifiedKey(md1.head,md1.head.next.next))