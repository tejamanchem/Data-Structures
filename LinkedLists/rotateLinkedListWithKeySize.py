from tkinter.messagebox import RETRY


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

    def printLinkedList(self):

        if self.head is None:
            print('no elements in the linked list')
            return
        
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

        print('')

    def rotateList(self,k):
    
        if self.head is None:
            print('no elements in the linked list to rotate')
            return
        if k is None:
            return

        currentNode =  self.head
        count =1
        while count < k and currentNode.next is not None:
            currentNode = currentNode.next
            count+=1

        
        kThNode = currentNode

        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = self.head

        self.head = kThNode.next

        kThNode.next = None

       
list1 = LinkedList()
list1.pushNode(60)
list1.pushNode(50)
list1.pushNode(40)
list1.pushNode(30)
list1.pushNode(20)
list1.pushNode(10)
print('linked list is')
list1.printLinkedList()
list1.rotateList(4)
list1.printLinkedList()