class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):
        
        if self.head is None:
            self.head = Node(data)
            return
        newNode = Node(data)

        temp = self.head
        while temp.next !=None:
            temp = temp.next
        temp.next = newNode
        return
    
    def checkEvenOrOdd(self):
        if self.head is None:
            print('No elements in the linked list')
            return

        temp =self.head
        listLength = 0
        while temp!= None:
            listLength+=1
            temp = temp.next
        if(listLength%2==0):
            print('EVEN')
        else:
            print('ODD')
    
    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return
        temp =self.head
        while temp!=None:
            if temp.next!=None:
                print(temp.data,end='->')
            else:
                print(temp.data,end='')
            temp = temp.next
        print()


linkedList1 = LinkedList()
linkedList1.pushNodes(1)
linkedList1.pushNodes(2)
linkedList1.pushNodes(3)
linkedList1.pushNodes(4)

linkedList2 = LinkedList()
linkedList2.pushNodes(5)
linkedList2.pushNodes(4)
linkedList2.pushNodes(3)
linkedList2.pushNodes(2)
linkedList2.pushNodes(1)

linkedList1.printLinkedList()
linkedList2.printLinkedList()

linkedList2.checkEvenOrOdd()
linkedList1.checkEvenOrOdd()
