
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head =  None

    def pushNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        newNode.next = temp
        self.head =newNode 

    def swapNodes(self,x,y):

        if x==y:
            return

        prevX = None
        currX = self.head
        while(currX !=None and currX.data!=x):
            prevX = currX
            currX= currX.next

        prevY = None
        currY = self.head
        while(currY!=None and currY.data!=y):
            prevY = currY
            currY=currY.next

        if currX==None or currY==None:
            return

        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY
        if prevY !=None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def printLinkedList(self):
        if self.head is None:
            print('no elements in the linked list')
            return

        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next

        print('')

list4 = LinkedList()
list4.pushNode(1)
list4.pushNode(2)
list4.pushNode(3)
list4.pushNode(4)
list4.pushNode(5)
list4.pushNode(6)
list4.printLinkedList()
print("")
list4.swapNodes(2,5)
list4.printLinkedList()
        
