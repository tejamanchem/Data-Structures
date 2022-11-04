class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        newNode.next = self.head

        self.head = newNode

        return

    def printLinkedList(self):

        if self.head is None:
            print('No elemenst in the linked list')
            return

        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp =temp.next

        print()

    def pairWiseSwap(self,head1):

        temp = head1

        if temp is None:
            return

        while temp and temp.next:

            if temp.data != temp.next.data:
                temp.data ,temp.next.data = temp.next.data , temp.data

            temp = temp.next.next

        


ps1=LinkedList()
ps1.pushNodes(5)
ps1.pushNodes(4)
ps1.pushNodes(3)
ps1.pushNodes(2)
ps1.pushNodes(1)
ps1.printLinkedList()
ps1.pairWiseSwap(ps1.head)
ps1.printLinkedList()