from email.quoprimime import header_decode


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):
        newNode =  Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head 
        while temp.next:
            temp =temp.next

        temp.next = newNode
        return

    def printLinkedList(self):
        if self.head is None:
            print('No elements in the linked list')
            return

        temp= self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()


    def add1ToLinkedList(self,head):

        if head is None:
            return

        ln = head

        if head.next is None:
            head.data = head.data+1
            return head

        t = head
        prev = None
        while(t.next != None):
            if(t.data != 9):
                ln=t
            t=t.next

        if (t.data ==9 and ln != None):
            t=ln
            t.data+=1
            t=t.next
            while (t!=None):
                t.data = 0
                t=t.next

        else:
            t.data = t.data+1
        return head



l1 = LinkedList()
l1.pushNodes(1)
l1.pushNodes(2)
l1.pushNodes(3)
l1.printLinkedList()
l1.head = l1.add1ToLinkedList(l1.head)
l1.printLinkedList()
