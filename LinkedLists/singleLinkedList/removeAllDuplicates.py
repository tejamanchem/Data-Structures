
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        temp =self.head 
        while temp.next:
            temp=temp.next
        temp.next = node
    
    def printl(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current= current.next
        print('')


    def removeDups(self):
        currentNode = self.head
        element_list =[]
        prevNode = None

        while currentNode is not None:
            if currentNode.data not in element_list:
                element_list.append(currentNode.data)
                prevNode = currentNode
                currentNode = currentNode.next
            else:
                prevNode.next = currentNode.next
                currentNode = currentNode.next

        return


l= LinkedList()
l.insert(15)
l.insert(14)
l.insert(16)
l.insert(15)
l.insert(15)
l.insert(14)
l.insert(18)
l.insert(159)
l.insert(12)
l.insert(10)
l.insert(15)
l.insert(14)

l.printl()
print("===============")

l.removeDups()
l.printl()