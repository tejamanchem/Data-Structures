class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def appendNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next = newNode

        return

    def printLinkedList(self):

        if self.head is None:
            print('No Elements in the linked list')
            return
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next

        print()

    def sortedInsert(self,a,b):
        if a==None or b==None:
            return None

        if a.data < b.data:
            return self.sortedInsert(a.next,b)
        if a.data > b.data:
            return self.sortedInsert(a,b.next)

        temp = Node()
        temp.data = a.data

        temp.next = self.sortedInsert(a.next,b.next)
        return temp



ll1 = LinkedList()
ll1.appendNode(5)
ll1.appendNode(2)
ll1.appendNode(1)
ll1.appendNode(3)
ll1.printLinkedList()

ll2 = LinkedList()
ll2.appendNode(6)
ll2.appendNode(9)
ll2.appendNode(7)
ll2.printLinkedList()

ll11 = ll1.sortedInsert(ll1.head,ll2.head)
print(ll11)
ll1.printLinkedList()


