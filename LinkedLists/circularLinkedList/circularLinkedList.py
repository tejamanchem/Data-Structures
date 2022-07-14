
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head=None
        self.lastNode= None

    def append(self,data):
        
        if self.head is None:
            self.head = Node(data)
            self.lastNode=self.head

        else:
            self.lastNode.next= Node(data)
            self.lastNode = self.lastNode.next
            self.lastNode.next = self.head

   

    def display(self):

        current = self.head

        while(current):
            print(current.data,end=' ')
            current= current.next

            if current == self.head:
                break


newcircularLinkedList = CircularLinkedList()
newcircularLinkedList.append(1)
newcircularLinkedList.append(2)
newcircularLinkedList.append(3)
newcircularLinkedList.append(5)
newcircularLinkedList.append(6)
newcircularLinkedList.append(7)
newcircularLinkedList.append(8)
newcircularLinkedList.append(9)
newcircularLinkedList.display()
































