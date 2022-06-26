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

    
