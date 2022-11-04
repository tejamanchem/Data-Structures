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

        newNode.next = self.head
        self.head = newNode
        return

    def printLinkedList(self):

        if self.head is None:
            print('No Elemenst in the linked list')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next

        print()

    def searchNode(self,head1,key):
        if head1 is None:
            return

        if key is None:
            print('Key is nedded for searching')
            return

        l=[]
        temp=head1
        while temp:
            l.append(temp.data)
            if key in l:
                return 'key found'
            temp=temp.next

        return 'key not found'

       
        
s1 = LinkedList()
s1.pushNodes(5)
s1.pushNodes(4)
s1.pushNodes(3)
s1.pushNodes(2)
s1.pushNodes(1)
s1.printLinkedList()
print(s1.searchNode(s1.head,9))
        