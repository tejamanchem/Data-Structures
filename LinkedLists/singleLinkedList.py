
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    
class LinkedList:

    def __init__(self):
        self.head =None
        self.lastNode= None

    
    def appendItems(self,item):

        if self.head is None:
            self.head = Node(item)
            self.lastNode = self.head

        else:
            self.lastNode.next = Node(item)
            self.lastNode = self.lastNode.next

        
    def printElements(self):
        if self.head is None:
            print("linked list is empty")
            return
        current = self.head

        while(current):
            print(current.data,end=' ')
            current=current.next


    
node1= LinkedList()
node1.appendItems(1)
node1.appendItems(2)
node1.appendItems(3)
node1.appendItems(4)
node1.appendItems(5)
node1.appendItems(6)
node1.printElements()