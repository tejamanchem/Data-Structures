class Node:

    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        newnode = Node(data=data)

        newnode.next = self.head

        if self.head is not None:
            self.head.prev = newnode

        self.head = newnode

        return

    def appendNode(self,data):

        newNode = Node(data=data)

        if self.head is None:
            self.head = newNode
            return

        
        temp=self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode
        newNode.prev = temp
        return


    def sortedInsert(self,data):

        newNode = Node(data=data)

        if self.head is None:
            self.head = newNode
            return

        elif (self.head.data >= newNode.data):

            newNode.next = self.head
            newNode.next.prev = newNode
            self.head = newNode

            return

        else:

            current = self.head

            while current.next is not None and current.next.data < newNode.data:
                current = current.next

            newNode.next = current.next

            if current.next is not None:
                newNode.next.prev = newNode

            current.next = newNode

            newNode.prev = current

            return

        


    def printLinkedList(self):

        if self.head is None:
            print('No Elements In The Linked List')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()


dl1 = DoublyLinkedList()
dl1.pushNodes(1)
dl1.appendNode(3)
dl1.appendNode(5)
dl1.appendNode(6)
dl1.printLinkedList()
dl1.sortedInsert(2)
dl1.printLinkedList()
dl1.sortedInsert(4)
dl1.sortedInsert(7)
dl1.printLinkedList()


        

