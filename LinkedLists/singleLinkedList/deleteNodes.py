

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head=None


    def addNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head= newNode
            return

        newNode.next = self.head

        self.head=newNode

    def deleteFirst(self):

        temp = self.head
        if self.head is None:
            print('no items in the linked list')
            return

        self.head = temp.next

    def deleteAfter(self,prevNode):

        if self.head is None:
            print('no nodes in the linked list')
            return

        temp = prevNode.next

        prevNode.next = temp.next

        
         
    def deleteLast(self):
        if self.head is None:
            print('linkedlis is empty')
            return

        temp = self.head 

        while(temp.next.next):
            temp=temp.next

        temp.next = None

    def deleteKey(self,key):

        if self.head is None:
            print('No nodes in the linked list')
            return
        
        temp = self.head
        prevNode=None

        while(temp):
            if temp.data==key:
                prevNode.next = temp.next
                break
            prevNode = temp
            temp=temp.next
        return
    
    def printLinkedList(self):
        temp = self.head
        print("")
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next

list1 = LinkedList()

list1.addNode(1)
list1.addNode(2)
list1.addNode(3)
list1.addNode(4)
list1.addNode(5)
list1.deleteFirst()
list1.deleteLast()
list1.printLinkedList()
list1.deleteAfter(list1.head)

list1.printLinkedList()
list1.deleteKey(2)
list1.printLinkedList()


        

        

        

