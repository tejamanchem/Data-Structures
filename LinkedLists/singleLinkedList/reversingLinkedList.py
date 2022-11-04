class Node:

    def __init__(self,data):
        self.data = data
        self.next =None

class LinkedList:

    def __init__(self):
        self.head = None

    def pushNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return


        temp = self.head

        self.head = newNode

        newNode.next = temp


    def reverseLinkedList(self):

        if self.head is None:
            print('linked is empty')
            return

        temp = self.head
        prevNode =None
        while(temp):
            newData = temp.next
            temp.next = prevNode
            prevNode =  temp
            temp = newData

        self.head = prevNode

    def printLinkedList(self):

        temp = self.head
        print("")
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next


list2 = LinkedList()
list2.pushNode(1)
list2.pushNode(2)
list2.pushNode(3)
list2.pushNode(4)
list2.pushNode(5)
list2.pushNode(6)
list2.pushNode(7)
list2.pushNode(8)
list2.printLinkedList()
list2.reverseLinkedList()
list2.printLinkedList()

