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
            self.head =  newNode
            return

        newNode.next = self.head

        self.head = newNode

    def reverseLinkedList(self,h,k):

        if h == None:
            return None

        currentNode = h
        prevNode = None
        nextNode = None
        count=0
        while currentNode is not None and count < k:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
            count+=1                       

        if nextNode is not None:
            h.next =  self.reverseLinkedList(nextNode,k)
        

        return prevNode

    def reverseLinkedListWithSpecifiedSize(self,head1,size):
        if size is None:
            return head1
        if head1 is None:
            return

        temp = head1
        prev = None
        count = 0
        while temp is not None and count <size:
            nextNode = temp.next
            temp.next = prev
            prev = temp
            temp = nextNode
            count+=1

        head1.next = temp
        self.head = prev
        return prev


    def printLinkedList(self):

        if self.head is None:
            print('Linked list is empty')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp= temp.next
            
        print('')

    
li = LinkedList()
li.pushNode(9)
li.pushNode(8)
li.pushNode(7)
li.pushNode(6)
li.pushNode(5)
li.pushNode(4)
li.pushNode(3)
li.pushNode(2)
li.pushNode(1)
li.printLinkedList()
li.head=li.reverseLinkedList(li.head,3)
li.printLinkedList()

l2 = LinkedList()
l2.pushNode(70)
l2.pushNode(60)
l2.pushNode(50)
l2.pushNode(40)
l2.pushNode(30)
l2.pushNode(20)
l2.pushNode(10)
print('Second Linked List')
l2.printLinkedList()
l2.head = l2.reverseLinkedListWithSpecifiedSize(l2.head,3)
l2.printLinkedList()
    
