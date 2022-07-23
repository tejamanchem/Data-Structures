class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        newNode = Node(data=data)

        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode

    def appendNode(self,data):

        newNode = Node(data=data)
        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp= temp.next

        temp.next=newNode
        newNode.prev = temp
        return

    def addAfter(self,data,prevNode=None):

        newNode = Node(data=data)

        if prevNode is None:
            print('Cannot insert After witout a prevNode')
            return

        newNode.next = prevNode.next

        prevNode.next = newNode

        newNode.prev = prevNode

        if newNode.next is not None:
            newNode.next.prev = newNode
        
        return

    def deleteNode(self,node):
        
        if self.head is None or node is  None:
            return
        if self.head == node:
            
            self.head = node.next
            return
        
        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        return


    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

        print()


d2 = DoublyLinkedList()
d2.appendNode(1)
d2.appendNode(2)
d2.appendNode(4)
d2.printLinkedList()
d2.addAfter(3,d2.head.next)
d2.pushNodes(0)
d2.printLinkedList()
d2.deleteNode(d2.head)
d2.printLinkedList()
            

        

        

        