class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self, data):

        if self.head is None:
            self.head = Node(data)
            return

        newNode = Node(data)
        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = newNode

        return

    def insertANodeFromN_Node(self, head1, n, x):

        if head1 is None:
            return

        if n is None:
            return

        if x is None:
            return

        newNode = Node(x)
        ptr = head1
        i = 0
        l = 0

        while ptr != None:
            l += 1
            ptr = ptr.next

        ptr = head1
        i = 1
        while (i <= (l-n)):
            ptr = ptr.next
            i = i+1

        newNode.next = ptr.next
        ptr.next = newNode

        return head1

    def printLinkedList(self):
        if self.head is None:
            print('No elements in the linked list')
            return
        temp = self.head
        while temp != None:
            if temp.next != None:
                print(temp.data, end='->')
            else:
                print(temp.data, end='')
            temp = temp.next
        print()
        return


linkedList1 = LinkedList()
linkedList1.pushNodes(1)
linkedList1.pushNodes(2)
linkedList1.pushNodes(3)
linkedList1.pushNodes(4)
linkedList1.pushNodes(5)
linkedList1.pushNodes(6)
linkedList1.pushNodes(7)
linkedList1.pushNodes(9)
linkedList1.printLinkedList()

linkedList1.head = linkedList1.insertANodeFromN_Node(linkedList1.head,2,8)
linkedList1.printLinkedList()
