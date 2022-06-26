
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtEnd(self,data):
        
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    
    def printLinkedList(self):

        if self.head is None:
            print('no elements in the linked list')
            return
        
        temp = self.head
        print('')
        while temp:
            print(temp.data,end=' ')
            temp = temp.next


def mergeLinkedList(headA,headB):

    dummyNode = Node(0)

    tail = dummyNode

    while True:


        if headA is None:
            tail.next = headB
            break
        
        if headB is None:
            tail.next = headA
            break
            	
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        tail = tail.next

    return dummyNode.next


list1 = LinkedList()
list2 = LinkedList()

list1.insertAtEnd(5)
list1.insertAtEnd(10)
list1.insertAtEnd(15)

list1.printLinkedList()

list2.insertAtEnd(2)
list2.insertAtEnd(3)
list2.insertAtEnd(20)

list2.printLinkedList()

list1.head=mergeLinkedList(list1.head,list2.head)

print('After Merging')
list1.printLinkedList()
list2.printLinkedList()







    


