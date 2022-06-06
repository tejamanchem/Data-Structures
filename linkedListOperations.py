
class Node:

    def __init__(self,item):
        self.data = item
        self.next=None
#
class LinkedList:

    def __init__(self):
        self.head=None

    def insertAtBegining(self,data):

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self,prevNode,data):

        if prevNode is None:
            print('the given prevNode must be in linked list')
            return
        

        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode


    def insertAtEnd(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while(last.next):
            last=last.next

        last.next = newNode
    def deleteNode(self,position):

        if self.head is None:
            return

        temp = self.head

        if position==0:
            self.head = temp.next
            temp = None
            return

        
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:

            return

        next = temp.next.next

        temp.next = None

        temp.next = next


      # Search an element
    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    # Sort the linked list
    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBegining(2)
    llist.insertAtBegining(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 5)

    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()

    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sortLinkedList(llist.head)
    print("Sorted List: ")
    llist.printList()

