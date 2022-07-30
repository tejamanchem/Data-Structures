
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertNodeAtEnd(self,data):

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
            print('No elements in the linked list')
            return

        temp = self.head 
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

        print('')

    
    def removeDuplicates(self,head1):

        if head1 is None:
            return

        node1 = head1

        while node1:

            lead = node1
            while node1.next and node1.next.data ==lead.data:
                node1 = node1.next

            node1 = lead.next = node1.next

        return head1

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

   
l1 = LinkedList()
l1.insertNodeAtEnd(1)
l1.insertNodeAtEnd(1)
l1.insertNodeAtEnd(1)
l1.insertNodeAtEnd(2)
l1.insertNodeAtEnd(2)
l1.insertNodeAtEnd(2)
l1.insertNodeAtEnd(2)
l1.insertNodeAtEnd(2)
l1.insertNodeAtEnd(3)
l1.insertNodeAtEnd(4)
l1.insertNodeAtEnd(4)
l1.insertNodeAtEnd(5)
l1.insertNodeAtEnd(3)
l1.insertNodeAtEnd(4)
l1.insertNodeAtEnd(4)
l1.insertNodeAtEnd(5)
l1.printLinkedList()

l1.removeDuplicates(l1.head)
l1.printLinkedList()
l1.removeDups()
l1.printLinkedList()


l2= LinkedList()
l2.insertNodeAtEnd(5)
l2.insertNodeAtEnd(2)
l2.insertNodeAtEnd(2)
l2.insertNodeAtEnd(4)
l2.printLinkedList()
l2.removeDups()
l2.printLinkedList()
