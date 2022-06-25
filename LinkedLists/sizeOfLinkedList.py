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

        last = self.head 

        while(last.next):
            last = last.next

        last.next= newNode

    def printLinkedList(self):

        if self.head is None:
            print('no nodes in the linked list')
            return

        temp = self.head 

        while(temp):
            print(temp.data,end=' ')
            temp = temp.next

    def countOfLinkedList(self):

        if self.head is None:
            print('the count of linked list is 0')
            return

        count =0
        temp = self.head
        while(temp):
            count = count+1
            temp = temp.next

        return count

list3 = LinkedList()
list3.appendNode(1)
list3.appendNode(2)
list3.appendNode(3)
list3.appendNode(4)
list3.appendNode(5)
list3.appendNode(6)
list3.appendNode(7)
list3.appendNode(8)
list3.appendNode(9)
list3.printLinkedList()
print("")
print('the count of linked list is :',list3.countOfLinkedList())