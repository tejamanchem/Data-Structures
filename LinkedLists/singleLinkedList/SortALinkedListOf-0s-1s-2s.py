class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def appendNodes(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp=temp.next

        temp.next = newNode

        return

    def printLinkedList(self):

        if self.head is None:
            print('Non elemenst in the linked list')
            return

        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next

        print()

    def swap0_1_2(self,head1):

        if head1 is None:
            return

        count=[0,0,0]
        ptr1 = head1

        while ptr1:
            count[ptr1.data]+=1
            ptr1 = ptr1.next
        
        i=0
        ptr = head1

        while ptr:

            if count[i]==0:
                i=i+1
            else:
                ptr.data = i
                count[ptr.data]-=1
                ptr=ptr.next




s1 = LinkedList()
s1.appendNodes(1)
s1.appendNodes(2)
s1.appendNodes(0)
s1.appendNodes(0)
s1.appendNodes(1)
s1.appendNodes(1)
s1.appendNodes(2)
s1.appendNodes(0)
s1.printLinkedList()
s1.swap0_1_2(s1.head)
s1.printLinkedList()