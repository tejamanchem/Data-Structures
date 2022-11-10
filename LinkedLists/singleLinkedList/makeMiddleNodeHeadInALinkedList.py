class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        if self.head ==None:
            newNode = Node(data)
            self.head = newNode
            return
        newNode =  Node(data)

        temp = self.head
        while temp. next != None:
            temp = temp.next

        temp.next = newNode
        return

    def makeMiddleElemtnAsHead(self):

        if self.head is None:
            return
        
        oneNode = self.head
        twoNode = self.head

        while twoNode!=None and twoNode.next != None:
            prevNode = oneNode

            oneNode = oneNode.next

            twoNode =twoNode.next.next

        prevNode.next = oneNode.next
        oneNode.next = self.head
        self.head = oneNode

        return

    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return

        temp=self.head
        while temp!=None:
            if(temp.next !=None):
                 print(temp.data,end='->')
            else:
                print(temp.data,end='')
            temp=temp.next

        print()



linkedList1 = LinkedList()
linkedList1.pushNodes(1)
linkedList1.pushNodes(2)
linkedList1.pushNodes(3)
linkedList1.pushNodes(4)
linkedList1.pushNodes(5)
linkedList1.printLinkedList()
linkedList1.makeMiddleElemtnAsHead()
linkedList1.printLinkedList()
