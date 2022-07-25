
class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        newNode = Node(data=data)

        newNode.next= self.head

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode


    def appendNode(self,data):

        newNode = Node(data=data)
        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        newNode.next = temp.next
        temp.next = newNode
        return

    def addAfter(self,data,prevNode):

        if prevNode == None or data == None :
            return

        newNode = Node(data=data)

        newNode.next = prevNode.next

        newNode.prev = prevNode

        prevNode.next = newNode

        if newNode.next:
            newNode.next.prev= newNode

        return



    def getLastNode(self,head):
        if head is None:
            print('unable to Get Last node In Empty LinkedList')
            return

        temp = self.head
        while temp.next:
            temp = temp.next


        return temp

    def partition(self,low1,high1):
       
        x = high1.data
        i = low1.prev
        j=low1

        while (j != high1):
            if j.data <= x:

                i= low1 if(i is None) else i.next

                temp = i.data
                i.data = j.data
                j.data = temp

            j=j.next

        i = low1 if(i is None) else i.next
        temp = i.data
        i.data = high1.data
        high1.data = temp
        return i


    def _quickSortForLinkedList(self,low,high):
        if (high != None and low != high  and low != high.next):
     
            temp = self.partition(low,high)
            self._quickSortForLinkedList(low,temp.prev)
            self._quickSortForLinkedList(temp.next,high)


    def quickSort(self,node):

        if node is None:
            print('unable to process Quick sort on empty linked list')
            return

       

        head = self.getLastNode(node)

        self._quickSortForLinkedList(node,head)

        

    def printLinkedList(self):

        if self.head is None:
            print('No elements in the liked list')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

        print()


lq1=DoublyLinkedList()
lq1.pushNodes(1)
lq1.pushNodes(9)
lq1.addAfter(6,lq1.head)
lq1.appendNode(2)
lq1.addAfter(5,lq1.head.next)
lq1.appendNode(3)
lq1.printLinkedList()
lq1.quickSort(lq1.head)
lq1.printLinkedList()
lq1.appendNode(8)
lq1.quickSort(lq1.head)
lq1.printLinkedList()
