class Node:
    def __init__(self,data):
        self.data= data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def pushNode(self,data):
        if self.head is None:
            self.head= Node(data=data)
            return

        newnode = Node(data)
        temp = self.head
        while temp.next:
            temp=temp.next

        temp.next = newnode

        return

    def removeDuplicates(self):
        temp= self.head

        if self.head is None:
            return

        while temp.next:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new

            else:
                temp = temp.next

        return self.head


    def deleteNodeInLinkedList(self,key):
        
        temp =  self.head

        if temp is not None:
            if temp.data == key:
                self.head =  temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev= temp
            temp = temp.next
        
        if temp is None:
            return
        
        prev.next  =  temp.next
        temp = None


    def printLinkedList(self):
        temp = self.head

        while temp:
            if(temp.next):
                print(temp.data,end='->')
            else:
                print(temp.data,end='')
            temp = temp.next

        print()

        return


linkedList = LinkedList()

linkedList.pushNode(11)
linkedList.pushNode(11)
linkedList.pushNode(11)
linkedList.pushNode(20)
linkedList.pushNode(22)
linkedList.pushNode(30)
linkedList.pushNode(31)
linkedList.pushNode(31)
linkedList.pushNode(32)

linkedList.printLinkedList()

linkedList.head= linkedList.removeDuplicates()
linkedList.printLinkedList()

linkedList.deleteNodeInLinkedList(22)
linkedList.printLinkedList()
