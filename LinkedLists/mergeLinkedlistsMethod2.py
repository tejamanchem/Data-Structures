class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def pushNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head 
        
        self.head = newNode

    def printLinkedList(self):
        if self.head is None:
            print('No Elements In The LinkedList')
            return

        temp = self.head
        while temp:
            print(temp.data,end= ' ')
            temp = temp.next

        print('')

    def mergeLinkedList(self,list1,list2):
        print(list1.data)
        
        if list1 is None:
            return list2

        if list2 is None:
           
            return list1
        if list1.data <= list2.data:
            head1 = list1
            list1=list1.next

        else:
            head1 = list2
            list2 = list2.next

        current = head1

        while list1!=None or list2!=None:

            if list1 is None:
                current.next = list2
                break
            if list2 is None:
                current.next = list1

            if list1.data <= list2.data:
                current.next = list1
                list1=list1.next

            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        return head1

l1 = LinkedList()
l2 = LinkedList()

l1.pushNode(4)
l1.pushNode(3)
l1.pushNode(2)
l1.pushNode(1)

l2.pushNode(6)
l2.pushNode(5)
l2.pushNode(9)
l2.pushNode(7)

print('the linked lists are')
l1.printLinkedList()
l2.printLinkedList()

l1.head = l1.mergeLinkedList(l1.head,l2.head)
print('After Merging')
l1.printLinkedList()