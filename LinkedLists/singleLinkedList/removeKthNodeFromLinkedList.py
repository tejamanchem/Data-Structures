class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        if self.head is None:
            self.head = Node(data)
            return
        newNode = Node(data)

        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next = newNode

    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return
        temp = self.head
        while temp!=None:
            if temp.next !=None:
                print(temp.data,end='->')
            else:
                print(temp.data,end='')
            temp=temp.next
        print()

    def removeKthNode(self,index):

        if self.head is None:
            return
        temp=self.head
        prevNode = None

        for i in range(1,index):
            prev= temp
            temp=temp.next

        prev.next = temp.next
        return
    
linkedList = LinkedList()
linkedList.pushNodes(1)
linkedList.pushNodes(2)
linkedList.pushNodes(3)
linkedList.pushNodes(4)
linkedList.pushNodes(5)

linkedList.printLinkedList()

linkedList.removeKthNode(2)
linkedList.printLinkedList()