class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushNodes(self,nodeData):

        if self.head is None:
            self.head = Node(nodeData)
            return

        newNode = Node(nodeData)

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        return
    def insertAtMiddle(self,node):
        
        if self.head is None:
            self.head = Node(node)
            return
        newNode= Node(node)

        slowP=  self.head
        fastP = self.head.next

        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
        newNode.next = slowP.next
        slowP.next =  newNode
        return

    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return
        temp=self.head
        while temp:
            if temp.next:
                print(temp.data,end='->')
            else:
                print(temp.data,end='')
            temp=temp.next
        print()


linkedList = LinkedList()
linkedList.pushNodes(1)
linkedList.pushNodes(2)
linkedList.pushNodes(4)
linkedList.pushNodes(5)
linkedList.printLinkedList()
linkedList.insertAtMiddle(3)
linkedList.printLinkedList()
linkedList.insertAtMiddle(6)
linkedList.printLinkedList()