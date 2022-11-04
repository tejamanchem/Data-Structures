
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

    def pushNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head

        self.head = newNode

    def printLinkedList(self):
        if self.head is None:
            print('linked list is empty')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

        print('')

    def getNode(self,head1,position):
        if head1 is None:
            return 
        if head1.next is None:
            return head1.data

        lenList=0
        ptr = head1 
        
        while ptr.next:
            lenList+=1
            ptr = ptr.next

        while lenList > position:
            head1 = head1.next
            lenList -=1

        return head1.data

    
l1 = LinkedList()

l1.appendNode(1)
l1.appendNode(2)
l1.appendNode(3)
print(l1.getNode(l1.head,2))
