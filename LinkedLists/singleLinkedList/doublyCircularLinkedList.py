
class Node:

    def __init__(self,data):
        self.data = data
        self.prevNode = None
        self.next = None

class DoublyCircularLinkedList:

    def __init__(self):
        self.head = None
        self.startNode =None
        self.lastNode = None

    def append(self,data):

        if self.head is None:
            self.head = Node(data)
            self.lastNode = self.head

        else:
            newNode = Node(data)
            self.lastNode.next = newNode
            newNode.prevNode = self.lastNode
            newNode.next = self.head
            self.lastNode = newNode

    def display(self,symbol):
        if symbol=='LtoR':
            current = self.head
            while(current):
                print(current.data,end=' ')
                current = current.next
                if current == self.head:
                    break
            print()

        else:
            current = self.lastNode
            while(current):
                print(current.data,end=' ')
                current=current.prevNode
                # if current==self.head:
                #     break
            print()


newDCList = DoublyCircularLinkedList()
newDCList.append(1)
newDCList.append(2)
newDCList.append(3)
newDCList.append(4)
newDCList.append(5)
newDCList.append(6)
newDCList.append(7)
newDCList.append(8)
newDCList.append(9)
newDCList.display('LtoR')
newDCList.display('bdjfsd')

