class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushNode(self,data):

        newNode = Node(data=data)

        if self.head is None:
            self.head = newNode
            return
        
        temp =  self.head
        newNode.next = temp 
        self.head = newNode


    def removeDuplicates(self,head):
        
        if head is None:
            return


        if(head.next !=None):

            if(head.data == head.next.data):
                toFree = head.next
                head.next = head.next.next

                self.removeDuplicates(head)

            else:
                self.removeDuplicates(head.next)

        return head

    def printLinkedList(self):

        if self.head is None:
            print('No Elements in the linked list')
            return

        temp=self.head

        while temp:
            if temp.next is not None:
                print(temp.data,end='->')

            else:
                print(temp.data,end='')

            temp=temp.next
        print()

linkedList = LinkedList()
linkedList.pushNode(11)
linkedList.pushNode(11)
linkedList.pushNode(20)
linkedList.pushNode(21)
linkedList.pushNode(30)
linkedList.pushNode(30)
linkedList.pushNode(30)
linkedList.pushNode(33)

linkedList.printLinkedList()

linkedList.head = linkedList.removeDuplicates(linkedList.head)

linkedList.printLinkedList()
