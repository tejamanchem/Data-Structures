class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self,data):

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def partition(self, start, end):
        pivot = start 
      
        cur = start
        while (cur != None and cur != end):
            if (cur.data < end.data):
                pivot = start
                start.data, cur.data = cur.data,start.data
                self.printList()
                
                start = start.next
            cur = cur.next
        start.data,end.data = end.data, start.data
        return pivot

    def quickSort(self, start, end):
 
        if start == end:
            return

        pivot = self.partition(start, end)

        if (pivot != None and pivot.next != None):
            self.quickSort(pivot.next, end)

        if (pivot != None and start != pivot):
            self.quickSort(start, pivot)

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next

        print('')

l1 = LinkedList()
l1.insertAtBegining(1)
l1.insertAtBegining(2)
l1.insertAtBegining(3)
l1.insertAtBegining(4)
n=l1.head
while n.next:
    n= n.next

l1.printList()
l1.quickSort(l1.head,n)
l1.printList()